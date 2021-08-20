import vtk
import time
import random
import threading
from numpy import random


class Test(object):

    def __init__(self):
        self.points = vtk.vtkPoints()
        self.cell = vtk.vtkCellArray()
        poly = vtk.vtkPolyData()
        poly.SetPoints(self.points)
        poly.SetVerts(self.cell)
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(poly)
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(mapper)

        self._thread = threading.Thread(target=self._working)
        self._thread.start()

    def actor_axis(self):
        actor = vtk.vtkAxesActor()
        actor.SetTotalLength(2, 2, 2)
        actor.SetShaftType(0)
        actor.SetCylinderRadius(0.01)
        actor.GetXAxisCaptionActor2D().SetWidth(0.01)
        actor.GetYAxisCaptionActor2D().SetWidth(0.01)
        actor.GetZAxisCaptionActor2D().SetWidth(0.01)
        actor.RotateX(100)
        return actor

    def actor_line(self, p1, p2):
        line = vtk.vtkLineSource()
        line.SetPoint1(p1)
        line.SetPoint2(p2)
        line.Update()
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(line.GetOutput())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(1, 0, 0)
        return actor

    def points_grown_up(self):
        points_id = self.points.InsertNextPoint(20 * (random.rand(3) - 0.5))
        # id = self.points.InsertNextPoint([random.random(), random.random(), random.random()]
        self.cell.InsertNextCell(1)
        self.cell.InsertCellPoint(points_id)
        self.points.Modified()
        self.cell.Modified()

    def _working(self):
        while 1:
            if self.points.GetNumberOfPoints() < 10000:
                self.points_grown_up()
            time.sleep(0.001)


if __name__ == '__main__':

    def timer(obj, event):
        obj.GetRenderWindow().Render()


    def vtk_show(actors):
        ren = vtk.vtkRenderer()
        ren.UseHiddenLineRemovalOn()
        ren_win = vtk.vtkRenderWindow()
        ren_win.AddRenderer(ren)
        i_ren = vtk.vtkRenderWindowInteractor()
        i_ren.SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())
        i_ren.SetRenderWindow(ren_win)

        i_ren.AddObserver('TimerEvent', timer)
        i_ren.CreateRepeatingTimer(10)

        if actors.__class__ in [vtk.vtkActor, vtk.vtkAxesActor]:
            ren.AddActor(actors)
        elif actors.__class__ is list:
            for actor in actors:
                ren.AddActor(actor)
        ren_win.SetSize(1800, 1800)
        # ren_win.Render()
        i_ren.Initialize()
        i_ren.Start()
        i_ren.Initialize()
        i_ren.Start()


    test = Test()
    vtk_show([test.actor_axis(), test.actor_line([1.0, 0.0, 0.0], [1.0, 0.0, 5.0]), test.actor])
