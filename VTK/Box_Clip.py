import vtk

def actor_clip():
	sphere = vtk.vtkSphereSource()
	sphere.SetCenter(1, 1, 1)
	sphere.SetRadius(1)
	sphere.Update()
	
	box = vtk.vtkBox()
	box.SetBounds(0, 7, -1, 4, -3, 1)
	
	clipper = vtk.vtkClipPolyData()
	clipper.SetClipFunction(box)
	clipper.SetInputConnection(sphere.GetOutputPort())
	clipper.GenerateClippedOutputOn()
	clipper.Update()
	
	mapper_in = vtk.vtkPolyDataMapper()
	mapper_in.SetInputConnection(clipper.GetOutputPort(1))
	actor_in = vtk.vtkActor()
	actor_in.SetMapper(mapper_in)
	actor_in.GetProperty().SetColor(0, 255, 0)
	actor_in.GetProperty().SetPointSize(2)

	mapper_out = vtk.vtkPolyDataMapper()
	mapper_out.SetInputConnection(clipper.GetOutputPort(0))
	actor_out = vtk.vtkActor()
	actor_out.SetMapper(mapper_out)
	actor_out.GetProperty().SetColor(255, 0, 0)
	actor_in.GetProperty().SetPointSize(2)
	
	return actor_in, actor_out
	
def vtk_show(actor_list):
	ren1 = vtk.vtkRenderer()
	ren1.UseHiddenLineRemovalOn()
	renWin = vtk.vtkRenderWindow()
	renWin.AddRenderer(ren1)
	iren = vtk.vtkRenderWindowInteractor()
	iren.SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())	
	iren.SetRenderWindow(renWin)
	for actor in actor_list:
		ren1.AddActor(actor)
	renWin.SetSize(1800, 1800)
	iren.Initialize()
	renWin.Render()
	iren.Start()
	

actor_in, actor_out = actor_clip()
vtk_show([actor_in, actor_out])
