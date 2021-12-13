import sys
# sys.path.append('/home/pi/Desktop/XYZ-GUIDES')  # RASP 使用路径
import signal
from PyQt5.QtWidgets import QMainWindow
from example.AppSBC.UI.UI import Ui_MainWindow
from example.AppSBC._GuiSBC import GuiSBC
from XYZGuides.SBC.Guides import Guides

MACHINE_SN = 'TEST_1234'


class AppSBC(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # GUIDES
        self.guides = Guides(machine_sn=MACHINE_SN)
        # GUI
        self._gui = GuiSBC(ui=self, guides=self.guides)
        # SIGNAL
        signal.signal(signal.SIGINT, self.closeEvent)

    def closeEvent(self, event_signum=None, frame=None):
        self.guides.exit()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = AppSBC()
    window.show()
    sys.exit(app.exec_())
