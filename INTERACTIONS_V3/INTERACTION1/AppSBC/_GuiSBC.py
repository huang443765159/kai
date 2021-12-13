from INTERACTION1.SBC.OnePump import OnePump
from INTERACTION1.AppSBC.UI.UI import Ui_MainWindow
import INTERACTION1.Util.QTools as QTools


LIQUID_WATER_HIGH = 0
LIQUID_CH_A = 1
LIQUID_CH_B = 2
LIQUID_CH_WHL = 3
LIQUID_CH_WAX = 4


class GuiSBC(object):

    def __init__(self, ui: Ui_MainWindow, one_pump: OnePump, bot_id=1):
        self._ui = ui
        self._bot_id = bot_id
        self._one_pump = one_pump
        # UI: TABLE
        self._ui.table_liquids.verticalHeader().setFixedWidth(66)
        QTools.table_init(table=self._ui.table_liquids)
        for liquid_id in [0, 1, 2, 3, 4]:
            self._ui.table_liquids.item(liquid_id, 0).setText(f"{self._one_pump.get_liquid_ts_remain(liquid_id)}")
        # UI LED
        self._leds = {
            1: {0: self._ui.led_water_high,
                1: self._ui.led_ch_a,
                2: self._ui.led_ch_b,
                3: self._ui.led_ch_whl,
                4: self._ui.led_ch_wax},
            2: {0: self._ui.led_water_high,
                1: self._ui.led_ch_a,
                2: self._ui.led_ch_b,
                3: self._ui.led_ch_whl,
                4: self._ui.led_ch_wax}}
        # UI: SIGNAL
        self._one_pump.sign_tcp_online.connect(self._signal_tcp_online)
        self._one_pump.sign_sensor_level.connect(self._signal_one_liquid_level)
        self._one_pump.sign_pump_shooting.connect(self._signal_pump_shooting)
        self._one_pump.sign_pump_remain_ts.connect(self._signal_pump_remain_ts)
        # TEST_BTN
        self._ui.btn_stop_all.clicked.connect(self._stop_all)
        self._ui.btn_ch_whl.stateChanged.connect(lambda x: self._one_pump.set_liquid_shooting(3, x, 0))
        self._ui.btn_ch_a.stateChanged.connect(lambda x: self._one_pump.set_liquid_shooting(1, x, 0))
        self._ui.btn_ch_b.stateChanged.connect(lambda x: self._one_pump.set_liquid_shooting(2, x, 0))
        self._ui.btn_water.stateChanged.connect(lambda x: self._one_pump.set_liquid_shooting(0, x, 0))
        self._ui.btn_ch_wax.stateChanged.connect(lambda x: self._one_pump.set_liquid_shooting(4, x, 0))
        # TEST_TS_REMAIN_UPDATE

    def _signal_tcp_online(self, is_online, ip, port):
        QTools.set_led_style(ui_btn=self._ui.led_tcp_pump, color='GREEN' if is_online else 'RED')
        for liquid_id in [0, 1, 2, 3, 4]:
            QTools.set_led_style(ui_btn=self._leds[self._bot_id][liquid_id], color='GREEN' if is_online else 'RED')

    def _signal_one_liquid_level(self, bot_id, liquid_id, liquid_level):
        self._ui.table_liquids.item(liquid_id, 1).setText(f"{liquid_level}")

    def _signal_pump_shooting(self, bot_id, liquid_id, switch):
        QTools.set_led_style(self._leds[bot_id][liquid_id], color='DARK_GREEN' if switch else 'GREEN')

    def _signal_pump_remain_ts(self, bot_id, liquid_id, remain_ts):
        self._ui.table_liquids.item(liquid_id, 0).setText(f"{remain_ts}")

    def _stop_all(self):
        self._one_pump.stop_all()
        for liquid_id in [0, 1, 2, 3, 4]:
            QTools.set_led_style(ui_btn=self._leds[self._bot_id][liquid_id], color='GREEN')
            self._leds[self._bot_id][liquid_id].setChecked(0)  # 未启动

