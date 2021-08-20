import socket
from ArtNetClass.LedControl.SBC._OneChannel import OneChannel


class LedControlSBC(object):

    def __init__(self, bot_id):
        self._bot_id = bot_id
        # ART_NET
        self._art_net = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # CHANNELS
        self._channels = dict()
        for cid in range(16):
            self._channels[cid] = OneChannel(art_net=self._art_net, channel_id=cid)

    def __getitem__(self, cid):
        return self._channels[cid]


if __name__ == '__main__':
    led = LedControlSBC(bot_id=1)
    # 测试一: 单点
    led[1].universe[1].set_rgb(address=1, r=100, g=0, b=0)
    led[1].universe[1].show()
    # 测试二: 单通道闪烁
    led[1].set_blink()
    # 测试三: 单通道彩色点
    led[1].set_colorful()
