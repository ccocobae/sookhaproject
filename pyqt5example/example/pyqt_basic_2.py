import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class TestForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyQT Test")
        self.setGeometry(800, 400, 500, 300)  # 윈도우 위치와 크기 지정

        btn_1 = QPushButton("Click1", self)
        btn_2 = QPushButton("Click2", self)
        btn_3 = QPushButton("Click3", self)

        btn_1.move(20, 20)
        btn_2.move(20, 60)
        btn_3.move(20, 100)

        btn_1.clicked.connect(self.btn_1_clicked)  # 버튼 1이 클릭되었을 때 btn_1_clicked 메서드를 실행
        btn_2.clicked.connect(self.btn_2_clicked)
        btn_3.clicked.connect(QCoreApplication.instance().quit)

    def btn_1_clicked(self):
        QMessageBox.about(self, "message", "clicked")

    def btn_2_clicked(self):
        print("Button clicked!")


if __name__ == "__main__":  # 이 파일을 '직접 실행'하는가?
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()


    app.exec_()  # 대기상태에서 시그널을 받음. (이벤트가 발생했다는 것을 알려주는 신호. 버튼이 클릭됐다거나 등등) -> 슬롯 : 이벤트를 처리함