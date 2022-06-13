import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):

        self.statusBar().showMessage('ver 0.0.1')  # 상태표시줄 메인윈도우에 붙이기

        exitWindow = QAction(QIcon('icons/cloud_icon.png'), 'EXIT', self)
        exitWindow.setShortcut('CTRL+Q')
        exitWindow.setStatusTip('프로그램 종료')
        exitWindow.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&파일')
        filemenu.addAction(exitWindow)


        self.setGeometry(100, 100, 300, 300)
        self.show()


if __name__ == '__main__':  # 이벤트 루프 만드는법
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())