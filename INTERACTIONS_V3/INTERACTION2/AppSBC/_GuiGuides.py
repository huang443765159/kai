from INTERACTION2.SBC.Guides import Guides
from INTERACTION2.AppSBC.UI.UI import Ui_MainWindow
import INTERACTION2.Util.QTools as QTools

STAGES = {0x10: '欢迎光临', 0x11: '向前行驶', 0x12: '停止行驶', 0x13: '向后行驶', 0x14: '正在清洗', 0x15: '清洗结束'}


class GuiGuides(object):

    def __init__(self, ui: Ui_MainWindow, guides: Guides):
        self._ui = ui
        self._guides = guides
        # UI: SIGNAL
        self._guides.sign_raw_data.connect(self._raw_data)
        self._guides.sign_stage_changed.connect(self._stage_show)
        self._guides.sign_tcp_error.connect(self._tcp_error)
        self._guides.sign_tcp_online.connect(self._tcp_online)

    def _raw_data(self, raw_data):
        QTools.set_led_style(ui_btn=self._ui.led_guides_data1, color='GREEN' if raw_data[0] else 'RED')
        QTools.set_led_style(ui_btn=self._ui.led_guides_data2, color='GREEN' if raw_data[1] else 'RED')

    def _stage_show(self, stage_id):
        self._ui.guides_show.setText(f'{STAGES[stage_id]}')

    def _tcp_error(self, error_type, code, error):
        pass

    def _tcp_online(self, is_connected, peer_ip, peer_port):
        QTools.set_led_style(ui_btn=self._ui.led_tcp_guides, color='GREEN' if is_connected else 'RED')

