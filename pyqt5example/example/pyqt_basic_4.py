import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType('/Users/soo/PycharmProjects/sookhaproject/pyqt5example/example/pyqt_basic_3.ui')[0]
# pyuic5 -x pyqt_basic_3.ui -o pyqt_basic_ui.py 로 파이썬 파일로 변경시킬 수 있음

class TestForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":  # 이 파일을 '직접 실행'하는가?
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()