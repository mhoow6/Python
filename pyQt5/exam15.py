import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                             QSizePolicy, QLabel, QFontDialog, QApplication)

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)

        # 사이즈 고정?
        btn.setSizePolicy(QSizePolicy.Fixed,
                          QSizePolicy.Fixed)

        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):
        # getFont에서 font 값이랑
        # ok를 눌렀지에 대한 값을 나눠서 받는다
        # font에는 글씨체, 사이즈 등 여러 정보가 들어가있다
        font, ok = QFontDialog.getFont()

        # 예외처리
        if ok:
            self.lbl.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())