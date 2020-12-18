from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("redrock.png")

        lbl = QLabel(self)

        # 레이블에 pixmap 객체를 넣음
        # 글씨 대신 이미지를 넣었다
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())