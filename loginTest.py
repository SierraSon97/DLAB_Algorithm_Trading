import sys
from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtWidgets import QApplication


class trueFriendAPI:
    def __init__(self):
        self.OCXconn = QAxWidget("ITGExpertCtl Control")

    def login(self):
        ret = self.OCXconn.dynamicCall("GetAccountCount()")
        print(ret)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = trueFriendAPI()
    test.login()
    app.exec_()