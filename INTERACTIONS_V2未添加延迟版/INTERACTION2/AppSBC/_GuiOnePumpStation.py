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
        # UI: SIGNAL
        self._one_pump_station.sign_tcp_online.connect(self._tcp_online)
        self._one_pump_station.sign_tcp_error.connect(self._tcp_error)
        self._one_pump_station.sign_drain_raw_data.connect(self._drain_raw_data)
        self._one_pump_station.sign_liquid_raw_data.connect(self._liquid_raw_data)
        self._one_pump_station.sign_pump_instruction.connect(self._pump_instruction)
        # UI: INIT
        self._ui.ip_local.setText(f'LOCAL_IP:{self._one_pump_station.get_my_ip()}')
        # TEST BTN
        self._ui.btn_all_stop.stateChanged.connect(lambda x: self._one_pump_station.pump_instruction(
            pump_instruct='ALL STOP', is_open=False))
        self._ui.btn_high_water.stateChanged.connect(lambda x: self._one_pump_station.pump_instruction(
            pump_instruct='HIGH WATER', is_open=x))
        self._ui.btn_wheel.stateChanged.connect(lambda x: self._one_pump_station.pump_instruction(
            pump_instruct='WHEEL', is_open=x))
        self._ui.btn_alkali.stateChanged.connect(lambda x: self._one_pump_station.pump_instruction(
            pump_instruct='ALKALI CHEM', is_open=x))
        self._ui.btn_acid.stateChanged.connect(lambda x: self._one_pump_station.pump_instruction(
            pump_instruct='ACID CHEM', is_open=x))
        self._ui.btn_water_wax.stateChanged.connect(lambda x: self._one_pump_station.pump_instruction(
            pump_instruct='WATER WAX', is_open=x))
        self._ui.btn_water_inflow.stateChanged.connect(lambda x: self._one_pump_station.pump_instruction(
            pump_instruct='WATER INFLOW', is_open=x))
        self._ui.btn_drain.stateChanged.connect(lambda x: self._one_pump_station.pump_instruction(
            pump_instruct='DRAIN', is_open=x))

    def _drain_raw_data(self, drain_raw_data):
        self._ui.ui_drain_data1.setText(f'{drain_raw_data[0]}')
        self._ui.ui_drain_data2.setText(f'{drain_raw_data[1]}')

    def _liquid_raw_data(self, liquid_raw_data):
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

    def _pump_instruction(self, pump_instruct, is_open):
        self._ui.log_pump_station.append(f'{pump_instruct} {is_open}')

    def _tcp_online(self, is_online, ip, port):
        QTools.set_led_style(ui_btn=self._ui.led_pump_station, color='GREEN' if is_online else 'RED')
        self._ui.led_pump_station.setText('ON' if is_online else 'OFF')
        self._ui.ip_nuc.setText(f'NUC_IP {ip}')
        self._ui.log_network.append(f'{ip} {port}')

    def _tcp_error(self, error_type, code, error):
        self._ui.log_error.append(f'{error_type} {code} {error}')
