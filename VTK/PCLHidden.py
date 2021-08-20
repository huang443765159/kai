import vtk
from numpy import random


def actor_axis():
    actor = vtk.vtkAxesActor()
    actor.SetTotalLength(4, 4, 4)
    actor.SetShaftType(0)
    actor.SetCylinderRadius(0.01)
    actor.GetXAxisCaptionActor2D().SetWidth(0.01)
    actor.GetYAxisCaptionActor2D().SetWidth(0.01)
    actor.GetZAxisCaptionActor2D().SetWidth(0.01)
    return actor


class PCLHidden(object):

    def __init__(self):
        # COLOR
        self._colors = dict()
        # RGB 列表第四位 0=AlPHA
        self.color = {'RED': (255, 0, 0, 255), 'BLUE': (0, 0, 255, 255)}
        for color_name in ['RED', 'BLUE']:
            self._colors[color_name] = vtk.vtkUnsignedCharArray()
            self._colors[color_name].SetNumberOfComponents(4)
        # VTK DATA
        self.points = vtk.vtkPoints()
        self.cell = vtk.vtkCellArray()
        self.poly = vtk.vtkPolyData()
        self.poly.SetPoints(self.points)
        self.poly.SetVerts(self.cell)
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(self.poly)
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(mapper)
        self.actor.GetProperty().SetColor(0, 1, 0)
        self.actor.GetProperty().SetPointSize(3)
        # PCL GROWN UP
        for i in range(2000):
            self.points_grown_up()

    def points_grown_up(self):
        point_id = self.points.InsertNextPoint(20 * (random.rand(3) - 0.5))
        self.cell.InsertNextCell(1)
        self.cell.InsertCellPoint(point_id)
        self._colors['RED'].InsertNextTuple4(*self.color['RED'])
        self._colors['BLUE'].InsertNextTuple4(*self.color['BLUE'])
        self.points.Modified()
        self.cell.Modified()
        self.poly.Modified()

    def set_color_name(self, color_name):
        self.poly.GetPointData().SetScalars(self._colors[color_name])
        self.poly.Modified()

    def clear_color(self):
        temp_color = vtk.vtkUnsignedCharArray()
        temp_color.SetNumberOfComponents(4)
        self.poly.GetPointData().SetScalars(temp_color)


if __name__ == '__main__':

    def render_timer(obj, event):
        obj.GetRenderWindow().Render()

    def vtk_show(actors):
        ren = vtk.vtkRenderer()
        ren.UseHiddenLineRemovalOn()
        if actors.__class__ in [vtk.vtkActor, vtk.vtkAxesActor, vtk.vtkAssembly]:
            ren.AddActor(actors)
        elif actors.__class__ is list:
            for actor in actors:
                ren.AddActor(actor)
        ren_win = vtk.vtkRenderWindow()
        ren_win.AddRenderer(ren)
        ren_win.SetSize(750, 750)
        i_ren = vtk.vtkRenderWindowInteractor()
        i_ren.SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())
        i_ren.SetRenderWindow(ren_win)
        # TIMER
        i_ren.AddObserver('TimerEvent', render_timer)
        i_ren.CreateRepeatingTimer(10)
        i_ren.Initialize()
        i_ren.Start()

    _plc = PCLHidden()
    _plc.set_color_name('RED')
    # plc_display.clear_color()
    # plc_display.set_color_name('BLUE')
    vtk_show([actor_axis(), _plc.actor])
