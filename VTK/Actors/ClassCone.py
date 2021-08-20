import vtk


class OneCone(object):

    def __init__(self, angle: int, color: list, height=1.5, resolution=200):
        self._cone = vtk.vtkConeSource()
        # SET
        self.set_angle(angle=angle)
        self.set_height(height=height)
        self.set_direction(1, 0, 0)
        self.set_resolution(resolution=resolution)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(self._cone.GetOutputPort())
        # ACTOR
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(mapper)
        # PROPERTY
        self._property = self.actor.GetProperty()
        self.set_color(color=color)

    def set_angle(self, angle: int):
        self._cone.SetAngle(angle)

    def set_height(self, height: float):
        self._cone.SetHeight(height)

    def set_center(self, center: list):
        self._cone.SetCenter(center)

    def set_direction(self, x, y, z):
        self._cone.SetDirection([x, y, z])

    def set_resolution(self, resolution: int):
        self._cone.SetResolution(resolution)

    def set_color(self, color: list):
        color = [rgb / 255 for rgb in color]
        self._property.SetColor(color)

    def get_angle(self):
        return self._cone.GetAngle()

    def get_height(self):
        return self._cone.GetHeight()

    def get_center(self):
        return self._cone.GetCenter()

    def get_direction(self):
        return self._cone.GetDirection()

    def get_resolution(self):
        return self._cone.GetResolution()

    def get_color(self):
        return self._property.GetColor()


if __name__ == '__main__':
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())
    actor = OneCone(color=[255, 0, 0], angle=20)
    ren.AddActor(actor.actor)
    # 小立方体
    # axesActor = vtk.vtkAxesActor()
    # axes = vtk.vtkOrientationMarkerWidget()
    # axes.SetOrientationMarker(axesActor)
    # axes.SetInteractor(iren)
    # axes.EnabledOn()
    # axes.InteractiveOn()
    # ren.ResetCamera()

    renWin.SetSize(1200, 1200)
    iren.Initialize()
    renWin.Render()
    iren.Start()
