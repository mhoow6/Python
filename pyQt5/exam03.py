import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 상태 표시줄 생성
        self.statusBar()
        
        # 상태 표시줄 객체를 받아오는 형태
        # 메뉴 설명등에 이용할 수 있다
        self.statusBar().showMessage("안녕하세요")

        # 메뉴 생성
        menu = self.menuBar()
        menu_file = menu.addMenu("File")
        menu_edit = menu.addMenu("Edit")

        # 액션
        file_exit = QAction('Exit', self)  # 메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip("누르면 영원히 bye")
        new_txt = QAction("텍스트 파일", self)
        new_py = QAction("파이썬 파일", self)

        file_exit.triggered.connect(QCoreApplication.instance().quit)

        # 서브 그룹
        file_new = QMenu('New', self)

        # 서브 메뉴 추가
        file_new.addAction(new_txt)
        file_new.addAction(new_py)

        # 파일 주 메뉴 추가
        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit) # 메뉴 등록
        
        self.resize(450, 400)
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())