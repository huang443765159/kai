import pickle
import struct
from PyQt5.QtCore import QObject
from XYZNetwork3.MixServer import MixServer
from XYZNetwork3.MixInviter import MixInviter
from XYZNetwork3.Utils.CONST import CONST as NET_CONST
from XYZLedWall3.Utils.CONST import CONST
from XYZLedWall3.Utils.Signal import SIGNAL
from XYZLedWall3.Utils.RgbHandle import RgbHandle
from XYZLedWall3.NUC.Vtk.VtkPoints import VtkPoints


class OneLedWall(QObject):

    def __init__(self, bot_id, rgb: RgbHandle, points: VtkPoints):
        super().__init__()
        self._rgb = rgb
        self._bot_id = bot_id
        self._points = points
        # NETWORK
        self._network = MixServer(event_cb=self._event,
                                  error_cb=self._error,
                                  recv_cb=self._recv,
                                  tcp_port=CONST.ANET.PORT[bot_id])
        # ATTR
        self._render = None
        self._source = 'MATH'
        self._link = False

    def _event(self, module, code, value):
        if module == NET_CONST.PTC.TCP and code == NET_CONST.EVT.CONNECTION:
            is_online, (ip, port) = value
            SIGNAL.sign_is_online.emit(self._bot_id, is_online, ip, port)

    def _error(self, module, code, value):
        pass

    def _recv(self, data, ip, port):
        pass

    # SHOW
    def show(self, rgb_list):
        self._points.set_color(color=None, rgb_list=rgb_list)
        self._render.render_once()
        if self._link:
            self._network.tcp.send(CONST.ANET.SHOW_HEAD + pickle.dumps(rgb_list))

    def read_img(self, img_id: int, bot_id: int):
        self._rgb.read_img(img_id=img_id, bot_id=bot_id)

    def read_video(self, video_id: int, bot_id: int):
        self._rgb.read_video(video_id=video_id, bot_id=bot_id)

    def set_r(self):
        self._points.set_color(color=(CONST.SHOW.COLOR[CONST.SHOW.R], 0, 0))
        self._render.render_once()
        if self._link:
            self._network.tcp.send(CONST.ANET.COLOR_HEAD + struct.pack('b', CONST.SHOW.R))

    def set_g(self):
        self._points.set_color(color=(0, CONST.SHOW.COLOR[CONST.SHOW.G], 0))
        self._render.render_once()
        if self._link:
            self._network.tcp.send(CONST.ANET.COLOR_HEAD + struct.pack('b', CONST.SHOW.G))

    def set_b(self):
        self._points.set_color(color=(0, 0, CONST.SHOW.COLOR[CONST.SHOW.B]))
        self._render.render_once()
        if self._link:
            self._network.tcp.send(CONST.ANET.COLOR_HEAD + struct.pack('b', CONST.SHOW.B))

    def set_blink(self):
        pass

    def set_colorful(self):
        self._points.set_color(color=None, blink=True)
        self._render.render_once()
        if self._link:
            self._network.tcp.send(CONST.ANET.COLOR_HEAD + struct.pack('b', CONST.SHOW.COLORFUL))

    # LINK
    def set_link(self, link: bool):
        self._link = link
        self._source = 'DEV' if self._link else 'MATH'

    def get_link(self):
        return self._link

    def set_render(self, render):
        self._render = render

    def link_inviter(self, inviter: MixInviter):
        inviter.add_server(self._network)
