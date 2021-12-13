from INTERACTIONS.NUC.Pumps import Pumps
from INTERACTIONS.AppNUC.UI.UI import Ui_MainWindow
import INTERACTIONS.Util.QTools as QTools

LIQUID_WATER_HIGH = 0
LIQUID_CH_A = 1
LIQUID_CH_B = 2
LIQUID_CH_WHL = 3
LIQUID_CH_WAX = 4


class GuiPumps(object):

    def __init__(self, ui: Ui_MainWindow, pumps: Pumps):
        self._ui = ui
        self._pumps = pumps
        # TABLE
        self._ui.table_liquids.verticalHeader().setFixedWidth(66)
        QTools.table_init(table=self._ui.table_liquids)
        # UI: SIGNAL
        self._pumps.sign_pump_tcp_online.connect(self._tcp_online)
        self._pumps.sign_sensor_level.connect(self._signal_sensor_level)
        self._pumps.sign_pump_shooting.connect(self._signal_pump_shooting)
        self._pumps.sign_pump_remain_ts.connect(self._signal_pump_remain_ts)
        # UI LEDS
        self._leds = {
            1: {0: self._ui.led_water_high1,
                1: self._ui.led_ch_a1,
                2: self._ui.led_ch_b1,
                3: self._ui.led_ch_whl1,
                4: self._ui.led_ch_wax1},
            2: {0: self._ui.led_water_high2,
                1: self._ui.led_ch_a2,
                2: self._ui.led_ch_b2,
                3: self._ui.led_ch_whl2,
                4: self._ui.led_ch_wax2}}
        # UI: INIT
        self._ui.btn_ini_load.clicked.connect(self._pump_load_ini)
        self._ui.drv_bot1.clicked.connect(self._bot_id_changed)
        self._ui.drv_bot2.clicked.connect(self._bot_id_changed)
        self._ui.switch_link.stateChanged.connect(self._pumps.set_link)
        self._ui.engine_turbo.currentTextChanged.connect(lambda _t: self._pumps.set_turbo(turbo=int(_t[0])))
        # PUMP SWITCH
        self._ui.btn_stop_all.clicked.connect(self._stop_all)
        self._ui.btn_ch_whl.stateChanged.connect(lambda x: self._set_pump_shooting(3, x, 0))
        self._ui.btn_ch_a.stateChanged.connect(lambda x: self._set_pump_shooting(1, x, 0))
        self._ui.btn_ch_b.stateChanged.connect(lambda x: self._set_pump_shooting(2, x, 0))
        self._ui.btn_water.stateChanged.connect(lambda x: self._set_pump_shooting(0, x, 0))
        self._ui.btn_ch_wax.stateChanged.connect(lambda x: self._set_pump_shooting(4, x, 0))
        # UI_UPDATE
        self._bot_id_changed()

    def _signal_sensor_level(self, bot_id, sensor_id, sensor_level):
        if bot_id == 1 if self._ui.drv_bot1.isChecked() else 2:
            self._ui.table_liquids.item(sensor_id, 1).setText(f"{sensor_level}")

    def _signal_pump_shooting(self, bot_id, liquid_id, switch):
        QTools.set_led_style(ui_btn=self._leds[bot_id][liquid_id], color='DARK_GREEN' if switch else 'GREEN')

    def _signal_pump_remain_ts(self, bot_id, liquid_id, remain_ts, extra_ts):
        if bot_id == 1 if self._ui.drv_bot1.isChecked() else 2:
            self._ui.table_liquids.item(liquid_id, 0).setText(f"{remain_ts}")

    def _pump_tcp_error(self, bot_id, error_type, code, error):
        pass

    def _tcp_online(self, bot_id, is_online, ip, port):
        led_tcp_pump = self._ui.led_tcp_pump if bot_id == 1 else self._ui.led_tcp_pump2
        QTools.set_led_style(ui_btn=led_tcp_pump, color='GREEN' if is_online else 'RED')
        for liquid_id in [0, 1, 2, 3, 4]:
            QTools.set_led_style(ui_btn=self._leds[bot_id][liquid_id], color='GREEN' if is_online else 'RED')

    def _pump_load_ini(self):
        bot_id = 1 if self._ui.drv_bot1.isChecked() else 2
        self._pumps.load_pump_ini(bot_id=bot_id)

    def _bot_id_changed(self):
        bot_id = 1 if self._ui.drv_bot1.isChecked() else 2
        sensors_level = self._pumps.get_sensors_level(bot_id)
        for sensor_id, sensor_level in sensors_level.items():
            self._ui.table_liquids.item(sensor_id, 0).setText(f"{sensor_level}")
        for sensor_id in [0, 1, 2, 3, 4]:
            self._ui.table_liquids.item(sensor_id, 0).setText(f"{self._pumps.get_liquid_remain_ts(bot_id, sensor_id)}")

    def _set_pump_shooting(self, liquid_type, switch, ts_extra):
        bot_id = 1 if self._ui.drv_bot1.isChecked() else 2
        self._pumps.set_pump_shooting(bot_id, liquid_type, switch, ts_extra)

    def _stop_all(self):
        self._pumps.stop_all()
        for liquid_type in [0, 1, 2, 3, 4]:
            for bot_id in [1, 2]:
                QTools.set_led_style(ui_btn=self._leds[bot_id][liquid_type], color='GREEN')
                self._leds[bot_id][liquid_type].setChecked(0)
