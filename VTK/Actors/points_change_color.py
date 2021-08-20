from vtkmodules import all


points = all.vtkPoints()
poly = all.vtkPolyData()
poly.SetPoints(points)
mapper = all.vtkPointGaussianMapper()
mapper.SetInputData(poly)
mapper.EmissiveOff()
mapper.SetScaleFactor(0.0)
actor = all.vtkActor()
actor.SetMapper(mapper)

colors_array = all.vtkUnsignedCharArray()
colors_array.SetNumberOfComponents(3)
for i in range(1000):
    color = (i * 0.1, 0, 0)
    colors_array.InsertNextTuple3(*color)
    points.InsertNextPoint([0.1 * i, 0.1 * i, 0])
points.Modified()

poly.GetPointData().SetScalars(colors_array)

render = all.vtkRenderer()
render.AddActor(actor)
ren_win = all.vtkRenderWindow()
ren_win.AddRenderer(render)
ren_win.SetSize(500, 500)
# colors_array.Reset()
# for i in range(0, 1000):
#     colors_array.InsertNextTuple3(0, 255, 0)
# colors_array.Modified()

ren_win.Render()
i_ren = all.vtkRenderWindowInteractor()
i_ren.SetRenderWindow(ren_win)
i_ren.Initialize()
i_ren.Start()
