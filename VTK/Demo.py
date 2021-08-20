import vtk

'''
数据源                 vtk.vtkConeSource()
映射器                 vtkPolyDataMapper()
映射器添加数据源         SetInputConnection(Cone.GetOutputPort())
演员                   vtk.vtkActor()
演员添加映射器           SetMapper(mapper)
渲染器                 vtk.vtkRenderer()
渲染器添加演员           AddActor(actor)
渲染窗口                vtk.vtkRendererWindow()
渲染窗口添加渲染器--生成图形  AddRenderer(renderer)
渲染窗口读取图形         .Renderer()
渲染窗口交互器           vtk.vtkRendererWindowInteractor()
交互器添加渲染窗口        SetRendererWindow(ren_win)
交互器初始化             Initialize()
交互器开始              start()
'''
cone = vtk.vtkConeSource()
cone_mapper = vtk.vtkPolyDataMapper()
cone_mapper.SetInputConnection(cone.GetOutputPort())

cone_actor = vtk.vtkActor()
cone_actor.SetMapper(cone_mapper)

ren = vtk.vtkRenderer()
ren.AddActor(cone_actor)
ren.SetBackground(0.5, 0.2, 0.7)

ren_win = vtk.vtkRenderWindow()
ren_win.AddRenderer(ren)
ren_win.SetSize(1000, 1000)
ren_win.Render()

i_ren = vtk.vtkRenderWindowInteractor()
i_ren.SetRenderWindow(ren_win)
i_ren.Initialize()
i_ren.Start()
