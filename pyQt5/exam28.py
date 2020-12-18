from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QPushButton
from PyQt5.QtGui import *
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.sid = QImage("sonic.jpg").scaled(120, 120)

        btn = QPushButton("이미지 변경", self)
        btn.resize(btn.sizeHint())
        btn.move(20, 150)
        btn.clicked.connect(self.openFileNameDialog)
        self.setGeometry(1400, 250, 320, 200)
        self.show()

    # 이미지를 여러번 불러올때 자동으로 호출되어야하기 때문에
    # paintEvent 사용
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawImages(painter)
        painter.end()

    # painter 객체를 이용해 이미지를 불러온다
    def drawImages(self, painter):
        painter.drawImage(5, 15, self.sid)
        painter.drawImage(self.sid.width() + 10, 15, self.grayScale(self.sid.copy())) # 옆 공간에 이미지 생김

    def grayScale(self, image):
        # 이미지 픽셀 하나하나마다 gray 값으로 변경할꺼야
        for i in range(self.sid.width()):
            for j in range(self.sid.height()):
                # c는 (i,j)의 픽셀정보
                c = image.pixel(i, j)
                gray = qGray(c)
                alpha = qAlpha(c)
                image.setPixel(i, j, qRgba(gray, gray, gray, alpha))

        return image


    def openFileNameDialog(self):
        # 1번째 인수: 해당 파일의 경로를 읽음
        # 2번째 인수: 설명글
        # 3번째 인수: 파일 이름에 미리 적혀있어야 될 것이 있으면 적는다
        # 4번째 인수: 타입 지정
        # getOpenFileName() -> 경로, 타입 = fileName, _
        fileName, _ = QFileDialog.getOpenFileName(self, "불러올 이미지를 선택하세요.", "", "ALL Files (*);;Python Files (*.py)")

        # 파일이 없는데 입력되면 fileName가 0이되서 if 문 실행 X
        if fileName:
            print(fileName)
            self.sid = QImage(fileName).scaled(120, 120)

app = QApplication([])
ex = Example()
sys.exit(app.exec_())