from XYZLedWall3.Utils.CONST import CONST
from XYZLedWall3.SBC.LedWall import LedWall
from XYZLedWall3.Utils.Signal import SIGNAL
from example.AppSBC.UI.UI import Ui_MainWindow
import example.Utils.QTools as QTools


class GuiSBC(object):

    def __init__(self, ui:Ui_MainWindow, led: LedWall, bot_id: int):
        self._ui = ui
        self._led = led
        self._bot_id = bot_id
        # SIGNAL
        SIGNAL.sign_is_online.connect(self._is_online)
        # BTN
        self._ui.btn_r.clicked.connect(self._set_r)
        self._ui.btn_g.clicked.connect(self._set_g)
        self._ui.btn_b.clicked.connect(self._set_b)
        self._ui.btn_colorful.clicked.connect(self._set_colorful)
        # IMG/VIDEO
        self._ui.btn_img.clicked.connect(self._read_img)
        self._ui.btn_video.clicked.connect(self._read_video)

    def _is_online(self, bot_id, is_online, ip, port):
        QTools.set_led_style(ui_btn=self._ui.led_bot1,
                             color=[0, CONST.SHOW.COLOR[CONST.SHOW.G], 0] if is_online else [CONST.SHOW.COLOR[CONST.SHOW.R], 0, 0])

    def _set_r(self):
        self._led.set_r()

    def _set_g(self):
        self._led.set_g()

    def _set_b(self):
        self._led.set_b()

    def _set_colorful(self):
        self._led.set_colorful()

    def _read_img(self):
        img_id = self._ui.show.value()
        if img_id in [CONST.SHOW.WELCOME, CONST.SHOW.THANKS]:
            self._led.rgb.read_img(img_id=img_id, bot_id=self._bot_id)

    def _read_video(self):
        video_id = self._ui.show.value()
        if video_id in [CONST.SHOW.SEA, CONST.SHOW.SKY]:
            self._led.rgb.read_video(video_id=video_id, bot_id=self._bot_id)
