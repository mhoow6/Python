# 시스템 쉘 스크립트 정보 가져와야하므로 import
import sys

# QtWidgets 안에 대부분의 위젯들이 있음
# 버튼을 가져오고 싶으면 버튼 가져오는 식으로
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

# Qwidget을 상속받아서 클래스를 만듬
class Exam(QWidget):
    # 생성자
    def __init__(self):
        # Qwidget 상위객체 생성
        super().__init__()
        self.initUI()
    def initUI(self):
        # 자신한테 버튼을 추가
        btn = QPushButton('눌러봐', self)

        # sizeHint는 글씨를 기준으로 크기를 조절해주는 메소드
        btn.resize(btn.sizeHint())

        # 왼쪽에서 20, 위쪽에서 30 옮김
        btn.move(20, 30)

        # 툴팁
        btn.setToolTip('툴팁입니다. <b>안녕하세요</b>')

        # 왼쪽에서부터 300, 위쪽에서 300 위치에서 창 생성
        # 크기 400x500
        self.setGeometry(300,300,400,500)
        
        self.setWindowTitle('첫 번째 학습시간')

        # 창 보여주기
        self.show()

# 모든 Qt5 어플리케이션은 QApplication 객체를 생성해야 한다
# 쉘 스크립트로 실행할 때 명령줄로 인수를 받을 수 있다.
# sys.argv는 그 부분을 제어하는 것이라고 보면 된다.
app = QApplication(sys.argv)

w = Exam()

# 프로그램 완전종료
# app.exec_는 Qwidget에게 이벤트 처리(넘겨주기)루프를 실행하기 위한 인수
# 이 코드는 메인 루프를 실행시킴
# 메인루프가 실행이 끝나면 sys.exit가 실행됨.
# 창을 종료한다든지 exit 함수를 실행한다든지해서 루프가 종료된다.
sys.exit(app.exec_())

# 설명
# 위젯창하고 일반창하고 다른 점은 메뉴(파일, 편집..)가 없다는 것