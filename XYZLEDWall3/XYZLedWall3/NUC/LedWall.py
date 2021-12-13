from PyQt5.QtCore import QObject
from XYZLedWall3.Utils.CONST import CONST
from XYZLedWall3.Utils.RgbHandle import RgbHandle
from XYZLedWall3.NUC._OneLedWall import OneLedWall
from XYZLedWall3.NUC.Vtk.VtkPoints import VtkPoints


class LedWall(QObject):

    def __init__(self, show_path: str):
        super().__init__()
        # HANDLE
        self._rgb = RgbHandle(show_path=show_path, rgb_callback=self._rgb_callback)
        # POINTS
        self._points = dict()
        for bot_id in [1, 2]:
            self._points[bot_id] = VtkPoints(bot_id=bot_id)
            self._points[bot_id].add_points(rows=CONST.LED.ROWS, cols=CONST.LED.COLS)
        # LED_WALL
        self._led = dict()
        for bot_id in [1, 2]:
            self._led[bot_id] = OneLedWall(bot_id=bot_id, rgb=self._rgb, points=self._points[bot_id])

    def _rgb_callback(self, rgb_list, bot_id):
        self._led[bot_id].show(rgb_list=rgb_list)

    def set_render(self, render):
        for bot_id in self._led.keys():
            self._led[bot_id].set_render(render=render)
            render.add_actor(self._points[bot_id].actor)

    def __getitem__(self, bot_id):
        return self._led[bot_id]

    def set_link(self, link: bool):
        for bot_id in self._led.keys():
            self._led[bot_id].set_link(link=link)

    def get_link(self):
        return self._led[1].get_link()

    def stop(self):
        self._rgb.stop()

    def link_inviter(self, inviter):
        for bot_id in self._led.keys():
            self._led[bot_id].link_inviter(inviter=inviter)
