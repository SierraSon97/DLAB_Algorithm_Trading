from lib import chartDataLib as sc

stockName = input('찾고자 하는 종목의 이름을 입력하시오 : ')
stockCode = sc.findStock(stockName)

if stockCode != 0:
    sc.setInputValue(stockCode)
    df = sc.getDataValue()
    print(df)
else:
    print('정확한 종목 명을 입력하세요')