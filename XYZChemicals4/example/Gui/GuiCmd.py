from example.Gui.UI.UI import Ui_MainWindow
from example.Devices.Devices import Devices
from XYZChemicals4.Utils.CONST import CONST


class GuiCmd:

    def __init__(self, ui: Ui_MainWindow):
        self._ui = ui
        self._devices = Devices()
        self._chemicals = self._devices.chemicals
        self._sign = self._chemicals.sign
        # ITEMS
        self._btn = {CONST.DEVICES.M3: self._ui.btn_m3, CONST.DEVICES.ACID: self._ui.btn_acid,
                     CONST.DEVICES.WAX: self._ui.btn_wax, CONST.DEVICES.WHEELS: self._ui.btn_wheels}
        for chem_id, ui_btn in self._btn.items():
            ui_btn.clicked.connect(lambda ena, _chem_id=chem_id: self._set_channel_switch(ena=ena, chem_id=_chem_id))
        self._ui.btn_water.clicked.connect(self._set_pump_ena)
        self._ui.btn_stop_all.clicked.connect(self._get_one_side().stop_all)

    def _set_channel_switch(self, ena: bool, chem_id: int):
        one_side = self._get_one_side()
        one_side.set_channel_switch(chem_id=chem_id, ena=ena)

    def _set_pump_ena(self, ena: bool):
        one_side = self._get_one_side()
        one_side.set_water_pump_ena(ena=ena)

    def _get_one_side(self):
        return self._chemicals.get_one_side(bot_id=1 if self._ui.drv_bot1.isChecked() else 2)
