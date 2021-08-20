import vtk
import time
import random
import threading
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


class Test(object):

    def __init__(self):
        # POINTS
        self.points = vtk.vtkPoints()
        self.cell = vtk.vtkCellArray()
        self.poly = vtk.vtkPolyData()
        self.poly.SetPoints(self.points)
        self.poly.SetVerts(self.cell)
        # mapper = vtk.vtkPolyDataMapper()
        # mapper.SetInputData(self.poly)
        # self.actor = vtk.vtkActor()
        # self.actor.SetMapper(mapper)
        # CLIP
        # self.clipper = vtk.vtkGeometryFilter()
        # self.clipper.SetInput(self.poly)
        geometry = vtk.vtkGeometryFilter()
        geometry.SetInputData(self.poly)
        geometry.ExtentClippingOn()
        geometry.SetExtent(-2, 2, -2, 2, -2, 2)
        geometry.PointClippingOn()
        # geometry.SetPointMinimum(0)
        # geometry.SetPointMaximum(1000)
        # geometry.CellClippingOn()
        # geometry.SetCellMinimum(0)
        # geometry.SetCellMaximum(100)
        geometry.Update()
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(geometry.GetOutputPort())
        mapper.SetScalarRange(1, 1.0)
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(mapper)
        self.actor.GetProperty().SetColor(1, 0, 0)

        # for i in range(50000):
        #     self.points_grown_up()
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.start()

    def points_grown_up(self):
        points_id = self.points.InsertNextPoint(20 * (random.rand(3) - 0.5))
        # id = self.points.InsertNextPoint([random.random(), random.random(), random.random()]
        self.cell.InsertNextCell(1)
        self.cell.InsertCellPoint(points_id)
        self.points.Modified()
        self.cell.Modified()
        self.poly.Modified()

    def _working(self):
        while 1:
            if self.points.GetNumberOfPoints() < 50000:
                self.points_grown_up()
            # time.sleep(0.0001)


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
        i_ren.CreateRepeatingTimer(1)

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