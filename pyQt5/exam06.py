import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # 리스트 생성
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        # 리스트 생성
        positions = [(i, j) for i in range(5) for j in range(4)]

        # 두 개의 리스트를 하나의 투플로 묶어줌
        # 빈칸을 제외하고는
        # 버튼을 생성해주고 그리드 위치에 맞게 추가
        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            # position (0,3) -> *position 0,3
            grid.addWidget(button, *position)

            # 확인용
            # print("{0} -> {1}".format(position, name))

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())