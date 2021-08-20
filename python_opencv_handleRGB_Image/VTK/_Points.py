from PyQt5.QtCore import QObject
from python_opencv_handleRGB_Image.VTK._OnePoint import OnePoint


class Points(QObject):

    def __init__(self, render):
        super().__init__()
        # RENDER
        self._render = render
        # POINTS
        p_id = 0
        self._points = dict()
        for cols in range(68):
            for rows in range(91):
                self._points[p_id] = OnePoint(size=3, color=(255, 0, 0), opacity=0.3)
                self._points[p_id].points.InsertNextPoint(cols * 0.68 / 68,
                                                          (0.68 / 68 * 91 - rows * 0.68 / 68) if cols % 2 == 0 else 0 + rows * 0.68 / 68,
                                                          0)
                self._points[p_id].points.Modified()
                self._render.AddActor(self._points[p_id].actor)
                p_id += 1

    def set_point_color(self, p_id, color):
        self._points[p_id].set_color(color=list(color))
