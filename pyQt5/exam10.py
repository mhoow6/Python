import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        # self가 붙으면 해당 함수가 아니라 클래스에 변수를 생성합니다. 이렇게 하면, 다른 함수에서도 해당 변수에 접근할 수 있습니다.
        # self를 붙이지 않으면, 해당 함수가 종료되면 변수는 소멸됩니다.
        self.text = "x: {0}, y: {1}".format(x, y)
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True) # CPU 자원을 이용하게 되므로 평소엔 OFF

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event Object')
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = "x: {0}, y: {1}".format(x, y)
        self.label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
