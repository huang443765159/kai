from vtkmodules import all as vtk
import numpy as np


def GetAngleBetweenPoints(endPt1, connectingPt, endPt2):
    x1 = endPt1[0] - connectingPt[0]
    y1 = endPt1[1] - connectingPt[1]
    x2 = endPt2[0] - connectingPt[0]
    y2 = endPt2[1] - connectingPt[1]
    angle = np.arctan2(y1, x1) - np.arctan2(y2, x2)
    angle = angle * 360 / (2 * np.pi)
    if (angle < 0):
        angle += 360
    return angle


textSource = vtk.vtkVectorText()
textSource.SetText("Forward")
textSource.Update()

transfo = vtk.vtkTransform()
transfo.Identity()
transfo.PostMultiply()

x = 1
xo = 0
y = 1
yo = 0
z = 1
zo = 1
# angle Z
teta = GetAngleBetweenPoints([x, y], [0, 0], [xo, yo])
print(teta)
transfo.RotateWXYZ(+(teta), 0, 0, 1)
# angle Y
teta = GetAngleBetweenPoints([x, z], [0, 0], [xo, zo])
print(teta)
transfo.RotateWXYZ(+(teta), 0, 1, 0)
transfo.Translate(x, y, z)

filter = vtk.vtkTransformPolyDataFilter()
filter.SetInputConnection(textSource.GetOutputPort())
filter.SetTransform(transfo)
filter.Update()

# Create a mapper and actor
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(filter.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(1.0, 0.0, 0.0)

# Create a renderer, render window, and interactor
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

renderer.AddActor(actor)
renderer.AddActor(vtk.vtkAxesActor())
renderer.SetBackground(0.4, 0.3, 0.2)

renderWindow.Render()
style = vtk.vtkInteractorStyleMultiTouchCamera()
renderWindowInteractor.SetInteractorStyle(style)
renderWindowInteractor.Start()
