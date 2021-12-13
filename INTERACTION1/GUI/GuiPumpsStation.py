
class GuiInteraction(object):

    def __init__(self, ui, core):
        self._ui = ui
        self._core = core
        self._leds = self._ui.leds
        # SIGNAL
        self._core.pumps_station.sign_liquid_data.connect(self._liquid_data)
        self._core.pumps_station.sign_pumps_event.connect(self._pumps_event)
        self._core.pumps_station.sign_event.connect(self._interaction_event)
        self._core.pumps_station.sign_error.connect(self._interaction_error)
        # TEST BTN
        self._ui.btn_all_stop.stateChanged.connect(
            lambda: self._core.pumps_station.pumps_event(pump_type='ALL STOP', switch=False))
        self._ui.btn_high_water.stateChanged.connect(
            lambda x: self._core.pumps_station.pumps_event(pump_type='HIGH WATER', switch=x))
        self._ui.btn_wheel.stateChanged.connect(
            lambda x: self._core.pumps_station.pumps_event(pump_type='WHEEL', switch=x))
        self._ui.btn_alkali.stateChanged.connect(
            lambda x: self._core.pumps_station.pumps_event(pump_type='ALKALI CHEM', switch=x))
        self._ui.btn_acid.stateChanged.connect(
            lambda x: self._core.pumps_station.pumps_event(pump_type='ACID CHEM', switch=x))
        self._ui.btn_water_wax.stateChanged.connect(
            lambda x: self._core.pumps_station.pumps_event(pump_type='WATER WAX', switch=x))
        self._ui.btn_water_inflow.stateChanged.connect(
            lambda x: self._core.pumps_station.pumps_event(pump_type='WATER INFLOW', switch=x))

    def _liquid_data(self, liquid_data):
        self._ui.ui_water_data.setText(f"{liquid_data['WATER']}")
        self._ui.ui_alkali_data.setText(f"{liquid_data['ALKALI']}")
        self._ui.ui_acid_data.setText(f"{liquid_data['ACID']}")
        self._ui.ui_wheel_data.setText(f"{liquid_data['WHEEL']}")
        self._ui.ui_wax_data.setText(f"{liquid_data['WAX']}")
        for liquid_type in liquid_data.keys():
            if liquid_type == 'WATER':
                color = 'RED' if liquid_data[liquid_type] <= 100 else 'GREEN'
                text = 'WARNING' if liquid_data[liquid_type] <= 100 else ' '
                self._leds['WATER'].set_appearance(color=color, text=text)
                percent = liquid_data[liquid_type] / 900
                progress = 'background: QLinearGradient(x1:0, y1:0, x2:1, y2:0, '
                progress += f'stop: 0 rgb(200, 0, 0), stop: {percent:.2f} rgb(200, 0, 0), '
                progress += f'stop: {percent + 0.01:.2f} rgb(255, 255, 255), stop: 1 rgb(255, 255, 255));'
                progress += f'border: 0.1px solid #616161;'
                progress += f'border-width: 1px;'
                progress += f'border-color: rgb(97, 97, 97);'
                progress += f'border-radius: 2.5px;'
                self._leds[liquid_type].set_stylesheet(progress)
            else:
                color = 'RED' if liquid_data[liquid_type] <= 60 else 'GREEN'
                text = 'WARNING' if liquid_data[liquid_type] <= 60 else ' '
                self._leds[liquid_type].set_appearance(color=color, text=text)
                percent = liquid_data[liquid_type] / 250
                progress = 'background: QLinearGradient(x1:0, y1:0, x2:1, y2:0, '
                progress += f'stop: 0 rgb(200, 0, 0), stop: {percent:.2f} rgb(200, 0, 0), '
                progress += f'stop: {percent + 0.01:.2f} rgb(255, 255, 255), stop: 1 rgb(255, 255, 255));'
                progress += f'border: 0.1px solid #616161;'
                progress += f'border-width: 1px;'
                progress += f'border-color: rgb(97, 97, 97);'
                progress += f'border-radius: 2.5px;'
                self._leds[liquid_type].set_stylesheet(progress)

    def _pumps_event(self, pump_type, switch):
        self._ui.log_pumps_station.append(f'{pump_type} {switch}')

    def _interaction_event(self, event_type, code, value):
        if event_type == 'ANET_TCP':
            if code == 'CONNECT':
                print(code, value)
                is_connected, (client_ip, client_port) = value
                color = 'GREEN' if is_connected else 'RED'
                text = 'ON' if is_connected else 'OFF'
                self._leds['PUMPS STATION'].set_appearance(color, text=text)
                self._ui.ip_nuc.setText(f'NucIP : {client_ip}')
                self._ui.ip_local.setText(f'LocalIP : {self._core.pumps_station.get_my_ip()}')
        self._ui.log_network.append(f'[PUMPS STATION] {event_type} {code} {value}')

    def _interaction_error(self, error_type, code, error):
        self._ui.log_error.append(f'[PUMPS STATION] {error_type} {code} {error}')
