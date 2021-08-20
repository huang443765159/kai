import vtk


class OneLine(object):

    def __init__(self, color, size):
        self._color = color
        self._size = size

        # VTK
        self._line = vtk.vtkLineSource()
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(self._line.GetOutput())
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(mapper)
        self.actor.GetProperty().SetColor(self._color)
        self.actor.GetProperty().SetLineWidth(self._size)

    def set_points(self, p1, p2):
        self._line.SetPoint1(p1)
        self._line.SetPoint2(p2)
        self._line.Update()

    def set_color(self, color):
        self.actor.GetProperty().SetColor(color)

    def get_color(self):
        return self.actor.GetProperty().GetColor()

    def set_line_width(self, size):
        self.actor.GetProperty().SetLineWidth(size)

    def get_line_width(self):
        return self.actor.GetProperty().GetLineWidth()
