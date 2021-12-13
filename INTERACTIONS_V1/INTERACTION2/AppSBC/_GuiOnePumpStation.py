from INTERACTION2.SBC.OnePumpStation import OnePumpStation
from INTERACTION2.AppSBC.UI.UI import Ui_SBC
import INTERACTION2.Util.QTools as QTools


class GuiOnePumpStation(object):
    def __init__(self, ui: Ui_SBC, one_pump_station: OnePumpStation):
        self._ui = ui
        self._one_pump_station = one_pump_station
        # UI: LEDS
        self._leds = dict()
        self._leds['PUMP STATION'] = self._ui.led_pump_station
        self._leds['WATER'] = self._ui.led_water
        self._leds['ALKALI'] = self._ui.led_alkali
        self._leds['ACID'] = self._ui.led_acid
        self._leds['WHEEL'] = self._ui.led_wheel
        self._leds['WAX'] = self._ui.led_wax
        # UI: PUMP
        self._leds['WATER_HIGH'] = self._ui.led_high_water
        self._leds['WHEEL'] = self._ui.led_ch1_wheel
        self._leds['CHEM_ALKALI'] = self._ui.led_ch_alkali
        self._leds['CHEM_ACID'] = self._ui.led_ch_acid
        self._leds['WATER_WAX'] = self._ui.led_ch1_wax
        # UI: SIGNAL
        self._one_pump_station.sign_tcp_online.connect(self._tcp_online)
        self._one_pump_station.sign_drain_raw_data.connect(self._drain_raw_data)
        self._one_pump_station.sign_liquid_raw_data.connect(self._liquid_raw_data)
        self._one_pump_station.sign_pump_emit.connect(self._pump_emit)
        self._one_pump_station.sign_pump_countdown.connect(self._pump_countdown)
        # UI: INIT
        self._ui.ip_local.setText(f'LOCAL_IP:{self._one_pump_station.get_my_ip()}')
        # TEST BTN
        self._ui.btn_all_stop.stateChanged.connect(lambda x: self._one_pump_station.stop_all(is_open=False, t_wait=0))
        self._ui.btn_high_water.stateChanged.connect(lambda x: self._one_pump_station.set_water_high_emit(
            is_open=x, t_wait=0))
        self._ui.btn_wheel.stateChanged.connect(lambda x: self._one_pump_station.set_wheel_emit(
            is_open=x, t_wait=0))
        self._ui.btn_alkali.stateChanged.connect(lambda x: self._one_pump_station.set_chem_alkali_emit(
            is_open=x, t_wait=0))
        self._ui.btn_acid.stateChanged.connect(lambda x: self._one_pump_station.set_chem_acid_emit(
            is_open=x, t_wait=0))
        self._ui.btn_water_wax.stateChanged.connect(lambda x: self._one_pump_station.set_water_wax_emit(
            is_open=x, t_wait=0))
        self._ui.btn_water_inflow.stateChanged.connect(lambda x: self._one_pump_station.set_water_inflow_emit(
            is_open=x, t_wait=0))
        self._ui.btn_drain.stateChanged.connect(lambda x: self._one_pump_station.set_drain_emit(
            is_open=x, t_wait=0))

    def _drain_raw_data(self, pump_id, drain_raw_data):
        self._ui.ui_drain_data1.setText(f'{drain_raw_data[0]}')
        self._ui.ui_drain_data2.setText(f'{drain_raw_data[1]}')

    def _liquid_raw_data(self, pump_id, liquid_raw_data):
        self._ui.ui_water_data.setText(f"{liquid_raw_data['WATER']}")
        self._ui.ui_alkali_data.setText(f"{liquid_raw_data['ALKALI']}")
        self._ui.ui_acid_data.setText(f"{liquid_raw_data['ACID']}")
        self._ui.ui_wheel_data.setText(f"{liquid_raw_data['WHEEL']}")
        self._ui.ui_wax_data.setText(f"{liquid_raw_data['WAX']}")
        for liquid_type in liquid_raw_data.keys():
            liquid_height = 100 if liquid_type == 'WATER' else 60
            container_height = 900 if liquid_type == 'WATER' else 250
            color = 'RED' if liquid_raw_data[liquid_type] <= liquid_height else 'GREEN'
            text = 'WARNING' if liquid_raw_data[liquid_type] <= liquid_height else ' '
            QTools.set_led_style(ui_btn=self._leds[liquid_type], color=color)
            self._leds[liquid_type].setText(text)
            percent = liquid_raw_data[liquid_type] / container_height
            progress = QTools.set_style_sheet(percent=percent)
            self._leds[liquid_type].setStyleSheet(progress)

    def _pump_countdown(self, pump_id, instruct, countdown):
        self._ui.ui_log_pump_countdown.setText(f'{pump_id} {instruct}')
        self._ui.pump_countdown_box.setValue(int(countdown))

    def _pump_emit(self, bot_id, instruct, is_open):
        self._ui.ui_log_pump.setText(f'{bot_id} {instruct} {is_open}')
        if instruct in ['WATER_HIGH', 'CHEM_ALKALI', 'CHEM_ACID', 'WHEEL', 'WATER_WAX']:
            QTools.set_led_style(ui_btn=self._leds[instruct], color='GREEN' if is_open else 'RED')
        elif instruct == 'ALL STOP':
            for instruct in ['WATER_HIGH', 'CHEM_ALKALI', 'CHEM_ACID', 'WHEEL', 'WATER_WAX']:
                QTools.set_led_style(ui_btn=self._leds[instruct + str(bot_id)], color='RED')

    def _tcp_online(self, is_online, ip, port):
        QTools.set_led_style(ui_btn=self._ui.led_pump_station, color='GREEN' if is_online else 'RED')
        self._ui.led_pump_station.setText('ON' if is_online else 'OFF')
        self._ui.ip_nuc.setText(f'NUC_IP {ip}')
