import vtk


class InteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera):

    def __init__(self, parent=None):
        self.AddObserver("MiddleButtonPressEvent", self.middle_button_press_event)
        self.AddObserver("MiddleButtonReleaseEvent", self.middle_button_release_event)
        self.AddObserver("LeftButtonPressEvent", self.left_button_press_event)
        self.AddObserver("LeftButtonReleaseEvent", self.left_button_release_event)
        self.AddObserver("RightButtonPressEvent", self.right_button_press_event)
        self.AddObserver("RightButtonReleaseEvent", self.right_button_release_event)
        self.AddObserver("MouseWheelForwardEvent", self.mouse_wheel_forward)
        self.AddObserver("MouseWheelBackwardEvent", self.mouse_wheel_backward)
        # self.AddObserver("MouseMoveEvent", self.mouse_move_event)  # 屏蔽所有鼠标事件信号

    def middle_button_press_event(self, obj, event):
        # print("Middle Button pressed")
        self.OnMiddleButtonDown()
        return

    def middle_button_release_event(self, obj, event):
        # print("Middle Button released")
        self.OnMiddleButtonUp()
        return

    def left_button_press_event(self, obj, event):
        self.OnLeftButtonDown()
        return

    def left_button_release_event(self, obj, event):
        # print("Left Button released")
        self.OnLeftButtonUp()
        return

    def right_button_press_event(self, obj, event):
        # print("right Button pressed")
        self.OnRightButtonDown()
        return

    def right_button_release_event(self, obj, event):
        # print("right Button released")
        self.OnRightButtonDown()
        return

    def mouse_wheel_forward(self, obj, event):
        # print("mouse wheel forward")
        return

    def mouse_wheel_backward(self, obj, event):
        # print("mouse wheel backward")
        return

    def mouse_move_event(self, obj, event):
        return
        # self.OnRightButtonDown()
