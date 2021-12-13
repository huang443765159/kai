import os
from PyQt5.QtWidgets import QMainWindow
from XYZLedWall3.SBC.LedWall import LedWall
from example.AppSBC.GuiSBC import GuiSBC
from example.AppSBC.UI.UI import Ui_MainWindow


class AppSBC(QMainWindow):

    def __init__(self):
        super().__init__()
        # UI
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        # LED
        self._led = LedWall(bot_id=1, show_path=os.getcwd())
        # GUI
        self._gui = GuiSBC(ui=self._ui, led=self._led, bot_id=1)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    sbc = AppSBC()
    sbc.show()
    sys.exit(app.exec_())
