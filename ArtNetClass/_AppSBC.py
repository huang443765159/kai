import sys
sys.path.append('/home/pi/Desktop')
from PyQt5.QtWidgets import QMainWindow
from ArtNetClass._example.AppSBC.GuiSBC import GuiSBC
from ArtNetClass._example.AppSBC.UI.UI import Ui_MainWindow
from ArtNetClass.LedControl.SBC.LedControl import LedControlSBC


class AppSBC(QMainWindow):

    def __init__(self):
        super().__init__()
        # UI
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        # LED
        self._led = LedControlSBC(bot_id=1)
        # GUI
        self._gui = GuiSBC(ui=self._ui, led=self._led)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    sbc = AppSBC()
    sbc.show()
    sys.exit(app.exec_())
