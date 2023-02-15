import vtk
import time
import random
import threading
from numpy import random


def actor_axis():
    actor = vtk.vtkAxesActor()
    actor.SetTotalLength(3, 3, 3)
    actor.SetShaftType(0)
    actor.SetCylinderRadius(0.01)
    actor.GetXAxisCaptionActor2D().SetWidth(0.01)
    actor.GetYAxisCaptionActor2D().SetWidth(0.01)
    actor.GetZAxisCaptionActor2D().SetWidth(0.01)
    return actor


def actor_line(p1, p2):
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


class Test(object):

    def __init__(self):
        # POINTS
        self.points = vtk.vtkPoints()
        self.cell = vtk.vtkCellArray()
        self.poly = vtk.vtkPolyData()
        self.poly.SetPoints(self.points)
        self.poly.SetVerts(self.cell)
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(self.poly)
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(mapper)
        # CLIP
        box = vtk.vtkBox()
        box.SetBounds(0, 1, 0, 1, 0, 1)
        self.clipper = vtk.vtkClipPolyData()
        self.clipper.SetInputData(self.poly)
        self.clipper.SetClipFunction(box)
        self.clipper.Update()
        mapper_in = vtk.vtkPolyDataMapper()
        mapper_in.SetInputConnection(self.clipper.GetOutputPort(1))
        actor_in = vtk.vtkActor()
        actor_in.SetMapper(mapper_in)
        actor_in.GetProperty().SetColor(1, 0, 0)
        mapper_out = vtk.vtkPolyDataMapper()
        mapper_out.SetInputConnection(self.clipper.GetOutputPort(0))
        actor_out = vtk.vtkActor()
        actor_out.SetMapper(mapper_out)
        actor_out.GetProperty().SetColor(0, 1, 0)
        self.actor = vtk.vtkAssembly()
        self.actor.AddPart(actor_in)
        self.actor.AddPart(actor_out)

        for i in range(10000):
            self.points_grown_up()
        # THREAD
        # self._thread = threading.Thread(target=self._working)
        # self._thread.start()

    def points_grown_up(self):
        points_id = self.points.InsertNextPoint(20 * (random.rand(3) - 0.5))
        # id = self.points.InsertNextPoint([random.random(), random.random(), random.random()]
        self.cell.InsertNextCell(1)
        self.cell.InsertCellPoint(points_id)
        self.points.Modified()
        self.cell.Modified()
        self.poly.Modified()

    # def _working(self):
    #     while 1:
    #         if self.points.GetNumberOfPoints() < 1000:
    #             self.points_grown_up()
    #         time.sleep(0.001)


if __name__ == '__main__':

    def timer(obj, event):
        global test
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

        if actors.__class__ in [vtk.vtkActor, vtk.vtkAxesActor, vtk.vtkAssembly]:
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
    vtk_show([actor_axis(), test.actor])