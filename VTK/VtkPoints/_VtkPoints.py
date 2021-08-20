from vtkmodules import all


class VtkPoints(object):

    def __init__(self, size=3, opacity=1):
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

    def add_points(self, points):
        for point in points:
            self._color_array.InsertNextTuple3(100, 0, 0)
            self._points.InsertNextPoint(point)
        self._points.Modified()
        self._poly.GetPointData().SetScalars(self._color_array)

    def set_color(self, color, rgb_list=None):
        self._color_array.Reset()
        if rgb_list is None:
            for idx in range(self._points.GetNumberOfPoints()):
                self._color_array.InsertNextTuple3(*color)
        else:
            for idx, rgb in enumerate(rgb_list):
                self._color_array.InsertNextTuple3(*rgb)
        self._color_array.Modified()

    def get_points_num(self):
        return self._points.GetNumberOfPoints()

    def set_opacity(self, opacity: float):
        self.actor.GetProperty().SetOpacity(opacity)
