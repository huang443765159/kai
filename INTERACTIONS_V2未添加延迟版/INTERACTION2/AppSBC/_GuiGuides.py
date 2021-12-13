from INTERACTION2.SBC.Guides import Guides
from INTERACTION2.AppSBC.UI.UI import Ui_SBC
import INTERACTION2.Util.QTools as QTools

STAGES = {0x10: '欢迎光临', 0x11: '向前行驶', 0x12: '停止行驶', 0x13: '向后行驶', 0x14: '正在清洗', 0x15: '清洗结束'}


class GuiGuides(object):

    def __init__(self, ui: Ui_SBC, guides: Guides):
        self._ui = ui
        self._guides = guides
        # UI: SIGNAL
        self._guides.sign_raw_data.connect(self._raw_data)
        self._guides.sign_stage_changed.connect(self._stage_show)
        self._guides.sign_tcp_error.connect(self._tcp_error)
        self._guides.sign_tcp_online.connect(self._tcp_online)
        # UI: INIT
        self._ui.ip_local.setText(f'LOCAL_IP {self._guides.get_my_ip()}')
        # BTN
        self._ui.btn_welcome.clicked.connect(lambda: self._guides.set_stage_id_for_test(0x10))
        self._ui.btn_stop_forward.clicked.connect(lambda: self._guides.set_stage_id_for_test(0x12))
        self._ui.btn_back_driving.clicked.connect(lambda: self._guides.set_stage_id_for_test(0x13))
        self._ui.btn_forward.clicked.connect(lambda: self._guides.set_stage_id_for_test(0x11))
        self._ui.btn_washing.clicked.connect(lambda: self._guides.set_stage_id_for_test(0x14))
        self._ui.btn_washing_end.clicked.connect(lambda: self._guides.set_stage_id_for_test(0x15))

    def _raw_data(self, raw_data):
        self._ui.ui_guides_data1.setText(f'{raw_data[0]}')
        self._ui.ui_guides_data2.setText(f'{raw_data[1]}')

    def _stage_show(self, stage_id):
        self._ui.ui_stage_show.setText(f'{STAGES[stage_id]}')

    def _tcp_error(self, error_type, code, error):
        self._ui.log_error.append(f'{error_type} {code} {error}')

    def _tcp_online(self, is_connected, peer_ip, peer_port):
        QTools.set_led_style(ui_btn=self._ui.led_guides, color='GREEN' if is_connected else 'RED')
        self._ui.led_guides.setText('ON' if is_connected else 'OFF')
        self._ui.ip_nuc.setText(f'NUC_IP {peer_ip}')
        self._ui.log_network.append(f'NUC_IP {peer_ip} {peer_port}')

