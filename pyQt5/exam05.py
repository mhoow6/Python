import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)

# QHBoxLayout
# --> 가로 방향으로 쌓임

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK") # OK 버튼 생성
        cancelButton = QPushButton("Cancel") # Cancel 버튼 생성

        hbox = QHBoxLayout() # 가로로 쌓을 수 있는 레이아웃 생성
        hbox.addStretch(1) # 버튼 2개가 차지하지 않고 있는 공간만큼 빈 공간 생성
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Exam()
    sys.exit(app.exec_())