import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QLineEdit')
        self.show()

    # textChanged[str]이 text에 들어간다.
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize() # 글씨 사이즈 자동 조정


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()