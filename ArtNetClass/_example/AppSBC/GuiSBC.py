from ArtNetClass.Utils.CONST import CONST
from ArtNetClass._example.AppSBC.UI.UI import Ui_MainWindow
from ArtNetClass.LedControl.SBC.LedControl import LedControlSBC


class GuiSBC(object):

    def __init__(self, ui: Ui_MainWindow, led: LedControlSBC):
        self._ui = ui
        self._led = led
        # UI
        self._ui.btn_r.clicked.connect(self._set_r)
        self._ui.btn_g.clicked.connect(self._set_g)
        self._ui.btn_b.clicked.connect(self._set_b)
        self._ui.btn_color.clicked.connect(self._set_color)
        self._ui.btn_blink.stateChanged.connect(self._set_blink)

    def _set_r(self):
        if not self._ui.btn_all.isChecked():
            cid = self._ui.channel.value()
            self._led[cid].set_r(r=100)
        else:
            for cid in CONST.ART_NET.UNIVERSES.keys():
                self._led[cid].set_r(r=100)

    def _set_g(self):
        if not self._ui.btn_all.isChecked():
            cid = self._ui.channel.value()
            self._led[cid].set_g(g=100)
        else:
            for cid in CONST.ART_NET.UNIVERSES.keys():
                self._led[cid].set_g(g=100)

    def _set_b(self):
        if not self._ui.btn_all.isChecked():
            cid = self._ui.channel.value()
            self._led[cid].set_b(b=100)
        else:
            for cid in CONST.ART_NET.UNIVERSES.keys():
                self._led[cid].set_b(b=100)

    def _set_color(self):
        if not self._ui.btn_all.isChecked():
            cid = self._ui.channel.value()
            self._led[cid].set_colorful()
        else:
            for cid in CONST.ART_NET.UNIVERSES.keys():
                self._led[cid].set_colorful()

    def _set_blink(self, ena):
        if not self._ui.btn_all.isChecked():
            cid = self._ui.channel.value()
            self._led[cid].set_blink() if ena else self._led[cid].stop()
        else:
            for cid in CONST.ART_NET.UNIVERSES.keys():
                self._led[cid].set_blink() if ena else self._led[cid].stop()
