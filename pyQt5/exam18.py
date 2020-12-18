import sys
from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar, QPushButton
from PyQt5.QtCore import QBasicTimer

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgessBar')
        self.show()

    # 타이머 실행 시
    def timerEvent(self, e) -> None:
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText("Finished")
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive(): # timer가 Active될 경우
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self) # interval: 100 -> 1000/100 초마다 한 번씩 타이머를 실행
            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())