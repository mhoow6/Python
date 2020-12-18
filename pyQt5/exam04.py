import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, qApp
from PyQt5.QtCore import QCoreApplication


class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 상태 표시줄 생성
        self.statusBar()
        self.statusBar().showMessage("안녕하세요")

        # 메뉴 생성
        menu = self.menuBar() # 메뉴바 생성
        menu_file = menu.addMenu("File") # 그룹 생성
        menu_edit = menu.addMenu("Edit") # 그룹 생성
        menu_view = menu.addMenu("View") # 그룹 생성

        # 액션
        file_exit = QAction('Exit', self)  # 메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip("누르면 영원히 bye")
        new_txt = QAction("텍스트 파일", self)
        new_py = QAction("파이썬 파일", self)
        view_stat = QAction('상태표시줄', self, checkable = True)
        view_stat.setChecked(True) # 기본적으로 체크

        # file_exit.triggered.connect(qApp.quit) 도 가능
        # quit()으로 안 쓰는 이유는 괄호안에 메소드 "명"을 넘겨줘야하기 때문에 quit() -> quit
        file_exit.triggered.connect(QCoreApplication.instance().quit)
        view_stat.triggered.connect(self.tglStat)

        # 서브 그룹
        file_new = QMenu('New', self)

        # 서브 메뉴 추가
        file_new.addAction(new_txt)
        file_new.addAction(new_py)
        menu_view.addAction(view_stat) # view라는 그룹에 view_stat 액션 추가

        # 파일 주 메뉴 추가
        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit)  # 메뉴 등록

        self.resize(450, 400)
        self.show()
    def tglStat(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()

    def contextMenuEvent(self, QContextMenuEvent):
        cm = QMenu(self)

        quit = cm.addAction("Quit")

        # 메뉴 실행 정보를 저장하는 exec_()에 전체적인 맵의 위치를 저장해서 넘김
        action = cm.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        if action == quit:
            # QCoreApplication.instance().quit과 동일
            qApp.quit()
app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())