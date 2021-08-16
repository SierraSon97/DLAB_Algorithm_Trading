import win32com.client
import pandas as pd
import matplotlib.pyplot as plt

# 종목들 가져오기
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
stockNum = instCpStockCode.GetCount()

# 종목코드 리스트 구하기
objCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
codeList = objCpCodeMgr.GetStockListByMarket(1) # 거래소
codeList2 = objCpCodeMgr.GetStockListByMarket(2) # 코스닥

# 차트 객체 구하기
objStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

# 현재가 객체 구하기
objStockMst = win32com.client.Dispatch("DsCbo1.StockMst")

instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")

objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")



class getChartData():
    def getObjStock(self, stockcode):
        objStockMst.SetInputValue(0, stockcode)
        objStockMst.BlockRequest()

    def findStock(self, stockname):
        for i in range(stockNum):
            if instCpStockCode.GetData(1, i) == stockname:
                return instCpStockCode.GetData(0, i)
        return 0

    def setInputValue(self, stockcode):
        objStockChart.SetInputValue(0, stockcode)  # 종목 코드
        objStockChart.SetInputValue(1, ord('2'))  # 개수로 조회
        objStockChart.SetInputValue(4, 100)  # 최근 100일 치
        objStockChart.SetInputValue(5, [0, 2, 3, 4, 5, 8])  # 날짜,시가,고가,저가,종가,거래량
        objStockChart.SetInputValue(6, ord('D'))  # '차트 주가 - 일간 차트 요청
        objStockChart.SetInputValue(9, ord('1'))  # 수정주가 사용
        objStockChart.BlockRequest()

    def setInputValue(self, stockcode, startdate, enddate):
        objStockChart.SetInputValue(0, stockcode)  # 종목 코드
        objStockChart.SetInputValue(1, ord('2'))  # 개수로 조회
        objStockChart.SetInputValue(2, startdate)
        objStockChart.SetInputValue(3, enddate)
        objStockChart.SetInputValue(4, 100)  # 최근 100일 치
        objStockChart.SetInputValue(5, [0, 2, 3, 4, 5, 8])  # 날짜,시가,고가,저가,종가,거래량
        objStockChart.SetInputValue(6, ord('D'))  # '차트 주가 - 일간 차트 요청
        objStockChart.SetInputValue(9, ord('1'))  # 수정주가 사용
        objStockChart.BlockRequest()

    def getDataValue(self):
        len = objStockChart.GetHeaderValue(3)

        day = []
        open = []
        high = []
        low = []
        close = []
        vol = []

        for i in range(len):
            day.append(objStockChart.GetDataValue(0, i))
            open.append(objStockChart.GetDataValue(1, i))
            high.append(objStockChart.GetDataValue(2, i))
            low.append(objStockChart.GetDataValue(3, i))
            close.append(objStockChart.GetDataValue(4, i))
            vol.append(objStockChart.GetDataValue(5, i))
        df = pd.DataFrame({
            'Day' : day,
            'Open' : open,
            'High' : high,
            'Low' : low,
            'Close' : close,
            'Vol' : vol
        })
        return df
    def getCurrentPrice(self, stockcode):
        objStockMst.SetInputValue(0, stockcode)
        objStockMst.BlockRequest()

        # 현재가 통신 및 통신 에러 처리
        rqStatus = objStockMst.GetDibStatus()
        rqRet = objStockMst.GetDibMsg1()
        print("통신상태", rqStatus, rqRet)
        if rqStatus != 0:
            return
        code = objStockMst.GetHeaderValue(0)  # 종목코드
        name = objStockMst.GetHeaderValue(1)  # 종목명
        time = objStockMst.GetHeaderValue(4)  # 시간
        cprice = objStockMst.GetHeaderValue(11)  # 종가
        diff = objStockMst.GetHeaderValue(12)  # 대비
        open = objStockMst.GetHeaderValue(13)  # 시가
        high = objStockMst.GetHeaderValue(14)  # 고가
        low = objStockMst.GetHeaderValue(15)  # 저가
        offer = objStockMst.GetHeaderValue(16)  # 매도호가
        bid = objStockMst.GetHeaderValue(17)  # 매수호가
        vol = objStockMst.GetHeaderValue(18)  # 거래량
        vol_value = objStockMst.GetHeaderValue(19)  # 거래대금

        # 예상 체결관련 정보
        exFlag = objStockMst.GetHeaderValue(58)  # 예상체결가 구분 플래그
        exPrice = objStockMst.GetHeaderValue(55)  # 예상체결가
        exDiff = objStockMst.GetHeaderValue(56)  # 예상체결가 전일대비
        exVol = objStockMst.GetHeaderValue(57)  # 예상체결수량

        print("코드", code)
        print("이름", name)
        print("시간", time)
        print("종가", cprice)
        print("대비", diff)
        print("시가", open)
        print("고가", high)
        print("저가", low)
        print("매도호가", offer)
        print("매수호가", bid)
        print("거래량", vol)
        print("거래대금", vol_value)

        if (exFlag == ord('0')):
            print("장 구분값: 동시호가와 장중 이외의 시간")
        elif (exFlag == ord('1')):
            print("장 구분값: 동시호가 시간")
        elif (exFlag == ord('2')):
            print("장 구분값: 장중 또는 장종료")

        print("예상체결가 대비 수량")
        print("예상체결가", exPrice)
        print("예상체결가 대비", exDiff)
        print("예상체결수량", exVol)


class getPERData():
    def SetInputValue(self, stockcode):
        instMarketEye.SetInputValue(0, (4, 67, 70, 111))
        instMarketEye.SetInputValue(1, stockcode)
        instMarketEye.BlockRequest()

    def GetData(self):
        print("현재가: ", instMarketEye.GetDataValue(0, 0))
        print("PER: ", instMarketEye.GetDataValue(1, 0))
        print("EPS: ", instMarketEye.GetDataValue(2, 0))
        print("최근분기년월: ", instMarketEye.GetDataValue(3, 0))
