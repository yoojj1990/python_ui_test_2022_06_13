import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()  # 부모클래스의 초기화자 호출
        self.initWindow()


    def initWindow(self):
        QToolTip.setFont(QFont("Arial", 12))
        self.setToolTip("툴팁 <U>설명</U>이 나옵니다")  # 위젯 판에 튤팁 적용

        btn1 = QPushButton('버튼1', self)
        btn1.setToolTip("버튼에 대한 설명이 나오는 곳")  # 버튼에 튤팁 적용

        self.setGeometry(100, 100, 300, 300)
        self.show()

if __name__ == '__main__':  # 이벤트 루프 만드는법
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())