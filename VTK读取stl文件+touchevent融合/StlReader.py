from vtkmodules import all as vtk
import os
print(os.getcwd())


cone = vtk.vtkConeSource()
cone_mapper = vtk.vtkPolyDataMapper()
cone_mapper.SetInputConnection(cone.GetOutputPort())

cone_actor = vtk.vtkActor()
cone_actor.SetMapper(cone_mapper)

stl_actor = vtk.vtkActor()
stl_mapper = vtk.vtkPolyDataMapper()
stl_actor.SetMapper(stl_mapper)
stl = vtk.vtkSTLReader()
stl.SetFileName('Arm.stl')
stl_mapper.SetInputConnection(stl.GetOutputPort())
stl.Update()

ren = vtk.vtkRenderer()
ren.AddActor(cone_actor)
ren.AddActor(stl_actor)
ren.SetBackground(0.5, 0.2, 0.7)

ren_win = vtk.vtkRenderWindow()
ren_win.AddRenderer(ren)
ren_win.SetSize(1000, 1000)
ren_win.Render()

i_ren = vtk.vtkRenderWindowInteractor()
i_ren.SetRenderWindow(ren_win)
i_ren.Initialize()
i_ren.Start()
