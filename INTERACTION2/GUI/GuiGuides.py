
class GuiGuides(object):

    def __init__(self, ui, core):
        self._ui = ui
        self._core = core
        self._leds = self._ui.leds
        # SIGNAL
        self._core.guides.sign_data.connect(self._guides_data)
        self._core.guides.sign_event.connect(self._guides_event)
        self._core.guides.sign_error.connect(self._guides_error)
        self._core.guides.display.sign_display_show.connect(self._display_show)
        # DISPLAY BTN
        self._ui.btn_display_start.clicked.connect(self._core.guides.display.display_start)
        self._ui.btn_display_stop.clicked.connect(self._core.guides.display.display_stop)
        self._ui.btn_display_next.clicked.connect(self._core.guides.display.display_next)
        self._ui.btn_display_last.clicked.connect(self._core.guides.display.display_last)

    def _guides_data(self, guides_data):
        self._ui.ui_guides_data1.setText(f'{guides_data[0]}')
        self._ui.ui_guides_data2.setText(f'{guides_data[1]}')

    def _guides_event(self, event_type, code, value):
        if event_type == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (client_ip, client_port) = value
                color = 'GREEN' if is_connected else 'RED'
                text = 'ON' if is_connected else 'OFF'
                self._core.guides.display.start()
                self._leds['GUIDES'].set_appearance(color=color, text=text)
        self._ui.log_network.append(f'[GUIDES] {event_type} {code} {value}')

    def _guides_error(self, error_type, code, error):
        self._ui.log_error.append(f'[GUIDES ERROR] {error_type} {code} {error}')

    def _display_show(self, display_show):
        self._ui.ui_display_type.setText(display_show)
