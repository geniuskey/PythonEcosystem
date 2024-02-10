import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("간단한 계산기")
        # self.setGeometry(100, 100, 300, 250)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        layout.addWidget(self.result_display)

        buttons_layout = QGridLayout()
        layout.addLayout(buttons_layout)

        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("AC", 3, 0), ("0", 3, 1), ("=", 3, 2), ("+", 3, 3)
        ]

        self.buttons_dict = {}
        for text, row, col in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            buttons_layout.addWidget(button, row, col)
            self.buttons_dict[button] = text

        self.current_number: str = ""
        self.current_operation = None
        self.previous_number: int = 0
        self.reset()

    def reset(self):
        self.current_number = ""
        self.current_operation = None
        self.previous_number: int = 0
        self.result_display.setText("0")

    def button_click(self):
        button = self.sender()
        text = self.buttons_dict[button]

        if text.isdigit() or text == ".":
            self.current_number += text
            self.result_display.setText(self.current_number)
        elif text in ["+", "-", "*", "/"]:
            if self.current_number:
                self.previous_number = int(self.current_number)
                self.current_number = ""
                self.current_operation = text
        elif text == "=":
            if self.current_number and self.current_operation:
                if self.current_operation == "+":
                    result = self.previous_number + int(self.current_number)
                elif self.current_operation == "-":
                    result = self.previous_number - int(self.current_number)
                elif self.current_operation == "*":
                    result = self.previous_number * int(self.current_number)
                elif self.current_operation == "/":
                    if int(self.current_number) != 0:
                        result = self.previous_number / int(self.current_number)
                    else:
                        result = "Error: Division by zero"
                self.result_display.setText(str(result))
                self.current_number = ""
                self.previous_number = result

        elif text == "AC":
            self.reset()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
