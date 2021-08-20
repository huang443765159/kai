import vtk


class Cube(object):

    def __init__(self, x_length: float, y_length: float, z_length: float, opacity=0.2):
        self._cube = vtk.vtkCubeSource()
        self._cube.SetXLength(x_length)
        self._cube.SetYLength(y_length)
        self._cube.SetZLength(z_length)
        self._cube.Update()
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(self._cube.GetOutputPort())
        self.actor = vtk.vtkActor()
        self._property = self.actor.GetProperty()
        self._property.SetOpacity(opacity)
        self.actor.SetMapper(mapper)

    def set_color(self, color: tuple):
        color = [rgb / 255 for rgb in color]
        self._property.SetColor(color)

    def set_opacity(self, opacity: float):
        self._property.SetOpacity(opacity)

    def set_xyz_length(self, x_length: float, y_length: float, z_length: float):
        self._cube.SetXLength(x_length)
        self._cube.SetYLength(y_length)
        self._cube.SetZLength(z_length)
        self._cube.Update()


if __name__ == '__main__':
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())
    actor = Cube(7.0, 2.5, 3.5)
    ren.AddActor(actor.actor)
    # 小立方体
    axesActor = vtk.vtkAxesActor()
    axes = vtk.vtkOrientationMarkerWidget()
    axes.SetOrientationMarker(axesActor)
    axes.SetInteractor(iren)
    axes.EnabledOn()
    axes.InteractiveOn()
    ren.ResetCamera()

    renWin.SetSize(1200, 1200)
    iren.Initialize()
    renWin.Render()
    iren.Start()
