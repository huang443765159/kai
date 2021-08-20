import time
import threading
from ArtNetClass.Utils.CONST import CONST
from ArtNetClass.LedControl.SBC._OneUniverse import OneUniverse


class OneChannel(object):

    def __init__(self, art_net, channel_id):
        self._channel_id = channel_id
        # UNIVERSES
        self.universe = dict()
        for idx, universe in enumerate(CONST.ART_NET.UNIVERSES[channel_id]):
            self.universe[idx] = OneUniverse(universe=universe, art_net=art_net)
        # THREAD
        self._thread_switch = False

    def set_r(self, r: int):
        for universe in self.universe.values():
            for i in range(1, 171):
                universe.set_rgb(address=3 * (i - 1) + 1, r=r, g=0, b=0)
            universe.show()

    def set_g(self, g: int):
        for universe in self.universe.values():
            for i in range(1, 171):
                universe.set_rgb(address=3 * (i - 1) + 1, r=0, g=g, b=0)
            universe.show()

    def set_b(self, b: int):
        for universe in self.universe.values():
            for i in range(1, 171):
                universe.set_rgb(address=3 * (i - 1) + 1, r=0, g=0, b=b)
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

    def set_blink(self):
        thread = threading.Thread(target=self._working)
        self._thread_switch = True
        thread.daemon = True
        thread.start()

    def _working(self):
        while 1:
            if self._thread_switch:
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
                time.sleep(CONST.ART_NET.DELAY)
                for universe in self.universe.values():
                    for i in range(1, 171):
                        if (i - 1) % 3 == 0:
                            r, g, b = 0, 100, 0
                        elif (i - 2) % 3 == 0:
                            r, g, b = 0, 0, 100
                        else:
                            r, g, b = 100, 0, 0
                        universe.set_rgb(address=3 * (i - 1) + 1, r=r, g=g, b=b)
                    universe.show()
                time.sleep(CONST.ART_NET.DELAY)
                for universe in self.universe.values():
                    for i in range(1, 171):
                        if (i - 1) % 3 == 0:
                            r, g, b = 0, 0, 100
                        elif (i - 2) % 3 == 0:
                            r, g, b = 100, 0, 0
                        else:
                            r, g, b = 0, 100, 0
                        universe.set_rgb(address=3 * (i - 1) + 1, r=r, g=g, b=b)
                    universe.show()
                time.sleep(CONST.ART_NET.DELAY)

    def stop(self):
        self._thread_switch = False
