from PyQt5.QtWidgets import QMainWindow
from untitled import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_output.clicked.connect(self.setting)

    def setting(self):
        self.textBrowser.append('123')
        self.textBrowser.selectAll()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())