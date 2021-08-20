from vtkmodules import all as vtk

file1 = 'STL/AudiA42017.stl'
file2 = 'STL/House.stl'


class Test:

    def __init__(self):
        stl_writer = vtk.vtkSTLWriter()
        append_poly = vtk.vtkAppendPolyData()

        reader1 = vtk.vtkSTLReader()
        reader1.SetFileName(file1)
        reader1.Update()
        reader2 = vtk.vtkSTLReader()
        reader2.SetFileName(file2)
        reader2.Update()

        mapper1 = vtk.vtkPolyDataMapper()
        mapper1.SetInputData(vtk.vtkPolyData())
        mapper2 = vtk.vtkPolyDataMapper()
        mapper2.SetInputData(vtk.vtkPolyData())

        actor1 = vtk.vtkActor()
        actor1.SetMapper(mapper1)
        actor2 = vtk.vtkActor()
        actor2.SetMapper(mapper2)

        actor1.GetMapper().SetInputData(reader1.GetOutput())
        actor2.GetMapper().SetInputData(reader2.GetOutput())

        h_center = actor2.GetCenter()
        c_center = actor1.GetCenter()
        c_h = actor1.GetBounds()[2]
        x = h_center[0] - c_center[0]
        y = 0.07 - c_h
        z = h_center[2] - c_center[2]
        actor1.SetPosition(x, y, z)

        # append_poly.AddInputData(reader1.GetOutput())
        # append_poly.AddInputData(reader2.GetOutput())
        reader1.FastDelete()
        reader2.FastDelete()

        render = vtk.vtkRenderer()
        ren_win = vtk.vtkRenderWindow()
        ren_win.AddRenderer(render)
        ren_win.SetSize(2000, 2000)
        i_ren = vtk.vtkRenderWindowInteractor()
        i_ren.SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())
        i_ren.SetRenderWindow(ren_win)
        render.AddActor(actor1)
        render.AddActor(actor2)
        ren_win.Render()

        actors = render.GetActors()
        actor_items = actors.GetNumberOfItems()
        actors.InitTraversal()
        for i in range(actor_items):
            actor = actors.GetNextActor()
            position = list(actor.GetPosition())
            actor.SetPosition(position[0], position[1], position[2])
            mapper = actor.GetMapper()
            poly = mapper.GetInput()
            if position != (0, 0, 0):  # 如果发生平移则把每个点的坐标都做一下平移
                points = poly.GetPoints()
                sum_pts = points.GetNumberOfPoints()
                for x in range(sum_pts):
                    pos_point = list(points.GetPoint(x))
                    for y in range(3):
                        pos_point[y] += position[y]
                        points.SetPoint(x, pos_point)
            append_poly.AddInputData(poly)
            append_poly.Update()

        filter = vtk.vtkTriangleFilter()
        filter.SetInputConnection(append_poly.GetOutputPort())
        stl_writer.SetFileName('STL/1.stl')
        stl_writer.SetInputConnection(filter.GetOutputPort())
        stl_writer.Update()
        stl_writer.Write()

        i_ren.Start()


if __name__ == '__main__':
    test = Test()
