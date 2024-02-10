import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QVBoxLayout, QWidget, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QPlainText 예제")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.text_edit = QPlainTextEdit()
        layout.addWidget(self.text_edit)

        self.clear_button = QPushButton("지우기")
        self.clear_button.clicked.connect(self.clear_text)
        layout.addWidget(self.clear_button)

    def clear_text(self):
        self.text_edit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
