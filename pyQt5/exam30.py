# exit code -1073740791 (0xC0000409) 발생
# 같은 에러 코드가 난 경우를 stackoverflow에서 봤고, thread 문제라고 하는데
# 시간이 너무 걸릴 것 같으므로 패스하겠다.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.createReflectedImage()

    def initUI(self):
        # 이미지 객체 생성
        self.img = QImage("sonic.jpg")

        # 이미지 없으면 에러 메시지 출력 후 종료
        if self.img.isNull():
            print("Error loading image")
            sys.exit(1)

        # 이미지의 가로 세로 값 저장
        self.iw = self.img.width()
        self.ih = self.img.height()

        self.setGeometry(200, 200, 250, 450)
        self.setWindowTitle("Reflection")
        self.show()

    def createReflectedImage(self):
        # ARGB32로 설정하는 이유는 CompositionMode 설정하기 위함
        self.refImage = QImage(self.iw, self.ih, QImage.Format_ARGB32)

        painter = QPainter()
        painter.begin(self.refImage)
        # refImage 객체에 self.img 넣기
        painter.drawImage(0, 0, self.img)

        # CompositionMode_DestinationIn
        # 원본 이미지의 불투명도를 감소시킬 수 있는 모드 적용
        painter.setCompositionMode(QPainter.CompositionMode_DestinationIn)

        # QLinearGradient(시작 x, 시작 y, 끝 x, 끝 y)
        gradient = QLinearGradient(self.iw / 2, 0, self.iw / 2, self.ih)

        # setColorAt(위치, 색상)
        # 그라데이션의 정지점의 색상을 정의하는 메소드
        # 1 - 시작지점 0 - 종료지점
        gradient.setColorAt(1, QColor(0, 0, 0))
        gradient.setColorAt(0, Qt.transparent)

        painter.fillRect(0, 0, self.iw, self.ih, gradient)

        painter.end()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.draw(painter) # 이미지를 그리는 메소드 호출
        painter.end()

    def draw(self, painter):
        # 페인터의 좌표 0,0 -> +25, +15 이동 후 이미지 출력
        painter.drawImage(25, 15, self.img)

        # 페인터의 좌표 중심을 25,15에서 0, 2 * self.ih + 15로 변경
        painter.translate(0, 2 * self.ih + 15)

        # 좌표를 바꿔준다 y,x
        painter.scale(1, -1)

        # 페인터의 좌표 중심을 (0, 2 * self.ih + 15)5에서 (+25, +0) 이동 후 이미지 출력
        painter.drawImage(25, 0, self.refImage)

if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    sys.exit(app.exec_())