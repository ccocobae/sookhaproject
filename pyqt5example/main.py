import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import re
import datetime
import os
from lib.ViewtubeLayout import Ui_MainWindow
from lib.AuthDialog import AuthDialog

form_class = uic.loadUiType('/Users/soo/PycharmProjects/sookhaproject/pyqt5example/ui/viewtube_v1.0.ui')[0]


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initAuthLock()
        self.initSignal()
        self.user_id = None
        self.user_pw = None

    # 기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)  # True -> 버튼 활성화
        self.fileNavButton.setEnabled(False)
        self.streamCombobox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg('인증안됨')

    # 기본 UI 활성화
    def initAuthActive(self):
        self.previewButton.setEnabled(True)  # True -> 버튼 활성화
        self.fileNavButton.setEnabled(True)
        self.streamCombobox.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg('인증 완료')

    def showStatusMsg(self, msg):
        self.statusbar.showMessage(msg)

    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck)

    @pyqtSlot()
    def authCheck(self):
        dlg = AuthDialog()
        dlg.exec_()
        self.user_id = dlg.user_id
        self.user_pw = dlg.user_pw

        # 인증
        if self.user_id == "sookha" and self.user_pw == "sookha11!!":
            self.initAuthActive()
            self.loginButton.setText("인증 완료")
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setEnabled(True)
        else:
            QMessageBox.about(self, "인증 오류", "아이디 또는 비밀번호 인증 오류")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewtube_main = Main()
    viewtube_main.show()
    app.exec_()