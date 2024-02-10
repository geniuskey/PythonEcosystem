import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QSplitter, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSplitter 예제")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        splitter = QSplitter()
        layout.addWidget(splitter)

        left_edit = QTextEdit()
        right_edit = QTextEdit()

        splitter.addWidget(left_edit)
        splitter.addWidget(right_edit)
        splitter.setSizes([200, 400])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
