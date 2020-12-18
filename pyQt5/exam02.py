import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication

class Exam(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('눌러봐', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # 버튼을 클릭했을 때 시그널 발생
        # 클릭했을 때 수행하는 슬롯을 연결시킴
        # 슬롯이란 코드를 의미함
        # QCoreApplication에 있는 객체를 불러온다음
        # 그 안의 메소드인 quit()를 부른다
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.show()

    # override; 월래 메소드를 같은 이름으로 재정의함
    # X 버튼 눌렀을 때의 메소드
    def closeEvent(self, QCloseEvent):
        # 질문 형태의 메시지 박스
        # 제목, 메시지, 버튼종류, 기본값
        ans = QMessageBox.question(self, "종료 확인", "종료하시겠습니까?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if ans == QMessageBox.Yes:
            # QCloseEvent 발생을 승인
            QCloseEvent.accept()
        else:
            # 무시
            QCloseEvent.ignore()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())
