import sys
import win32com.client
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
from lib import tradeLib
from lib import chartDataLib

ui = uic.loadUiType('./ui/main.ui')[0]
objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = objCpCybos.IsConnect

class MainWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def checkBalance(self):
        return
    def checkCount(self):
        return
    def purchase(self):
        return
    def sell(self):
        return



if __name__== "__main__":
    if (bConnect == 0):
        print("PLUS가 정상적으로 연결되지 않음. ")
        exit()
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()



