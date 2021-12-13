
class GuiPumpsStation(object):

    def __init__(self, ui, core):
        self._ui = ui
        self._core = core
        self._leds = self._ui.leds
        # SIGNAL
        self._core.pumps_station[2].sign_drain_data.connect(self._drain_data)
        for device_id in [1, 2]:
            self._core.pumps_station[device_id].sign_liquid_data.connect(self._liquid_data)
            self._core.pumps_station[device_id].sign_pumps_event.connect(self._pumps_event)
            self._core.pumps_station[device_id].sign_event.connect(self._pumps_network_event)
            self._core.pumps_station[device_id].sign_error.connect(self._pumps_network_error)
        # # INTERACTION1
        self._ui.btn_all_stop.stateChanged.connect(
            lambda x: self._core.pumps_station[1].pumps_event(pump_type='ALL STOP', switch=False))
        self._ui.btn_high_water.stateChanged.connect(
            lambda x: self._core.pumps_station[1].pumps_event(pump_type='HIGH WATER', switch=x))
        self._ui.btn_wheel.stateChanged.connect(
            lambda x: self._core.pumps_station[1].pumps_event(pump_type='WHEEL', switch=x))
        self._ui.btn_alkali.stateChanged.connect(
            lambda x: self._core.pumps_station[1].pumps_event(pump_type='ALKALI CHEM', switch=x))
        self._ui.btn_acid.stateChanged.connect(
            lambda x: self._core.pumps_station[1].pumps_event(pump_type='ACID CHEM', switch=x))
        self._ui.btn_water_wax.stateChanged.connect(
            lambda x: self._core.pumps_station[1].pumps_event(pump_type='WATER WAX', switch=x))
        self._ui.btn_water_inflow.stateChanged.connect(
            lambda x: self._core.pumps_station[1].pumps_event(pump_type='WATER INFLOW', switch=x))
        # INTERACTION2
        self._ui.btn_all_stop.stateChanged.connect(
            lambda x: self._core.pumps_station[2].pumps_event(pump_type='ALL STOP', switch=False))
        self._ui.btn_high_water.stateChanged.connect(
            lambda x: self._core.pumps_station[2].pumps_event(pump_type='HIGH WATER', switch=x))
        self._ui.btn_wheel.stateChanged.connect(
            lambda x: self._core.pumps_station[2].pumps_event(pump_type='WHEEL', switch=x))
        self._ui.btn_alkali.stateChanged.connect(
            lambda x: self._core.pumps_station[2].pumps_event(pump_type='ALKALI CHEM', switch=x))
        self._ui.btn_acid.stateChanged.connect(
            lambda x: self._core.pumps_station[2].pumps_event(pump_type='ACID CHEM', switch=x))
        self._ui.btn_water_wax.stateChanged.connect(
            lambda x: self._core.pumps_station[2].pumps_event(pump_type='WATER WAX', switch=x))
        self._ui.btn_water_inflow.stateChanged.connect(
            lambda x: self._core.pumps_station[2].pumps_event(pump_type='WATER INFLOW', switch=x))
        self._ui.btn_drain.stateChanged.connect(
            lambda x: self._core.pumps_station[2].pumps_event(pump_type='DRAIN', switch=x))

    def function_creator(self, device_id, p_type):
        def func(x):
            self._core.pumps_station[device_id].pumps_event(pump_type=p_type, switch=x)
        return func

    def _drain_data(self, drain_data):
        print(drain_data)
        self._ui.ui_drain_data1.setText(f'{drain_data[0]}')
        self._ui.ui_drain_data2.setText(f'{drain_data[1]}')

    def _liquid_data(self, device_id, liquid_data):
        if device_id == 1:
            self._ui.ui_water_data1.setText(f"{liquid_data['WATER']}")
            self._ui.ui_alkali_data1.setText(f"{liquid_data['ALKALI']}")
            self._ui.ui_acid_data1.setText(f"{liquid_data['ACID']}")
            self._ui.ui_wheel_data1.setText(f"{liquid_data['WHEEL']}")
            self._ui.ui_wax_data1.setText(f"{liquid_data['WAX']}")
        else:
            self._ui.ui_water_data2.setText(f"{liquid_data['WATER']}")
            self._ui.ui_alkali_data2.setText(f"{liquid_data['ALKALI']}")
            self._ui.ui_acid_data2.setText(f"{liquid_data['ACID']}")
            self._ui.ui_wheel_data2.setText(f"{liquid_data['WHEEL']}")
            self._ui.ui_wax_data2.setText(f"{liquid_data['WAX']}")
        for liquid_type in liquid_data.keys():
            if liquid_type == 'WATER':
                color = 'RED' if liquid_data[liquid_type] <= 100 else 'GREEN'
                text = 'WARNING' if liquid_data[liquid_type] <= 100 else ' '
                self._leds['WATER2'].set_appearance(color=color, text=text)
                percent = liquid_data[liquid_type] / 900
                progress = 'background: QLinearGradient(x1:0, y1:0, x2:1, y2:0, '
                progress += f'stop: 0 rgb(200, 0, 0), stop: {percent:.2f} rgb(200, 0, 0), '
                progress += f'stop: {percent + 0.01:.2f} rgb(64, 64, 64), stop: 1 rgb(64, 64, 64));'
                progress += f'border: 0.1px solid #616161;'
                progress += f'border-width: 1px;'
                progress += f'border-color: rgb(97, 97, 97);'
                progress += f'border-radius: 2.5px;'
                self._leds[liquid_type + str(device_id)].set_stylesheet(progress)
            else:
                color = 'RED' if liquid_data[liquid_type] <= 60 else 'GREEN'
                text = 'WARNING' if liquid_data[liquid_type] <= 60 else ' '
                self._leds[liquid_type + str(device_id)].set_appearance(color=color, text=text)
                percent = liquid_data[liquid_type] / 250
                progress = 'background: QLinearGradient(x1:0, y1:0, x2:1, y2:0, '
                progress += f'stop: 0 rgb(200, 0, 0), stop: {percent:.2f} rgb(200, 0, 0), '
                progress += f'stop: {percent + 0.01:.2f} rgb(64, 64, 64), stop: 1 rgb(64, 64, 64));'
                progress += f'border: 0.1px solid #616161;'
                progress += f'border-width: 1px;'
                progress += f'border-color: rgb(97, 97, 97);'
                progress += f'border-radius: 2.5px;'
                self._leds[liquid_type + str(device_id)].set_stylesheet(progress)

    def _pumps_event(self, device_id, pump_type, switch):
        station = self._ui.log_pumps_station1 if device_id == 1 else self._ui.log_pumps_station2
        station.append(f'{pump_type} {switch}')

    def _pumps_network_event(self, device_id, event_type, code, value):
        if event_type == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (server_ip, server_port) = value
                color = 'GREEN' if is_connected else 'RED'
                text = 'ON' if is_connected else 'OFF'
                self._leds['PUMPS STATION' + str(device_id)].set_appearance(color=color, text=text)
        self._ui.log_network.append(f'[PUMPS STATION]{device_id} {event_type} {code} {value}')

    def _pumps_network_error(self, device_id, error_type, code, error):
        self._ui.log_error.append(f'[PUMPS STATION]{device_id} {error_type} {code} {error}')
