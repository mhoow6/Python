from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
import sys

class Button(QPushButton):
    # 버튼은 초기화할때 2개가 필요함
    def __init__(self, title, parent):
        super().__init__(title, parent)

    # 버튼 위에서 마우스가 움직이고 있을때의 메소드
    def mouseMoveEvent(self, e):
        # 우클릭이 아니면 메소드 종료
        if e.buttons() != Qt.RightButton:
            return

        # 다양한 멀티미디어 데이터를 다루는 mimeData
        mimeData = QMimeData()

        # 버튼에 드래그 객체 생성
        drag = QDrag(self)

        # 드래그 객체가 건들 수 있는 데이터를 정함
        drag.setMimeData(mimeData)

        # 그(mimeDate) 객체를 활성화
        drag.exec_(Qt.MoveAction)

    # 매개변수 e는 메소드를 호출한 객체를 구분하기 위해 있다
    # 버튼이 여러개 있을 때 e로 버튼을 구분할 수 있다.
    def mousePressEvent(self, e):
        super().mousePressEvent(e)

        if e.button() == Qt.LeftButton:
            print('press')

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)

        self.show()

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)

        # 데이터가 이동하는 메소드는 반드시 허용여부를 줘야한다.
        e.accept()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()