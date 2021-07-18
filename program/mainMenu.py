import sys
import win32com.client
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
from lib import tradeLib
from lib import chartDataLib

ui = uic.loadUiType('../ui/main.ui')[0]

objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = objCpCybos.IsConnect

class MainWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_chkBal.clicked.connect(self.checkBalance())
        self.btn_chkcut.clicked.connect(self.checkCount())
        self.btn_purchase.clicked.connect(self.purchase())
        self.btn_sell.clicked.connect(self.sell())


    def checkBalance(self):
        print('test1')
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



