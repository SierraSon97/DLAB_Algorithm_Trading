import sys
import win32com.client
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import pandas as pd
import sqlite3

class daishin():
    def __init__(self):
        super().__init__()

    def checkStatus(self):
        objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
        bConnect = objCpCybos.IsConnect
        if (bConnect == 0):
            print("PLUS가 정상적으로 연결되지 않음. ")
            return 0
        else:
            return 1
    def getStockList(self):
        objCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
        codeList = objCpCodeMgr.GetStockListByMarket(1)  # 거래소
        codeList2 = objCpCodeMgr.GetStockListByMarket(2)
