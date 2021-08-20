from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow


class NewWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_ok.clicked.connect(self._btn_clicked)

    @staticmethod
    def _btn_clicked():
        print('hello world')


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = NewWindow()
    window.show()

    sys.exit(app.exec_())
