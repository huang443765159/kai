import sys
sys.path.append('Desktop/')
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QEvent, QTimer
import types
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from QtTouchEvent_New.InteractorStyle import MyEvent


class Test(QMainWindow):

    def __init__(self):
        super().__init__()
        # WIDGET
        self._widget = QWidget(self)
        self._widget.setAttribute(Qt.WA_TranslucentBackground | Qt.SubWindow)
        self.setCentralWidget(self._widget)
        self.resize(900, 900)
        self._widget.event = types.MethodType(self._handle_event, self._widget)
        self._widget.setAttribute(Qt.WA_AcceptTouchEvents)  # 与半透明分开设置
        # VTK
        self._vtk_widget = QVTKRenderWindowInteractor(self._widget)
        self._vtk_widget.resize(900, 900)
        self._ren_win = self._vtk_widget.GetRenderWindow()
        # CAMERA
        self._interactor = self._ren_win.GetInteractor()
        self._vtk_widget.SetInteractorStyle(MyEvent())
        # RENDER
        self._renderer = vtk.vtkOpenGLRenderer()
        self._renderer.SetBackground((0, 0, 0))
        self._renderer.AddActor(self._axis_actor())
        self._ren_win.AddRenderer(self._renderer)
        # CAMERA
        self._camera = self._renderer.GetActiveCamera()
        # self._camera_angle = self._camera.GetViewAngle()
        # self._camera_last_angle = 30
        self._camera_pose = [0, 0, 13]
        self._last_camera_pose = [0, 0, 0]
        self.set_camera_pose(pos=[0, 0, 13.0], center=[0, 0, 0], view=[0, 0, 0])
        self._vtk_widget.Start()
        # BUTTON WIDGET
        widget = QWidget(self._widget)
        widget.resize(200, 200)
        widget.setStyleSheet('QWidget {background: red}')
        widget.setToolTip('button test')
        widget.show()
        button = QPushButton(widget)
        button.setStyleSheet('QPushButton {background: blue}')
        button.setText('test')
        button.pressed.connect(self._widget_display)
        button.show()
        # TIMER
        self._event_ena = False
        self._timer = QTimer(self)
        self._timer.setInterval(int(1000/100))
        self._timer.timeout.connect(self._detect_event)
        self._timer.start()
        self._high_timer = QTimer(self)
        self._high_timer.setInterval(int(1000/60))
        self._high_timer.timeout.connect(self._render_once)

    def _widget_display(self):
        widget = QWidget(self._widget)
        widget.resize(400, 400)
        widget.move(300, 0)
        widget.setStyleSheet('QWidget {background: rgba(30, 30, 30, 0.5)}')
        widget.show()
        button = QPushButton(widget)
        button.setStyleSheet('QPushButton {background: rgba(255, 255, 255, 0.5)}')
        button.setText('1234567876543245654345654')
        button.show()
        button.clicked.connect(lambda: widget.setVisible(False))

    # @staticmethod
    def _handle_event(self, widget, event):
        if event.type() in [QEvent.TouchBegin, QEvent.TouchUpdate, QEvent.TouchEnd]:
            touch_points = event.touchPoints()
            # print(len(touch_points))
            if len(touch_points) == 1:
                print(1)
            elif len(touch_points) == 2:
                # self._camera.Zoom(1.01)
                self._camera_pose[2] -= 0.03
            elif len(touch_points) == 3:
                # self._camera.Zoom(0.99)
                self._camera_pose[2] += 0.03
            if event.type() == QEvent.TouchBegin:
                self._event_ena = True
            elif event.type() == QEvent.TouchEnd:
                self._event_ena = False
        widget.update()
        return True

    # CAMERA
    def set_camera_pose(self, pos, center, view):
        self._camera.SetPosition(pos)
        self._camera.SetFocalPoint(center)
        self._camera.SetViewUp(view)
        # self._render_once()

    def _detect_event(self):
        if self._event_ena:
            self._high_timer.start()
            self._timer.stop()
        else:
            self._high_timer.stop()
            self._timer.start()

    def _render_once(self):
        if self._last_camera_pose[2] != self._camera_pose[2]:
            self._last_camera_pose[2] = self._camera_pose[2]
            print(1)
            self._camera.SetPosition(self._camera_pose)
            self._interactor.Render()

    @staticmethod
    def _axis_actor():
        actor = vtk.vtkAxesActor()
        actor.SetTotalLength(2, 2, 2)
        actor.SetShaftType(0)
        actor.SetCylinderRadius(0.01)
        actor.GetXAxisCaptionActor2D().SetWidth(0.01)
        actor.GetYAxisCaptionActor2D().SetWidth(0.01)
        actor.GetZAxisCaptionActor2D().SetWidth(0.01)
        return actor


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setOverrideCursor(Qt.BlankCursor)
    test = Test()
    test.show()
    sys.exit(app.exec_())