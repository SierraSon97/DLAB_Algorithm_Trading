import sys
import win32com.client
from PyQt5 import uic
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import *
from lib import tradeLib
from lib import chartDataLib

ui = uic.loadUiType('../ui/main.ui')[0]

objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = objCpCybos.IsConnect

checkBalance = tradeLib.Cp6033()


class MainWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_chkBal.clicked.connect(self.checkBalance)
        self.btn_chkcut.clicked.connect(self.checkCount)
        self.btn_purchase.clicked.connect(self.purchase)
        self.btn_sell.clicked.connect(self.sell)

    def timeout(self):
        current_time = QTime.currentTime()
        text_time = current_time.toString("hh:mm:ss")
        time_msg = "현재시간 : " + text_time
        self.statusBar().show

    def checkBalance(self):
        retcode = int(input('계좌번호를 입력하세요 : '))
        checkBalance.Request(retcode)
        return
    def checkCount(self):
        print('test2')
        return
    def purchase(self):
        print('test3')
        return
    def sell(self):
        print('test4')
        return



if __name__== "__main__":
    if (bConnect == 0):
        print("PLUS가 정상적으로 연결되지 않음. ")
        exit()
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()



