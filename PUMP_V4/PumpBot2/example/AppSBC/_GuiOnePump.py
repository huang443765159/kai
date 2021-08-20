from PumpBot2.SBC.OnePump.OnePump import OnePump
from PumpBot2.example.AppSBC.UI.UI import Ui_MainWindow
import PumpBot2.example.Util.QTools as QTools
from PumpBot2.Util.DEFINES import CHANNEL as CH


class GuiOnePump(object):

    def __init__(self, ui: Ui_MainWindow, one_pump: OnePump, bot_id=2):
        self._ui = ui
        self._bot_id = bot_id
        self._one_pump = one_pump
        # UI: SIGNAL
        self._one_pump.sign_tcp_online.connect(self._signal_tcp_online)
        self._one_pump.sign_channel_ena.connect(self._signal_pump_state)
        # UI: LED
        self._led = {
            1: {CH.WATER: self._ui.led_water_high,
                CH.CH_A: self._ui.led_ch_a,
                CH.CH_B: self._ui.led_ch_b,
                CH.CH_WHL: self._ui.led_ch_whl,
                CH.CH_WAX: self._ui.led_ch_wax},
            2: {CH.WATER: self._ui.led_water_high,
                CH.CH_A: self._ui.led_ch_a,
                CH.CH_B: self._ui.led_ch_b,
                CH.CH_WHL: self._ui.led_ch_whl,
                CH.CH_WAX: self._ui.led_ch_wax}}
        for ui_led in list(self._led[bot_id].values()):
            QTools.set_led_style(ui_btn=ui_led, color='RED')
        QTools.set_led_style(ui_btn=self._ui.led_tcp_pump, color='RED')
        self._btn = {
            CH.WATER: self._ui.btn_water,
            CH.CH_A: self._ui.btn_ch_a,
            CH.CH_B: self._ui.btn_ch_b,
            CH.CH_WHL: self._ui.btn_ch_whl,
            CH.CH_WAX: self._ui.btn_ch_wax}
        # TEST_BTN
        self._ui.btn_stop_all.clicked.connect(self._stop_all)
        self._ui.btn_ch_whl.stateChanged.connect(lambda x: self._one_pump.set_pump_ena(3, x))
        self._ui.btn_ch_a.stateChanged.connect(lambda x: self._one_pump.set_pump_ena(1, x))
        self._ui.btn_ch_b.stateChanged.connect(lambda x: self._one_pump.set_pump_ena(2, x))
        self._ui.btn_water.stateChanged.connect(lambda x: self._one_pump.set_pump_ena(0, x))
        self._ui.btn_ch_wax.stateChanged.connect(lambda x: self._one_pump.set_pump_ena(4, x))

    def _signal_tcp_online(self, is_online, ip, port):
        QTools.set_led_style(ui_btn=self._ui.led_tcp_pump, color='GREEN' if is_online else 'RED')

    def _signal_pump_state(self, bot_id, cid, ena):
        QTools.set_led_style(self._led[bot_id][cid], color='GREEN' if ena else 'RED')
        self._btn[cid].setChecked(2 if ena else 0)

    def _stop_all(self):
        self._one_pump.stop_all()
        for liquid_id in [0, 1, 2, 3, 4]:
            QTools.set_led_style(ui_btn=self._led[self._bot_id][liquid_id], color='RED')
            self._btn[liquid_id].setChecked(0)
