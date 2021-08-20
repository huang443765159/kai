from vtkmodules import all


class OnePoint(object):

    def __init__(self, size, color, opacity):
        # POINT
        self.points = all.vtkPoints()
        poly = all.vtkPolyData()
        poly.SetPoints(self.points)
        mapper = all.vtkPointGaussianMapper()
        mapper.SetInputData(poly)
        mapper.EmissiveOff()
        mapper.SetScaleFactor(0.0)
        self.actor = all.vtkActor()
        self.actor.SetMapper(mapper)
        self.actor.GetProperty().SetPointSize(size)
        self.actor.GetProperty().SetColor(color)
        self.actor.GetProperty().SetOpacity(opacity)

    def set_pos(self, pos: list):
        self.actor.SetPosition(pos)

    def set_color(self, color):
        color = [i / 255 for i in color]
        self.actor.GetProperty().SetColor(color)

    def get_pos(self):
        return self.actor.GetPosition()

    def get_color(self):
        return self.actor.GetProperty().GetColor()

    def opacity(self, opacity):
        self.actor.GetProperty().SetOpacity(opacity)