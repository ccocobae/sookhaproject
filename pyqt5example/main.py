import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
import re
import datetime
import os
from lib.ViewtubeLayout import Ui_MainWindow

form_class = uic.loadUiType('/Users/soo/PycharmProjects/sookhaproject/pyqt5example/ui/viewtube_v1.0.ui')[0]


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewtube_main = Main()
    viewtube_main.show()
    app.exec_()