from example.Gui.UI.UI import Ui_MainWindow
from example.Devices.Devices import Devices
from XYZChemicals4.Utils.CONST import CONST


class GuiSystem:

    def __init__(self, ui: Ui_MainWindow):
        self._ui = ui
        self._devices = Devices()
        self._chemicals = self._devices.chemicals
        self._sign = self._chemicals.sign
        # SYSTEM
        self._sign.cur_flow.connect(self._signal_cur_flow)
        self._sign.cur_level.connect(self._signal_cur_level)
        self._sign.cur_pressure.connect(self._signal_cur_pressure)
        self._sign.pump_ena.connect(self._signal_pump_ena)
        self._sign.channel_switch.connect(self._signal_channel_switch)
        self._ui.drv_bot1.clicked.connect(self._update)
        self._ui.drv_bot2.clicked.connect(self._update)
        # ITEMS
        self._btn = {CONST.DEVICES.M3: self._ui.btn_m3, CONST.DEVICES.ACID: self._ui.btn_acid,
                     CONST.DEVICES.WAX: self._ui.btn_wax, CONST.DEVICES.WHEELS: self._ui.btn_wheels}
        self._flows = {CONST.DEVICES.M3: self._ui.flow_m3, CONST.DEVICES.ACID: self._ui.flow_acid,
                       CONST.DEVICES.WAX: self._ui.flow_wax, CONST.DEVICES.WHEELS: self._ui.flow_wheels}
        self._levels = {CONST.DEVICES.M3: self._ui.level_m3, CONST.DEVICES.ACID: self._ui.level_acid,
                        CONST.DEVICES.WAX: self._ui.level_wax, CONST.DEVICES.WHEELS: self._ui.level_wheels}
        self._pressure = {CONST.DEVICES.M3: self._ui.press_m3, CONST.DEVICES.ACID: self._ui.press_acid,
                          CONST.DEVICES.WAX: self._ui.press_wax, CONST.DEVICES.WHEELS: self._ui.press_wheels}

    def _update(self):
        one_side = self._chemicals.get_one_side(bot_id=self._get_bot_id())
        # BTN
        for chem_id, ui_btn in self._btn.items():
            ena = one_side.get_channel_switch(chem_id=chem_id)
            ui_btn.blockSignals(True)
            ui_btn.setChecked(ena)
            ui_btn.blockSignals(False)
        pump_ena = one_side.get_water_pump_ena()
        self._ui.btn_water.blockSignals(True)
        self._ui.btn_water.setChecked(pump_ena)
        self._ui.btn_water.blockSignals(False)
        # FLOW
        for chem_id, ui_flow in self._flows.items():
            cur_flow = one_side.get_cur_flow(chem_id=chem_id)
            ui_flow.setValue(cur_flow)
        # LEVEL
        for chem_id, ui_level in self._levels.items():
            cur_level = one_side.get_cur_level(chem_id=chem_id)
            ui_level.setValue(cur_level / CONST.TANK.HEIGHT * 10)
        # PRESSURE
        for chem_id, ui_press in self._pressure.items():
            cur_press = one_side.get_cur_pressure(chem_id=chem_id)
            ui_press.setValue(cur_press)

    def _signal_pump_ena(self, bot_id: int, ena: bool):
        if bot_id == self._get_bot_id():
            self._ui.btn_water.blockSignals(True)
            self._ui.btn_water.setChecked(ena)
            self._ui.btn_water.blockSignals(False)

    def _signal_channel_switch(self, bot_id: int, chem_id: int, switch: bool):
        if bot_id == self._get_bot_id():
            self._btn.get(chem_id).blockSignals(True)
            self._btn.get(chem_id).setChecked(switch)
            self._btn.get(chem_id).blockSignals(False)

    def _signal_cur_flow(self, bot_id: int, chem_id: int, flow: float):
        if bot_id == self._get_bot_id():
            self._flows.get(chem_id).setValue(flow)

    def _signal_cur_level(self, bot_id: int, chem_id: int, level: int):
        if bot_id == self._get_bot_id():
            self._levels.get(chem_id).setValue(level)

    def _signal_cur_pressure(self, bot_id: int, chem_id: int, pressure: int):
        if bot_id == self._get_bot_id():
            self._pressure.get(chem_id).setValue(pressure)

    def _get_bot_id(self) -> int:
        return 1 if self._ui.drv_bot1.isChecked() else 2
