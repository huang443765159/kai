
class GuiGuides(object):

    def __init__(self, ui, core):
        self._ui = ui
        self._core = core
        self._leds = self._ui.leds
        # SIGNAL
        self._core.guides.sign_data.connect(self._data)
        self._core.guides.sign_event.connect(self._event)
        self._core.guides.sign_error.connect(self._error)

    def _data(self, guides_data):
        print(guides_data)
        self._ui.ui_guides_data1.setText(f'{guides_data[0]}')
        self._ui.ui_guides_data2.setText(f'{guides_data[1]}')

    def _event(self, event_type, code, value):
        if event_type == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (server_ip, server_port) = value
                color = 'GREEN' if is_connected else 'RED'
                text = 'ON' if is_connected else 'OFF'
                self._leds['GUIDES'].set_appearance(color=color, text=text)
                self._ui.ip_nuc.setText(f'NucIP : {server_ip}')
                self._ui.ip_local.setText(f'LocalIP : {self._core.guides.get_my_ip()}')
        self._ui.log_network.append(f'[GUIDES] {event_type}, {code}, {value}')

    def _error(self, error_type, code, error):
        self._ui.log_error.append(f'[GUIDES] {error_type} {code} {error}')
