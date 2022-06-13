import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/mywin.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        #super().__init__() # 부모클래스의 초기화자를 호출(안하면 에러)
        p = super()
        p.__init__()

        self.setupUi(self)

        self.setWindowTitle("HelloWorld")
        self.setWindowIcon(QIcon("icons/cloud_icon.png"))


        self.btn1.clicked.connect(self.btn1Click)
        self.btn2.clicked.connect(self.btn2Click)

    def btn1Click(self):
        self.label1.setText("버튼1이 클릭됨")  # 슬롯
        self.lineEdit1.setText("버튼1이 클릭!!")
        print("버튼1이 클릭됨")

    def btn2Click(self):
        self.label1.setText("버튼2이 클릭됨")  # 슬롯
        self.lineEdit1.setText("버튼2이 클릭!!")
        print("버튼2이 클릭됨")

app = QApplication(sys.argv)

myWin = MyWindow()
myWin.show()


app.exec_()