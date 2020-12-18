import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        # grid.addWidget(reviewEdit, 3, 1, 5, 1)
        # grid.addWidget(reviewEdit, 3, 1, 5, 1)할 경우 review 라벨이 위로 달라 붙는 이유:
        # grid.addWidget(element, 행, 열, 행범위, 열범위 [,정렬]) 에서 행범위, 열범위를 입력하지 않았을 때의 기본값은 1줄이므로 범위를 정확히 3행, 1열만 차지함. 여기서 textEdit의 기본적인 세로 길이 때문에 행 크기 자체가 늘어남. grid는 자동 좌우 상하 중간 정렬되므로 중간 정렬 됨.
        # 그런데 행범위를 5, 열범위를 1 입력할 경우, 3행에서 7행까지, 1열에서 1열까지 범위를 확보하고 그 안에 element를 넣게 됨.
        # 여기서 review label은 grid.addWidget(review, 3, 0)으로 형성되어 기본 3행 0열만 차지하여 1줄만 차지하므로 5줄을 차지하는 reviewEdit에 비해 위에 붙는 것처럼 보이게 됨.
        grid.addWidget(reviewEdit, 3, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())