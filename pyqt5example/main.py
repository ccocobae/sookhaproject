import sys
import pytube
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QUrl
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
        self.is_play = False

        self.youtb = None
        self.youtb_fsize = 0

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
        self.previewButton.setEnabled(True)
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
        self.previewButton.clicked.connect(self.load_url)
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.webEngineView.loadProgress.connect(self.showProgressBrowserLoading)
        self.fileNavButton.clicked.connect(self.selectDownPath)

    def load_url(self):
        url = self.urlTextEdit.text().strip()
        v = re.compile('https://www.youtube.com/?')  # ????
        if self.is_play:
            self.append_log_msg('Stop Click')
            self.webEngineView.load(QUrl('about:blank'))
            self.previewButton.setText("재생")
            self.is_play = False
            self.urlTextEdit.clear()
            self.urlTextEdit.setFocus(True)
            self.startButton.setEnabled(False)
            self.streamCombobox.clear()
            self.progressBar_2.setValue(0)
            self.showStatusMsg("인증 완료")
        else:
            if v.match(url) is not None:
                self.append_log_msg('Play click')
                self.webEngineView.load(QUrl(url))
                self.showStatusMsg(url + " is now playing.")
                self.previewButton.setText("중지")
                self.is_play = True
                self.startButton.setEnabled(True)
                self.initialYouWork(url)
            else:
                QMessageBox(self, "URL 형식 오류", "Youtube 주소 형식이 아닙니다.")
                self.urlTextEdit.clear()
                self.urlTextEdit.setFocus(True)

    def initialYouWork(self, url):
        video_list = pytube.YouTube(url)

        self.youtb = video_list.streams.all()
        self.streamCombobox.clear()
        for q in self.youtb:
            print(q)

    @pyqtSlot()
    def authCheck(self):
        dlg = AuthDialog()
        dlg.exec_()
        self.user_id = dlg.user_id
        self.user_pw = dlg.user_pw

        # 인증
        if self.user_id == "sookha" and self.user_pw == "sookha!":
            self.initAuthActive()
            self.loginButton.setText("인증 완료")
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setEnabled(True)
            self.append_log_msg("Login Success")

        else:
            QMessageBox.about(self, "인증 오류", "아이디 또는 비밀번호 인증 오류")

    def append_log_msg(self, act):
        now = datetime.datetime.now()
        nowDate = now.strftime("%Y-%m-%d %H:%M:%S")
        app_msg = self.user_id + ' : ' + str(act) + " - (" + nowDate + ")"
        print(app_msg)
        self.plainTextEdit.appendPlainText(str(app_msg))

        with open('/Users/soo/PycharmProjects/sookhaproject/pyqt5example/log/log.txt', 'a') as f:
            f.write(app_msg+'\n')

    @pyqtSlot(int)
    def showProgressBrowserLoading(self, v):  # 아니 왜 progressbar 가 거꾸로 증가하지
        self.progressBar.setValue(v)

    @pyqtSlot()
    def selectDownPath(self):
        # 파일 선택
        # fname = QFileDialog.getOpenFileName(self)
        # self.pathTextEdit.setText(fname[0])

        # 경로 선택
        fpath = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.pathTextEdit.setText(fpath)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewtube_main = Main()
    viewtube_main.show()
    app.exec_()