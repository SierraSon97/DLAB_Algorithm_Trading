import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("PyStock_Login.ui")[0]

#ȭ���� ���µ� ���Ǵ� Class ����
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__" :
    #QApplication : ���α׷��� ��������ִ� Ŭ����
    app = QApplication(sys.argv) 

    #WindowClass�� �ν��Ͻ� ����
    myWindow = WindowClass() 

    #���α׷� ȭ���� �����ִ� �ڵ�
    myWindow.show()

    #���α׷��� �̺�Ʈ������ ���Խ�Ű��(���α׷��� �۵���Ű��) �ڵ�
    app.exec_()
    #test