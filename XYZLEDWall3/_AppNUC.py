import os
from PyQt5.QtCore import QObject
from XYZNetwork3.MixInviter import MixInviter
from XYZLedWall3.NUC.LedWall import LedWall
from XYZLedWall3.Utils.CONST import CONST
from example.AppNUC.GuiNUC import GuiNUC
from example.AppNUC.UI.UI import Ui_MainWindow


class AppNUC(QObject):

    def __init__(self):
        super().__init__()
        # UI
        self._ui = Ui_MainWindow()
        # LED
        self._led = LedWall(show_path=os.getcwd())
        # INVITER
        self._inviter = MixInviter()
        self._led.link_inviter(inviter=self._inviter)
        self._inviter.set_machine_sn(machine_sn=CONST.TEST.MACHINE_SN)
        # GUI
        self._gui = GuiNUC(ui=self._ui, led=self._led)
        self._gui.show()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    nuc = AppNUC()
    sys.exit(app.exec_())
