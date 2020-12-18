import sys

from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)

class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)

        # 버튼 자체에 드래그 기능 활성화
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):

        # 일반적인 텍스트가 올 경우 이벤트 허용
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):

        # 드래그 했던 텍스트를 내 버튼 자체의 텍스트로 설정
        self.setText(e.mimeData().text())


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 300, 150)


def main():

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()