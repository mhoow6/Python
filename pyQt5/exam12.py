import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

# pyqtSignal을 쓰기 위해 QObject 클래스를 상속받음
# pyqtSignal은 신호방출이 가능한 객체
class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()

        # closeApp에 close라는 슬롯을 연결
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit Signal')
        self.show()

    # closeApp과 연결되있는 슬롯이 있는데
    # emit은 closeApp에 충격?을 주는거라고 보면 됨
    def mousePressEvent(self, event):
        self.c.closeApp.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# emit 설명
# 1. 마우스 클릭
# 2. mousePressEvent 발생
# 3. closeApp 객체의 신호가 방출 (emit)
# 4. clossApp과 연결된(connect) self.close 실행행