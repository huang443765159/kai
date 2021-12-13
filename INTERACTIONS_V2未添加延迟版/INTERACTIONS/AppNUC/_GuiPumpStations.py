from INTERACTIONS.NUC.PumpStations import PumpStations
from INTERACTIONS.AppNUC.UI.UI import Ui_MainWindow
import INTERACTIONS.Util.QTools as QTools


class GuiPumpStations(object):

    def __init__(self, ui: Ui_MainWindow, pump_stations: PumpStations):
        self._ui = ui
        self._pump_stations = pump_stations
        # UI: SIGNAL
        self._pump_stations.sign_drain_raw_data.connect(self._drain_raw_data)
        self._pump_stations.sign_liquid_raw_data.connect(self._liquid_raw_data)
        self._pump_stations.sign_pump_instruction.connect(self._pump_instruction)
        self._pump_stations.sign_pump_tcp_error.connect(self._pump_tcp_error)
        self._pump_stations.sign_pump_tcp_online.connect(self._pump_tcp_online)
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
        # UI: TEST BTN
        # PUMP1
        self._ui.btn_all_stop.stateChanged.connect(
            lambda x: self._pump_stations[1].pump_instruction(pump_instruct='ALL STOP', is_open=False))
        self._ui.btn_high_water.stateChanged.connect(
            lambda x: self._pump_stations[1].pump_instruction(pump_instruct='HIGH WATER', is_open=x))
        self._ui.btn_wheel.stateChanged.connect(
            lambda x: self._pump_stations[1].pump_instruction(pump_instruct='WHEEL', is_open=x))
        self._ui.btn_alkali.stateChanged.connect(
            lambda x: self._pump_stations[1].pump_instruction(pump_instruct='ALKALI CHEM', is_open=x))
        self._ui.btn_acid.stateChanged.connect(
            lambda x: self._pump_stations[1].pump_instruction(pump_instruct='ACID CHEM', is_open=x))
        self._ui.btn_water_wax.stateChanged.connect(
            lambda x: self._pump_stations[1].pump_instruction(pump_instruct='WATER WAX', is_open=x))
        self._ui.btn_water_inflow.stateChanged.connect(
            lambda x: self._pump_stations[1].pump_instruction(pump_instruct='WATER INFLOW', is_open=x))
        # PUMP2
        self._ui.btn_all_stop.stateChanged.connect(
            lambda x: self._pump_stations[2].pump_instruction(pump_instruct='ALL STOP', is_open=False))
        self._ui.btn_high_water.stateChanged.connect(
            lambda x: self._pump_stations[2].pump_instruction(pump_instruct='HIGH WATER', is_open=x))
        self._ui.btn_wheel.stateChanged.connect(
            lambda x: self._pump_stations[2].pump_instruction(pump_instruct='WHEEL', is_open=x))
        self._ui.btn_alkali.stateChanged.connect(
            lambda x: self._pump_stations[2].pump_instruction(pump_instruct='ALKALI CHEM', is_open=x))
        self._ui.btn_acid.stateChanged.connect(
            lambda x: self._pump_stations[2].pump_instruction(pump_instruct='ACID CHEM', is_open=x))
        self._ui.btn_water_wax.stateChanged.connect(
            lambda x: self._pump_stations[2].pump_instruction(pump_instruct='WATER WAX', is_open=x))
        self._ui.btn_water_inflow.stateChanged.connect(
            lambda x: self._pump_stations[2].pump_instruction(pump_instruct='WATER INFLOW', is_open=x))
        self._ui.btn_drain.stateChanged.connect(
            lambda x: self._pump_stations[2].pump_instruction(pump_instruct='DRAIN', is_open=x))
        # UI: INIT
        self._ui.ip_local.setText(f'LOCAL_IP {self._pump_stations[2].get_my_ip()}')

    def _drain_raw_data(self, drain_raw_data):
        self._ui.ui_drain_data1.setText(f'{drain_raw_data[0]}')
        self._ui.ui_drain_data2.setText(f'{drain_raw_data[1]}')

    def _liquid_raw_data(self, device_id, liquid_raw_data):
        if device_id == 1:
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
            QTools.set_led_style(ui_btn=self._leds[liquid_type + str(device_id)], color=color)
            self._leds[liquid_type + str(device_id)].setText(text)
            percent = liquid_raw_data[liquid_type] / container_height
            progress = QTools.set_style_sheet(percent=percent)
            self._leds[liquid_type + str(device_id)].setStyleSheet(progress)

    def _pump_instruction(self, device_id, pump_instruct, is_open):
        station = self._ui.log_pump_station1 if device_id == 1 else self._ui.log_pump_station2
        station.append(f'{pump_instruct} {is_open}')

    def _pump_tcp_error(self, device_id, error_type, code, error):
        self._ui.log_error.append(f'[PUMP STATION]{device_id} {error_type} {code} {error}')

    def _pump_tcp_online(self, device_id, is_online, ip, port):
        QTools.set_led_style(ui_btn=self._leds['PUMP STATION' + str(device_id)], color='GREEN' if is_online else 'RED')
        self._leds['PUMP STATION' + str(device_id)].setText('ON' if is_online else 'OFF')
        nuc_ip = self._ui.ip_nuc1 if device_id == 1 else self._ui.ip_nuc2
        nuc_ip.setText(f'NUC_IP {ip}')
        self._ui.log_network.append(f'{ip} {port}')
