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


def getObjStock(stockCode):
    objStockMst.SetInputValue(0, stockCode)
    objStockMst.BlockRequest()

def getCodeList():
    return

def findStock(stockName):
    for i in range(stockNum):
        if instCpStockCode.GetData(1, i) == stockName:
            stockCode = instCpStockCode.GetData(0, i)
            return stockCode
    return 0

def setInputValue(stockCode):
    objStockChart.SetInputValue(0, stockCode)  # 종목 코드 - 삼성전자
    objStockChart.SetInputValue(1, ord('2'))  # 개수로 조회
    objStockChart.SetInputValue(4, 100)  # 최근 100일 치
    objStockChart.SetInputValue(5, [0, 2, 3, 4, 5, 8])  # 날짜,시가,고가,저가,종가,거래량
    objStockChart.SetInputValue(6, ord('D'))  # '차트 주가 - 일간 차트 요청
    objStockChart.SetInputValue(9, ord('1'))  # 수정주가 사용
    objStockChart.BlockRequest()

def getDataValue():
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