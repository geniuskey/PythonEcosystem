"""
필요 패키지 설치
> pip install pyqt5 PyQtWebEngine jupyter notebook
"""
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class MainWindow(QMainWindow):
    def __init__(self, notebook_url):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(notebook_url))
        self.setCentralWidget(self.browser)
        self.showMaximized()

    def closeEvent(self, event):
        # 어플리케이션 종료 시 Jupyter Notebook 서버도 함께 종료합니다.
        self.notebook_process.terminate()
        event.accept()

def main():
    # Jupyter Notebook 서버를 백그라운드에서 시작합니다.
    notebook_process = subprocess.Popen(["jupyter", "notebook", "--NotebookApp.token=''"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    app = QApplication(sys.argv)
    notebook_url = "http://localhost:8888"
    window = MainWindow(notebook_url)
    window.notebook_process = notebook_process
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
