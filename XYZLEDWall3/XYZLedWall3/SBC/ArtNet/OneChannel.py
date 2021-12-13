from XYZLedWall3.Utils.CONST import CONST
from XYZLedWall3.SBC.ArtNet._OneUniverse import OneUniverse


class OneChannel(object):

    def __init__(self, art_net, channel_id):
        self._art_net = art_net
        self._channel_id = channel_id
        # UNIVERSE
        self.universe = dict()
        for idx in CONST.ARTNET.CHANNELS[channel_id]:
            self.universe[idx] = OneUniverse(universe=idx, art_net=art_net)
        # THREAD
        self._thread_switch = False

    def set_r(self, r=100):
        for universe in self.universe.values():
            for i in range(1, 171):
                universe.set_rgb(address=3 * (i - 1) + 1, r=r, g=0, b=0)
            universe.show()

    def set_g(self, g=100):
        for universe in self.universe.values():
            for i in range(1, 171):
                universe.set_rgb(address=3 * (i - 1) + 1, r=0, g=g, b=0)
            universe.show()

    def set_b(self, b=100):
        for universe in self.universe.values():
            for i in range(1, 171):
                universe.set_rgb(address=3 * (i - 1) + 1, r=0, g=0, b=b)
            universe.show()

    def set_color(self, color_id: int):
        for universe in self.universe.values():
            if color_id == CONST.SHOW.R:
                r, g, b = CONST.SHOW.COLOR[CONST.SHOW.R], 0, 0
            elif color_id == CONST.SHOW.G:
                r, g, b = 0, CONST.SHOW.COLOR[CONST.SHOW.G], 0
            else:
                r, g, b = 0, 0, CONST.SHOW.COLOR[CONST.SHOW.B]
            for i in range(1, 171):
                universe.set_rgb(address=3 * (i - 1) + 1, r=r, g=g, b=b)
            universe.show()

    def set_colorful(self):
        for universe in self.universe.values():
            for i in range(1, 171):
                if (i - 1) % 3 == 0:
                    r, g, b = 100, 0, 0
                elif (i - 2) % 3 == 0:
                    r, g, b = 0, 100, 0
                else:
                    r, g, b = 0, 0, 100
                universe.set_rgb(address=3 * (i - 1) + 1, r=r, g=g, b=b)
            universe.show()
