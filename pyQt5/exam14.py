import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
                             QColorDialog, QApplication)

from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20 , 20)
        self.btn.clicked.connect(self.showDialog)

        # 작은 검정 사각형이 프레임임
        self.frm = QFrame(self)

        # 16진수 색상값(#FFFFFF)이 %s안에 들어간다.
        # 그리고 그 값은 col 객체로 전달
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        # 컬러피커에서 얻은 색상값을 col에 저장
        # 색상값이 아닌 객체로 값을 받는다는 것에 주의
        col = QColorDialog.getColor()

        # OK를 누를 경우
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())