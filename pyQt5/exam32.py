# 2020-11-25 결과가 출력이 안되는 버그 있음

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QTimer

# as를 이용하여 BeautifulSoup을 bs로 입력할 수 있다.
from bs4 import BeautifulSoup as bs
import urllib.request as req, sys, time

# scarp_01 모듈에서 Ui_MainWindow 클래스를 import
from scrap_01 import Ui_MainWindow

# QMainWindow, Ui_MainWindow(scrap_01) 이중 상속받음
class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # setupUi는 Ui_MainWindow의 함수
        # 이 함수에 Example 객체를 넘겨 레이아웃을 잡는다
        self.setupUi(self)

        self.timer = QTimer()

        # timer의 timeout 시그널에 chk 슬롯을 넘김
        self.timer.timeout.connect(self.chk)

        # 기본 interval을 5분으로 설정하고
        # 1000(ms)는 1초: 60은 1분: 5를 곱하면 --> 5분
        self.timer.setInterval(5 * 60 * 1000)

        # 5분에 해당하는 라디오 버튼을 체크
        self.rb_5min.setChecked(True)
        self.show()

    # 여기까지 하고 Run했을 때 AttributeError: 'Example' object has no attribute 'setCycle' 가 일어남.
    # 이미 QtDesigner에서 슬롯을 지정했는데 해당 메소드들을 구현하지 않아서 오류 발생

    # 검색 주기를 설정하는 함수
    def setCycle(self):
        if self.rb_5min.isChecked():
            self.timer.setInterval(5*60*1000)
        elif self.rb_1min.isChecked():
            self.timer.setInterval(1*60*1000)
        elif self.rb_10min.isChecked():
            self.timer.setInterval(10 * 60 * 1000)
        elif self.rb_30sec.isChecked():
            self.timer.setInterval(30*1000)
        elif self.rb_5ec.isChecked():
            self.timer.setInterval(5*1000)

    # 체크 시작
    def startChk(self):
        # url(LineEdit) 비활성화
        self.url.setEnabled(False)

        # 타이머 시작
        self.timer.start()

    def stopChk(self):
        self.url.setEnabled(True)
        self.timer.stop()

    def chk(self):

        # url 텍스트의 html 코드를 가져옴
        self.rsp = req.urlopen(self.url.text())
        self.html = bs(self.rsp, "html.parser")

        try:
            # self.html.find(alt="UP"): html 코드중 alt속성이 Up인 것을 찾는다
            # 그리고 test에 저장
            self.test = self.html.find(alt="UP").attrs['alt']
        except:
            # 없으면 XX을 저장
            self.test = "XX"

            # time 객체를 이용해 실시간으로 체크한 결과를 레이블에 나타냄
            self.t = time.localtime()
            self.lbl_print.setText("{}:{}:{} 체크결과:{}".format(self.t.tm_hour, self.t.tm_min, self.t.tm_sec, self.test))

if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    sys.exit(app.exec_())