from vtkmodules import all as vtk


class Test:

    def __init__(self):
        floor_mapper = vtk.vtkPolyDataMapper()
        floor_mapper.SetInputData(vtk.vtkPolyData())
        self.floor_actor = vtk.vtkActor()
        self.floor_actor.SetMapper(floor_mapper)
        car_mapper = vtk.vtkPolyDataMapper()
        car_mapper.SetInputData(vtk.vtkPolyData())
        self.car_actor = vtk.vtkActor()
        self.car_actor.SetMapper(car_mapper)

    def load_floor_file(self, file_path):
        reader = vtk.vtkSTLReader()
        reader.SetFileName(file_path)
        reader.Update()
        self.floor_actor.GetMapper().SetInputData(reader.GetOutput())

    def load_car_file(self, file_path):
        reader = vtk.vtkSTLReader()
        reader.SetFileName(file_path)
        reader.Update()
        self.car_actor.GetMapper().SetInputData(reader.GetOutput())

    def splicing(self):
        f_center = self.floor_actor.GetCenter()
        c_center = self.car_actor.GetCenter()
        c_h = self.car_actor.GetBounds()[2]
        x = f_center[0] - c_center[0]
        y = 0.07 - c_h
        z = f_center[2] - c_center[2]
        self.car_actor.SetPosition(x, y, z)

    @staticmethod
    def axis():
        actor = vtk.vtkAxesActor()
        actor.SetTotalLength(0.5, 0.5, 0.5)
        actor.SetShaftType(0)
        actor.SetCylinderRadius(0.01)
        actor.GetXAxisCaptionActor2D().SetWidth(0.01)
        actor.GetYAxisCaptionActor2D().SetWidth(0.01)
        actor.GetZAxisCaptionActor2D().SetWidth(0.01)
        return actor


if __name__ == '__main__':
    test = Test()
    test.load_floor_file(file_path='STL/1.stl')
    # test.load_car_file(file_path='STL/FTAlpha2020.stl')
    test.splicing()
    render = vtk.vtkRenderer()
    render.AddActor(test.floor_actor)
    render.AddActor(test.car_actor)
    render.AddActor(test.axis())

    ren_win = vtk.vtkRenderWindow()
    ren_win.AddRenderer(render)
    ren_win.SetSize(2000, 2000)
    ren_win.Render()
    i_ren = vtk.vtkRenderWindowInteractor()
    i_ren.SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())
    i_ren.SetRenderWindow(ren_win)
    i_ren.Start()
