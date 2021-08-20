from vtkmodules import all


class VtkLine(object):

    def __init__(self, color, width):
        self._color = color
        # LINE
        self._points = all.vtkPoints()
        self._lines = all.vtkCellArray()
        self._line = all.vtkLine()
        poly = all.vtkPolyData()
        poly.SetPoints(self._points)
        poly.SetLines(self._lines)
        mapper = all.vtkPolyDataMapper()
        mapper.SetInputData(poly)
        self.actor = all.vtkActor()
        self.actor.SetMapper(mapper)
        self.actor.GetProperty().SetLineWidth(width)
        self.actor.GetProperty().SetColor(color)

    def set_point(self, p):
        self._points.InsertNextPoint(p)

    def set_line(self, l_id, p_id):
        self._line.GetPointIds().SetId(l_id, p_id)
        self._line.GetPointIds().SetId(l_id + 1, p_id + 1)
        self._lines.InsertNextCell(self._line)

    def set_color(self, color: tuple):
        self.actor.GetProperty().SetColor(color)

