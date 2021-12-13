from INTERACTIONS.NUC.PumpStations import PumpStations
from INTERACTIONS.AppNUC.UI.UI import Ui_MainWindow
import INTERACTIONS.Util.QTools as QTools
import INTERACTIONS.XYZAutoNet.Tool as ANETools


class GuiPumpStations(object):

    def __init__(self, ui: Ui_MainWindow, pump_stations: PumpStations):
        self._ui = ui
        self._pump_stations = pump_stations
        # UI: SIGNAL
        self._pump_stations.sign_drain_raw_data.connect(self._drain_raw_data)
        self._pump_stations.sign_liquid_raw_data.connect(self._liquid_raw_data)
        self._pump_stations.sign_pump_emit.connect(self._pump_is_open)
        self._pump_stations.sign_pump_tcp_online.connect(self._pump_tcp_online)
        self._pump_stations.sign_pump_countdown.connect(self._pump_countdown)
        # UI: LED
        self._leds = dict()
        self._leds['PUMP STATION1'] = self._ui.led_pump_station1
        self._leds['WATER1'] = self._ui.led_water1
        self._leds['ALKALI1'] = self._ui.led_alkali1
        self._leds['ACID1'] = self._ui.led_acid1
        self._leds['WHEEL1'] = self._ui.led_wheel1
        self._leds['WAX1'] = self._ui.led_wax1
        self._leds['PUMP STATION2'] = self._ui.led_pump_station2
        self._leds['WATER2'] = self._ui.led_water2
        self._leds['ALKALI2'] = self._ui.led_alkali2
        self._leds['ACID2'] = self._ui.led_acid2
        self._leds['WHEEL2'] = self._ui.led_wheel2
        self._leds['WAX2'] = self._ui.led_wax2
        # PUMP LED
        self._leds['WATER_HIGH1'] = self._ui.led_pump_1
        self._leds['WATER_HIGH2'] = self._ui.led_pump_2
        self._leds['WHEEL1'] = self._ui.led_ch1_wheel
        self._leds['WHEEL2'] = self._ui.led_ch2_wheel
        self._leds['CHEM_ALKALI1'] = self._ui.led_ch1_alkali
        self._leds['CHEM_ALKALI2'] = self._ui.led_ch2_alkali
        self._leds['CHEM_ACID1'] = self._ui.led_ch1_acid
        self._leds['CHEM_ACID2'] = self._ui.led_ch2_acid
        self._leds['WATER_WAX1'] = self._ui.led_ch1_wax
        self._leds['WATER_WAX2'] = self._ui.led_ch2_wax
        # UI: INIT
        self._ui.drv_bot1.clicked.connect(self._bot_id_changed)
        self._ui.drv_bot2.clicked.connect(self._bot_id_changed)
        self._ui.switch_link.stateChanged.connect(self._pump_stations.set_link)
        self._ui.engine_turbo.currentTextChanged.connect(lambda _t: self._pump_stations.set_turbo(turbo=int(_t[0])))
        self._bot_id_changed()
        self._ui.ip_local.setText(f'LOCAL_IP: {ANETools.get_my_ip()}')
        # PUMP SWITCH
        self._ui.btn_all_stop.stateChanged.connect(lambda x: self._set_stop_all(is_open=x, t_wait=0))
        self._ui.btn_wheel.stateChanged.connect(lambda x: self._set_wheel_emit(is_open=x, t_wait=0))
        self._ui.btn_alkali.stateChanged.connect(lambda x: self._set_chem_alkali_emit(is_open=x, t_wait=0))
        self._ui.btn_acid.stateChanged.connect(lambda x: self._set_chem_acid_emit(is_open=x, t_wait=0))
        self._ui.btn_water_wax.stateChanged.connect(lambda x: self._set_water_wax_emit(is_open=x, t_wait=0))
        self._ui.btn_high_water.stateChanged.connect(lambda x: self._set_water_high_emit(is_open=x, t_wait=0))
        self._ui.btn_drain.stateChanged.connect(lambda x: self._set_drain_emit(is_open=x, t_wait=0))
        self._ui.btn_water_inflow.stateChanged.connect(lambda x: self._set_water_inflow_emit(is_open=x, t_wait=0))

    def _drain_raw_data(self, drain_raw_data):
        self._ui.ui_drain_data1.setText(f'{drain_raw_data[0]}')
        self._ui.ui_drain_data2.setText(f'{drain_raw_data[1]}')

    def _liquid_raw_data(self, pump_id, liquid_raw_data):
        if pump_id == 1:
            self._ui.ui_water_data1.setText(f"{liquid_raw_data['WATER']}")
            self._ui.ui_alkali_data1.setText(f"{liquid_raw_data['ALKALI']}")
            self._ui.ui_acid_data1.setText(f"{liquid_raw_data['ACID']}")
            self._ui.ui_wheel_data1.setText(f"{liquid_raw_data['WHEEL']}")
            self._ui.ui_wax_data1.setText(f"{liquid_raw_data['WAX']}")
        else:
            self._ui.ui_water_data2.setText(f"{liquid_raw_data['WATER']}")
            self._ui.ui_alkali_data2.setText(f"{liquid_raw_data['ALKALI']}")
            self._ui.ui_acid_data2.setText(f"{liquid_raw_data['ACID']}")
            self._ui.ui_wheel_data2.setText(f"{liquid_raw_data['WHEEL']}")
            self._ui.ui_wax_data2.setText(f"{liquid_raw_data['WAX']}")
        for liquid_type in liquid_raw_data.keys():
            liquid_height = 100 if liquid_type == 'WATER' else 60
            container_height = 900 if liquid_type == 'WATER' else 250
            color = 'RED' if liquid_raw_data[liquid_type] <= liquid_height else 'GREEN'
            text = 'WARNING' if liquid_raw_data[liquid_type] <= liquid_height else ' '
            QTools.set_led_style(ui_btn=self._leds[liquid_type + str(pump_id)], color=color)
            self._leds[liquid_type + str(pump_id)].setText(text)
            percent = liquid_raw_data[liquid_type] / container_height
            progress = QTools.set_style_sheet(percent=percent)
            self._leds[liquid_type + str(pump_id)].setStyleSheet(progress)

    def _pump_is_open(self, pump_id, instruct, is_open):
        station = self._ui.ui_log_pump1 if pump_id == 1 else self._ui.ui_log_pump2
        station.setText(f'{instruct} {is_open}')
        if instruct in ['WATER_HIGH', 'CHEM_ALKALI', 'CHEM_ACID', 'WHEEL', 'WATER_WAX']:
            QTools.set_led_style(ui_btn=self._leds[instruct + str(pump_id)], color='GREEN' if is_open else 'RED')
        elif instruct == 'ALL STOP':
            for instruct in ['WATER_HIGH', 'CHEM_ALKALI', 'CHEM_ACID', 'WHEEL', 'WATER_WAX']:
                QTools.set_led_style(ui_btn=self._leds[instruct + str(pump_id)], color='RED')

    def _pump_tcp_error(self, pump_id, error_type, code, error):
        pass

    def _pump_countdown(self, pump_id, instruct, countdown):
        log = self._ui.ui_log_countdown_pump1 if pump_id == 1 else self._ui.ui_log_countdown_pump2
        box = self._ui.pump1_countdown_box1 if pump_id == 1 else self._ui.pump2_countdown_box2
        log.setText(f'{instruct}')
        box.setValue(int(countdown))

    def _pump_tcp_online(self, pump_id, is_online, ip, port):
        QTools.set_led_style(ui_btn=self._leds['PUMP STATION' + str(pump_id)], color='GREEN' if is_online else 'RED')
        self._leds['PUMP STATION' + str(pump_id)].setText('ON' if is_online else 'OFF')
        nuc_ip = self._ui.ip_nuc1 if pump_id == 1 else self._ui.ip_nuc2
        nuc_ip.setText(f'NUC_IP {ip}')

    def _bot_id_changed(self):
        bot_id = 1 if self._ui.drv_bot1.isChecked() else 2
        return bot_id

    def _set_stop_all(self, is_open, t_wait):
        bot_id = self._bot_id_changed()
        if is_open:
            self._pump_stations.set_stop_all(bot_id=bot_id, is_open=False, t_wait=t_wait)

    def _set_water_high_emit(self, is_open, t_wait):
        bot_id = self._bot_id_changed()
        self._pump_stations.set_water_high_emit(bot_id=bot_id, is_open=is_open, t_wait=t_wait)

    def _set_chem_alkali_emit(self, is_open, t_wait):
        bot_id = self._bot_id_changed()
        self._pump_stations.set_chem_alkali_emit(bot_id=bot_id, is_open=is_open, t_wait=t_wait)

    def _set_chem_acid_emit(self, is_open, t_wait):
        bot_id = self._bot_id_changed()
        self._pump_stations.set_chem_acid_emit(bot_id=bot_id, is_open=is_open, t_wait=t_wait)

    def _set_wheel_emit(self, is_open, t_wait):
        bot_id = self._bot_id_changed()
        self._pump_stations.set_wheel_emit(bot_id=bot_id, is_open=is_open, t_wait=t_wait)

    def _set_water_wax_emit(self, is_open, t_wait):
        bot_id = self._bot_id_changed()
        self._pump_stations.set_water_wax_emit(bot_id=bot_id, is_open=is_open, t_wait=t_wait)

    def _set_drain_emit(self, is_open, t_wait):
        bot_id = self._bot_id_changed()
        if bot_id == 2:
            self._pump_stations.set_drain_emit(bot_id=bot_id, is_open=is_open, t_wait=t_wait)

    def _set_water_inflow_emit(self, is_open, t_wait):
        bot_id = self._bot_id_changed()
        self._pump_stations.set_water_inflow_emit(bot_id=bot_id, is_open=is_open, t_wait=t_wait)
