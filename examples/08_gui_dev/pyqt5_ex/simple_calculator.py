import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('사칙연산 계산기')
        self.layout = QVBoxLayout()

        # 입력 필드
        self.firstNumber = QLineEdit(self)
        self.secondNumber = QLineEdit(self)
        self.result = QLineEdit(self)
        self.result.setReadOnly(True)  # 결과 필드는 읽기 전용

        # 버튼
        self.addButton = QPushButton('+', self)
        self.subtractButton = QPushButton('-', self)
        self.multiplyButton = QPushButton('*', self)
        self.divideButton = QPushButton('/', self)

        # 버튼 이벤트 연결
        self.addButton.clicked.connect(self.add)
        self.subtractButton.clicked.connect(self.subtract)
        self.multiplyButton.clicked.connect(self.multiply)
        self.divideButton.clicked.connect(self.divide)

        # 레이아웃 구성
        self.layout.addWidget(QLabel('숫자 1:'))
        self.layout.addWidget(self.firstNumber)
        self.layout.addWidget(QLabel('숫자 2:'))
        self.layout.addWidget(self.secondNumber)
        self.layout.addWidget(QLabel('결과:'))
        self.layout.addWidget(self.result)

        # 연산 버튼 레이아웃
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.addButton)
        self.buttonLayout.addWidget(self.subtractButton)
        self.buttonLayout.addWidget(self.multiplyButton)
        self.buttonLayout.addWidget(self.divideButton)

        self.layout.addLayout(self.buttonLayout)
        self.setLayout(self.layout)

    def add(self):
        result = float(self.firstNumber.text()) + float(self.secondNumber.text())
        self.result.setText(str(result))

    def subtract(self):
        result = float(self.firstNumber.text()) - float(self.secondNumber.text())
        self.result.setText(str(result))

    def multiply(self):
        result = float(self.firstNumber.text()) * float(self.secondNumber.text())
        self.result.setText(str(result))

    def divide(self):
        second_num = float(self.secondNumber.text())
        if second_num != 0:
            result = float(self.firstNumber.text()) / second_num
            self.result.setText(str(result))
        else:
            self.result.setText('오류: 0으로 나눌 수 없습니다.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
