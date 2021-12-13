import signal
from PyQt5.QtWidgets import QMainWindow
from example.AppNUC.UI.UI import Ui_MainWindow
from example.AppNUC._GuiNUC import GuiNUC
from XYZGuides.NUC.Guides import Guides

MACHINE_SN = 'TEST_1234'


class AppSBC(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        # GUIDES
        self._guides = Guides(machine_sn=MACHINE_SN)
        # GUI
        self._gui = GuiNUC(ui=self._ui, guides=self._guides)
        # SIGNAL
        signal.signal(signal.SIGINT, self.closeEvent)

    def closeEvent(self, event_signum=None, frame=None):
        self._guides.exit()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = AppSBC()
    window.show()
    sys.exit(app.exec_())
