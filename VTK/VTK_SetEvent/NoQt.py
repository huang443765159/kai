import vtk


def actor_axis():
    actor = vtk.vtkAxesActor()
    actor.SetTotalLength(2, 2, 2)
    actor.SetShaftType(0)
    actor.SetCylinderRadius(0.01)
    actor.GetXAxisCaptionActor2D().SetWidth(0.01)
    actor.GetYAxisCaptionActor2D().SetWidth(0.01)
    actor.GetZAxisCaptionActor2D().SetWidth(0.01)
    return actor

def Cube():
    pass


if __name__ == '__main__':

    camera = vtk.vtkCamera()
    # camera.Yaw(1)
    ren = vtk.vtkRenderer()
    # ren.SetActiveCamera(camera)
    ren_win = vtk.vtkRenderWindow()
    ren_win.AddRenderer(ren)
    i_ren = vtk.vtkRenderWindowInteractor()
    i_ren.SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())
    i_ren.SetNumberOfFlyFrames(1)
    # i_ren.GetInteractorStyle().SetCurrentStyleToTrackballCamera()
    i_ren.SetRenderWindow(ren_win)
    style = vtk.vtkInteractorStyle()
    a = style.OnMouseWheelForward()
    b = style.OnRightButtonDown()
    print(a, b)

    ren.AddActor(actor_axis())
    ren_win.SetSize(1800, 1800)
    i_ren.Initialize()
    i_ren.Start()
