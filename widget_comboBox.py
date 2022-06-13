import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()  # 부모클래스의 초기화자 호출
        self.initWindow()


    def initWindow(self):

        combo = QComboBox(self)
        combo.addItem('사과')
        combo.addItem('수박')
        combo.addItem('멜론')
        combo.addItem('딸기')

        self.label1 = QLabel('선택', self)
        self.label1.move(50, 100)

        combo.activated[str].connect(self.onCombo)

        self.setGeometry(100, 100, 300, 300)
        self.show()

    def onCombo(self, text):
        self.label1.setText(text)


if __name__ == '__main__':  # 이벤트 루프 만드는법
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())