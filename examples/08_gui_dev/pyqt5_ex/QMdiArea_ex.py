import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QMdiArea, QMdiSubWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MDI 예제")
        self.setGeometry(100, 100, 800, 600)

        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        self.create_actions()
        self.create_menus()

    def create_actions(self):
        self.new_action = QAction("새 문서", self)
        self.new_action.triggered.connect(self.create_new_document)

        self.exit_action = QAction("종료", self)
        self.exit_action.triggered.connect(self.close)

    def create_menus(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("파일")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.exit_action)

    def create_new_document(self):
        sub_window = QMdiSubWindow()
        sub_window.setWindowTitle("새 문서")
        text_edit = QTextEdit()
        sub_window.setWidget(text_edit)
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
