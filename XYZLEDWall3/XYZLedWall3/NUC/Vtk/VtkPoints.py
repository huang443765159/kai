from vtkmodules import all
from XYZLedWall3.Utils.CONST import CONST


class VtkPoints(object):

    def __init__(self, bot_id, size=3, opacity=1):
        self._bot_id = bot_id
        # POINTS
        self._points = all.vtkPoints()
        self._poly = all.vtkPolyData()
        self._poly.SetPoints(self._points)
        mapper = all.vtkPointGaussianMapper()
        mapper.SetInputData(self._poly)
        mapper.EmissiveOff()
        mapper.SetScaleFactor(0.0)
        self.actor = all.vtkActor()
        self.actor.SetMapper(mapper)
        self.actor.GetProperty().SetPointSize(size)
        self.actor.GetProperty().SetOpacity(opacity)
        # COLOR
        self._color_array = all.vtkUnsignedCharArray()
        self._color_array.SetNumberOfComponents(3)

    def add_points(self, rows: int, cols: int):
        for row in range(rows):
            for col in range(cols):
                self._color_array.InsertNextTuple3(100, 0, 0)
                self._points.InsertNextPoint([col * CONST.LED.LENGTH / CONST.LED.COLS,
                                              CONST.LED.HIGH - row * CONST.LED.HIGH / CONST.LED.ROWS,
                                              0 if self._bot_id == 1 else -3.5])
        self._points.Modified()
        self._poly.GetPointData().SetScalars(self._color_array)

    def set_color(self, color, rgb_list=None, blink=False):
        self._color_array.Reset()
        if rgb_list is None:
            for idx in range(self._points.GetNumberOfPoints()):
                if blink:
                    if idx % 3 == 0:
                        color = (CONST.SHOW.COLOR[CONST.SHOW.R], 0, 0)
                    elif (idx - 1) % 3 == 0:
                        color = (0, CONST.SHOW.COLOR[CONST.SHOW.G], 0)
                    else:
                        color = (0, 0, CONST.SHOW.COLOR[CONST.SHOW.B])
                self._color_array.InsertNextTuple3(*color)
        else:
            for idx, rgb in enumerate(rgb_list):
                self._color_array.InsertNextTuple3(*rgb)

        self._color_array.Modified()

    def get_points_num(self):
        return self._points.GetNumberOfPoints()
