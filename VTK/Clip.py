import vtk


cone = vtk.vtkConeSource()
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cone.GetOutputPort())
actor = vtk.vtkActor()
actor.SetMapper(mapper)

ren = vtk.vtkRenderer()
ren.AddActor(actor)
ren.SetBackground(0, 0, 0)

ren_win = vtk.vtkRenderWindow()
ren_win.AddRenderer(ren)

plane = vtk.vtkPlane()

clipper = vtk.vtkClipPolyData()
clipper.SetInputConnection(cone.GetOutputPort())
clipper.SetClipFunction(plane)
clipper.InsideOutOn()
# clipper.GenerateClippedOutputOn()

mapper_in = vtk.vtkPolyDataMapper()
mapper_in.SetInputConnection(clipper.GetOutputPort())
actor_in = vtk.vtkLODActor()
actor_in.SetMapper(mapper_in)
actor_in.GetProperty().SetColor(0, 1, 0)
ren.AddActor(actor_in)

# mapper_out = vtk.vtkPolyDataMapper()
# mapper_out.SetInputConnection(clipper.GetOutputPort(0))
# actor_out = vtk.vtkActor()
# actor_out.SetMapper(mapper_in)
# actor_out.GetProperty().SetColor(1, 0, 0)
# ren.AddActor(actor_out)


def my_callback(obj, event):
    global plane, actor_in
    obj.GetPlane(plane)
    actor_in.VisibilityOn()
i_ren = vtk.vtkRenderWindowInteractor()
i_ren.SetRenderWindow(ren_win)
i_ren.SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())
ren_win.Render()
plane_widget = vtk.vtkImplicitPlaneWidget()
plane_widget.SetInteractor(i_ren)
plane_widget.SetPlaceFactor(1)
plane_widget.SetInputConnection(cone.GetOutputPort())
plane_widget.PlaceWidget()
plane_widget.AddObserver('InteractionEvent', my_callback)
plane_widget.On()
i_ren.Start()
