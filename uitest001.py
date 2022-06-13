import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv) # QApplication 객체 생성

lable1 = QLabel("HelloWorld")
lable1.show()

button01 = QPushButton("버튼")
button01.show()




app.exec() # 이벤트 루프


