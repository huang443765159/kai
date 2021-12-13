import math
import socket
import pickle
import struct
from PyQt5.QtCore import QObject
from XYZNetwork3.MixClient import MixClient
from XYZNetwork3.Utils.CONST import CONST as NET_CONST
from XYZLedWall3.Utils.CONST import CONST
from XYZLedWall3.Utils.Signal import SIGNAL
from XYZLedWall3.Utils.RgbHandle import RgbHandle
from XYZLedWall3.Utils.RgbMapping import rbg_mapping
from XYZLedWall3.SBC.ArtNet.OneChannel import OneChannel


class LedWall(QObject):

    def __init__(self, bot_id, show_path):
        super().__init__()
        self._bot_id = bot_id
        # NETWORK
        self._network = MixClient(event_cb=self._event,
                                  error_cb=self._error,
                                  recv_cb=self._recv,
                                  tcp_port=CONST.ANET.PORT[bot_id])
        self._network.set_machine_sn(machine_sn=CONST.TEST.MACHINE_SN)
        # ART_NET
        self._art_net = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # CHANNELS
        self._channels = dict()
        for cid in range(16):
            self._channels[cid] = OneChannel(art_net=self._art_net, channel_id=cid)
        # RGB_HANDLE
        self.rgb = RgbHandle(show_path=show_path, rgb_callback=self._rgb_callback)
        # ATTR
        self._universe = int()

    def _event(self, module, code, value):
        if module == NET_CONST.PTC.TCP and code == NET_CONST.EVT.CONNECTION:
            is_online, (ip, port) = value
            SIGNAL.sign_is_online.emit(self._bot_id, is_online, ip, port)

    def _error(self, module, code, value):
        pass

    def _recv(self, data, ip, pkt_id):
        head = data[0: 2]
        if head == CONST.ANET.COLOR_HEAD:
            color_id = struct.unpack('b', data[2:])[0]
            for cid in self._channels.keys():
                if color_id == CONST.SHOW.COLORFUL:
                    self._channels[cid].set_colorful()
                else:
                    self._channels[cid].set_color(color_id=color_id)
        elif head == CONST.ANET.SHOW_HEAD:
            rgb_list = pickle.loads(data[2:])
            self._set_rgb(rgb_list=rgb_list)

    def _rgb_callback(self, rgb_list, bot_id):
        self._set_rgb(rgb_list=rgb_list)

    def _set_rgb(self, rgb_list):
        rgb_dict = rbg_mapping(rgb_list=rgb_list)
        for led_id, rgb in sorted(rgb_dict.items()):
            cid = int(led_id / CONST.ARTNET.IMG_PIXEL)
            uni_id = int((led_id % CONST.ARTNET.IMG_PIXEL) / CONST.ARTNET.UNIVERSE_PIXEL) + math.ceil(
                cid * CONST.ARTNET.PHY_PIXEL / CONST.ARTNET.UNIVERSE_PIXEL)
            if cid == 0:
                addr = led_id % CONST.ARTNET.UNIVERSE_PIXEL + 1
            else:
                addr = (led_id - 600 * cid) % CONST.ARTNET.UNIVERSE_PIXEL + 1
            self._channels[cid].universe[uni_id].set_rgb(address=3 * (addr - 1) + 1, r=list(rgb)[0], g=list(rgb)[1], b=list(rgb)[2])
            if addr == 170 or (addr == 90 and (uni_id + 1) % 4 == 0):
                self._channels[cid].universe[uni_id].show()

    def set_r(self):
        for cid in self._channels.keys():
            self._channels[cid].set_r()

    def set_g(self):
        for cid in self._channels.keys():
            self._channels[cid].set_g()

    def set_b(self):
        for cid in self._channels.keys():
            self._channels[cid].set_b()

    def set_colorful(self):
        for cid in self._channels.keys():
            self._channels[cid].set_colorful()

    def __getitem__(self, cid):
        return self._channels[cid]
