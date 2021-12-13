from PyQt5.QtWidgets import QMainWindow

from Example3.test.Gui.Gui import Gui
from Example3.test.Gui.UI.UI import Ui_MainWindow


class AppInstall(QMainWindow):

    def __init__(self):
        super(AppInstall, self).__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._gui = Gui(ui=self._ui)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    install = AppInstall()
    install.show()
    sys.exit(app.exec_())
