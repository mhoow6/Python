import sys, pickle
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton

class App(QWidget):
    def __init__(self):
        super().__init__()
        # 클래스 영역에 사이즈를 지정하기 위해 self.
        self.size = 4
        self.initUI()

    def initUI(self):
        self.setWindowTitle('테이블 위젯')
        self.setGeometry(50, 50, 660, 240)

        # Table 생성
        self.createTable()
        self.btn = QPushButton('저장')
        self.btn.clicked.connect(on_cl)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.btn)

        self.setLayout(self.layout)
        self.show()

    def createTable(self):
        self.table = QTableWidget()

        # 행 지정
        self.table.setRowCount(self.size)

        # 열 지정
        self.table.setColumnCount(self.size)

        # 열의 갯수만큼 필드 label 지정
        self.table.setHorizontalHeaderLabels(('이름', '국어', '영어', '수학'))

        try:
            fp = open("out.txt", "rb") # out.txt를 읽기모드 (바이너리 모드 파일)
            for r in range(self.size):
                for c in range(self.size):

                    # 테이블의 아이템에 파일의 값을 차례대로 넣어줌
                    self.table.setItem(r, c, QTableWidgetItem(str(pickle.load(fp))))
            fp.close() # 파일 읽었으면 닫아야지

        # 예외 처리
        except:
            for r in range(self.size):
                for c in range(self.size):
                    self.table.setItem(r, c, QTableWidgetItem(""))

def on_cl():
    fp = open("out.txt", "wb") # 쓰기모드
    for r in range(ex.size):
        for c in range(ex.size):
            # 테이블의 각 셀을 돌며 셀의 텍스트 값을 fp(파일)로 쓴다
            # 바이너리 파일을 저장하기 위해 pickle 모듈을 사용
            pickle.dump(ex.table.item(r,c).text(), fp)
    fp.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())