import vtk


class MyEvent(vtk.vtkInteractorStyleMultiTouchCamera):

    def __init__(self, parent=None):
        self.AddObserver("MiddleButtonPressEvent", self.middle_button_press_event)
        self.AddObserver("MiddleButtonReleaseEvent", self.middle_button_release_event)
        self.AddObserver("LeftButtonPressEvent", self.left_button_press_event)
        self.AddObserver("LeftButtonReleaseEvent", self.left_button_release_event)
        self.AddObserver("RightButtonPressEvent", self.right_button_press_event)
        self.AddObserver("RightButtonReleaseEvent", self.right_button_release_event)
        self.AddObserver("MouseWheelForwardEvent", self.mouse_wheel_forward)
        self.AddObserver("MouseWheelBackwardEvent", self.mouse_wheel_backward)
        # self.AddObserver("MouseMoveEvent", self.mouse_move_event)

    def middle_button_press_event(self, obj, event):
        print("Middle Button pressed")
        self.OnMiddleButtonDown()
        return

    def middle_button_release_event(self, obj, event):
        print("Middle Button released")
        self.OnMiddleButtonUp()
        return

    def left_button_press_event(self, obj, event):
        print("Left Button pressed")
        self.OnLeftButtonDown()
        return

    def left_button_release_event(self, obj, event):
        print("Left Button released")
        self.OnLeftButtonUp()
        return

    def right_button_press_event(self, obj, event):
        print("right Button pressed")
        self.OnRightButtonDown()
        return

    def right_button_release_event(self, obj, event):
        print("right Button released")
        self.OnLeftButtonUp()
        return

    def mouse_wheel_forward(self, obj, event):
        self.Rotate()
        print("mouse wheel forward")
        return

    def mouse_wheel_backward(self, obj, event):
        print("mouse wheel backward")
        return

    def mouse_move_event(self, obj, event):
        self.OnRightButtonDown()

    def axes(self):
        axes_actor = vtk.vtkAxesActor()
        axes_actor.SetTotalLength(2, 2, 2)
        axes_actor.SetShaftType(1)
        axes_actor.SetCylinderRadius(0.01)
        axes_actor.GetXAxisCaptionActor2D().SetWidth(0.01)
        axes_actor.GetYAxisCaptionActor2D().SetWidth(0.01)
        axes_actor.GetZAxisCaptionActor2D().SetWidth(0.01)
        return axes_actor


if __name__ == '__main__':
    ren = vtk.vtkRenderer()
    ren.AddActor(MyEvent().axes())
    ren_win = vtk.vtkRenderWindow()
    ren_win.AddRenderer(ren)
    i_ren = vtk.vtkRenderWindowInteractor()
    i_ren.SetRenderWindow(ren_win)
    i_ren.SetInteractorStyle(MyEvent())
    style = vtk.vtkInteractorStyle()

    ren_win.SetSize(1800, 1800)
    i_ren.Initialize()
    i_ren.Start()

