import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore


class TestForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyQT Test")
        self.setGeometry(800, 400, 500, 500)  # 윈도우 위치와 크기 지정

        label_1 = QLabel("입력테스트", self)
        label_2 = QLabel("출력테스트", self)

        label_1.move(20, 20)
        label_2.move(20, 60)

        self.lineEdit = QLineEdit("", self)  # Default
        self.plainEdit = QtWidgets.QPlainTextEdit(self)

        self.lineEdit.move(90, 20)
        self.plainEdit.setGeometry(QtCore.QRect(20, 90, 361, 231))

        self.lineEdit.textChanged.connect(self.lineEditChanged)  # lineEdit 에서 text에 변화가 있을 때
        self.lineEdit.returnPressed.connect(self.lineEditEnter)  # lineEdit 에서 enter 를 눌렀을 때

        self.statusBar = QStatusBar(self)  # 상태바
        self.setStatusBar(self.statusBar)

    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())  # lineEdit 에 입력된 text 를 받아와서 statusbar 에 출력

    def lineEditEnter(self):
        self.plainEdit.appendPlainText(self.lineEdit.text())  # insertPlainText 도 있다.
        self.lineEdit.clear()


if __name__ == "__main__":  # 이 파일을 '직접 실행'하는가?
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()


    app.exec_()  # 대기상태에서 시그널을 받음. (이벤트가 발생했다는 것을 알려주는 신호. 버튼이 클릭됐다거나 등등) -> 슬롯 : 이벤트를 처리함