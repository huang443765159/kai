from PyQt5.QtWidgets import QMainWindow

from Example2.Gui.UI.UI import Ui_MainWindow


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        # BTN


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    test = Example()
    test.show()
    sys.exit(app.exec_())
