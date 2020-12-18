import sys

from PyQt5.QtWidgets import QMainWindow, QPushButton, QDesktopWidget, QApplication, QMessageBox, QMenu, QAction, qApp, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QCoreApplication, QPoint

class Toy(QMainWindow):
    def __init__(self):
        super(Toy, self).__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('서버 종료', self)
        btn.move(300, 250)
        btn.resize(btn.sizeHint())
        btn.setToolTip('<b>서버를 종료합니다.</b>')
        btn.clicked.connect(QCoreApplication.instance().quit)

        btn_start = QPushButton('서버 시작', self)
        btn_start.move(300, 220)
        btn_start.resize(btn.sizeHint())

        menu = self.menuBar()
        menu_file = menu.addMenu("파일")
        menu_view = menu.addMenu("보기")

        file_save = QAction('저장', self)
        file_save.setShortcut('Ctrl+S')
        file_save.setStatusTip("서버 설정을 저장합니다.")
        menu_file.addAction(file_save)

        new_txt = QAction("Example 01", self)
        new_py = QAction("Example 02", self)
        file_new = QMenu("서버 세팅", self)
        file_new.addAction(new_txt)
        file_new.addAction(new_py)
        menu_file.addMenu(file_new)

        view_stat = QAction("상태표시줄", self, checkable=True)
        view_stat.setChecked(True)
        view_stat.triggered.connect(self.tglStat)
        menu_view.addAction(view_stat)

        self.statusBar()
        self.statusBar().showMessage("오류 발생시 댓글로 남겨주세요!")
        # self.setGeometry(300, 300, 300, 150)
        self.setFixedSize(400, 300)
        self.center()
        self.setWindowTitle('ACC Server Manager')
        self.show()

    # https://gist.github.com/saleph/163d73e0933044d0e2c4
    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "종료 확인", "종료하시겠습니까?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def tglStat(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()

    def contextMenuEvent(self, QContextMenuEvent):
        cm = QMenu(self)
        quit = cm.addAction("Quit")
        action = cm.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        # action = cm.exec_(self.mapToGlobal(QPoint(0, 0)))

        if action == quit:
            qApp.quit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Toy()
    sys.exit(app.exec_())