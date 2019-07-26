import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)  #1 sys.argv = 이 파일의 디렉토리
label = QLabel('PyQT First test!')
label.show()

app.exec_()