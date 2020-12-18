# mySQL 재설치 후 다시 시도해보자

import sys, pymysql
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTreeView
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt

class sql(QWidget):
    def __init__(self):
        super().__init__()
        # self.sqlConnect()
        self.initUI()
        # self.run()

    def sqlConnect(self):
        try:
            # NO.1
            self.conn = pymysql.connect(
                # 서버 IP 혹은 도메인
                host='127.0.0.1',
                user='root',
                password='1234',
                db='root',
                port=3306,
                charset='utf8'
            )
        except:
            print("문제가 있네요!")
            exit(1)
        print("연결 성공!")

        # 접속을 한 후 쿼리를 입력하기 위해 커서의 위치를 받아온다.
        # cmd 커서라고 생각
        self.cur = self.conn.cursor() # NO.2

    def initUI(self):
        self.w = 400
        self.h = 420
        self.btnSize = 40

        # 번호, 이름, 주소
        self.lbl번호 = QLabel("번호", self)
        self.lbl번호.move(25, 25)
        self.txt번호 = QLineEdit(self)
        self.txt번호.move(25 + 49, 22)

        self.lbl이름 = QLabel("이름", self)
        self.lbl이름.move(25, 60)
        self.txt이름 = QLineEdit(self)
        self.txt이름.move(25 + 49, 60)

        self.lbl주소 = QLabel("주소", self)
        self.lbl주소.move(25, 95)
        self.txt주소 = QLineEdit(self)
        self.txt주소.move(25 + 49, 95)

        # 트리뷰
        # 특정 목록을 나열해주는 역할
        self.리스트 = QTreeView(self)
        self.리스트.setRootIsDecorated(False)

        # True 시 번호 칸의 내용이 중앙정렬 된다.
        # self.리스트.setRootIsDecorated(True)
        self.리스트.setAlternatingRowColors(True)
        self.리스트.resize(330, 200)
        self.리스트.move(25, 130)

        # 번호, 이름, 주소
        # 열의 갯수는 미리 지정한다.
        self.내용 = QStandardItemModel(0, 3, self)
        self.내용.setHeaderData(0, Qt.Horizontal, "번호")
        self.내용.setHeaderData(1, Qt.Horizontal, "이름")
        self.내용.setHeaderData(2, Qt.Horizontal, "주소")

        # 데이터 추가
        # 1행
        self.내용.insertRows(self.내용.rowCount(), 1)

        # 1행 내용 추가
        self.내용.setData(self.내용.index(0, 0), self.내용.rowCount())
        self.내용.setData(self.내용.index(0, 1), "홍길동")
        self.내용.setData(self.내용.index(0, 2), "인천시")

        # 2행 추가
        self.내용.insertRows(self.내용.rowCount(), 1)

        # 2행 내용 추가
        self.내용.setData(self.내용.index(1, 0), self.내용.rowCount())
        self.내용.setData(self.내용.index(1, 1), "장동건")
        self.내용.setData(self.내용.index(1, 2), "서울시")

        # self.내용을 self.리스트에
        self.리스트.setModel(self.내용)
        self.리스트.setColumnWidth(0, 40)
        self.리스트.setColumnWidth(1, 80)

        # 이전, 다음, 신규, 수정, 버튼
        self.cmd이전 = QPushButton("이전", self)
        self.cmd이전.resize(self.btnSize,self.btnSize)
        self.cmd다음 = QPushButton("다음", self)
        self.cmd다음.resize(self.btnSize, self.btnSize)
        self.cmd신규 = QPushButton("신규", self)
        self.cmd신규.resize(self.btnSize, self.btnSize)
        self.cmd수정 = QPushButton("수정", self)
        self.cmd수정.resize(self.btnSize, self.btnSize)
        self.cmd삭제 = QPushButton("삭제", self)
        self.cmd삭제.resize(self.btnSize, self.btnSize)

        self.setGeometry(300, 300, 500, 520)
        self.setWindowTitle("데이터 베이스 활용 예제")
        self.show()

    # 프로그램 종료시 호출
    # -> None = annotation return zero
    def closeEvent(self, QCloseEvent) -> None:
        print("close!")
        self.conn.close() # NO.3

    def run(self):
        # 쿼리문 입력
        self.cmd = "create table test(no int, name char)"

        # cmd의 내용을 커서 위치에 옮김
        self.cur.execute(self.cmd)

        # Enter
        self.conn.commit()

        # 현재 커서 위치에 있는 모든 값;all을 가져온다;fetch
        print(self.cur.fetchall())

    # 프로그램의 사이즈가 변경될 때 호출
    def resizeEvent(self, QResizeEvent) -> None:
        self.btnX = self.width() - 220
        self.btnY = self.height() - 60

        self.cmd이전.move(self.btnX, self.btnY)
        self.cmd다음.move(self.btnX+self.btnSize*1, self.btnY)
        self.cmd신규.move(self.btnX + self.btnSize * 2, self.btnY)
        self.cmd수정.move(self.btnX + self.btnSize * 3, self.btnY)
        self.cmd삭제.move(self.btnX + self.btnSize * 4, self.btnY)


if __name__ == '__main__':
    app = QApplication([])
    ex = sql()
    sys.exit(app.exec_())

