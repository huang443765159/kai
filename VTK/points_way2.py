import vtk

from PyQt5.QtCore import QObject

def PointsDisplay(points):
    Points = vtk.vtkPoints()
    vertices = vtk.vtkCellArray()
    for v in points:
        point_tmp = [v[0], v[1], v[2]]
        id = Points.InsertNextPoint(point_tmp)
        vertices.InsertNextCell(1)
        vertices.InsertCellPoint(id)

    polydata = vtk.vtkPolyData()
    polydata.SetPoints(Points)
    polydata.SetVerts(vertices)
    Mapper = vtk.vtkPolyDataMapper()
    Mapper.SetInputData(polydata)
    Actor = vtk.vtkActor()
    Actor.SetMapper(Mapper)
    Actor.GetProperty().SetColor(1, 0, 0)

    ren1 = vtk.vtkRenderer()
    ren1.AddActor(Actor)
    # ren1.AddActor(ref_Actor)
    ren1.SetBackground(0.1, 0.2, 0.4)
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren1)
    # renWin.SetFullScreen(True)
    renWin.SetSize(300, 300)
    renWin.Render()
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()


PointsDisplay([[1, 1, 0], [2, 2, 0], [3, 3, 0]])
