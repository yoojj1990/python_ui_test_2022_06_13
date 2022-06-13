import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()  # 부모클래스의 초기화자 호출
        self.initWindow()


    def initWindow(self):

        lable_red = QLabel('빨강')
        lable_bule = QLabel('파랑')

        lable_red.setStyleSheet(

            "color:red;"
            "border-style:solid;"
            "border-width:2px;"
            "border-color:red;"
            "background-color:pink;"

        )

        lable_bule.setStyleSheet(

            "color:blue;"
            "border-style:solid;"
            "border-width:2px;"
            "border-color:blue;"
            "background-color:skyblue;"

        )

        styleBox = QVBoxLayout()
        styleBox.addWidget(lable_red)
        styleBox.addWidget(lable_bule)

        self.setLayout(styleBox)




        self.setGeometry(100, 100, 300, 300)
        self.show()

if __name__ == '__main__':  # 이벤트 루프 만드는법
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())