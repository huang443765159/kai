import sys
from platform import platform
if 'generic' in platform():
    sys.path.append('Desktop/')
import vtk
import types
import signal
from math import atan, degrees, pi
from PyQt5.QtCore import Qt, QEvent, QTimer, QPointF
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QToolBox
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from QtTouchEvent_2020101006PM.VTK.InteractorStyle import InteractorStyle

S_P1 = 180
S_P3 = 40


def get_angle(pt: QPointF):
    # 范围为0~2pi
    dx = pt.x()
    dy = pt.y()
    if dx == 0 and dy == 0:
        # print("\033[1;31;m", "WARNING, compare same points", )
        return None
    if dx == 0:
        return pi / 2 if dy > 0 else pi * 3 / 2
    if dy == 0:
        return 0 if dx > 0 else pi
    angle = atan(dy / dx)
    if dx < 0:
        angle += pi
    elif dx > 0 and dy < 0:
        angle += 2 * pi
    return angle


class Test(QMainWindow):

    def __init__(self):
        super().__init__()
        signal.signal(signal.SIGINT, self.exit)
        self._screen_size = QApplication.primaryScreen().size()
        # WIDGET
        self._widget = QWidget(self)
        self.setCentralWidget(self._widget)
        self._widget.resize(self._screen_size)
        self._widget.event = types.MethodType(self._handle_event, self._widget)
        self._widget.setAttribute(Qt.WA_AcceptTouchEvents | Qt.WA_TranslucentBackground)
        self._widget.setWindowFlags(Qt.NoDropShadowWindowHint)
        # VTK
        self._vtk_widget = QVTKRenderWindowInteractor(self._widget)
        self._vtk_widget.resize(self._screen_size)
        self._ren_win = self._vtk_widget.GetRenderWindow()
        self._interactor = self._ren_win.GetInteractor()
        self._vtk_widget.SetInteractorStyle(InteractorStyle())
        self._sw, self._sh = self._screen_size.width(), self._screen_size.height()
        self.resize(int(self._sw * 0.7), int(self._sh * 0.7))
        self.move(int(self._sw * (1 - 0.7) / 2), int(self._sh * (1 - 0.7) / 2))
        # STYLE
        self._widget.setFocus()
        QApplication.setStyle('Fusion')
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # 开启touch事件之后
        # QMainWindow不可开启此方法，会把子类所有插件变透明，且报qt.qpa.xcb: QXcbConnection: XCB error: 8 (BadMatch) 错误
        # TEST_DOCK
        self._dock = QWidget(self)
        self._dock.resize(70, 150)
        self._dock.move(int(self._sw * 0.7 - 80), 100)
        self._dock.setStyleSheet('QWidget {background: rgb(60, 60, 60)}')
        self._dock.show()
        # TEST_BTN
        self._button = QPushButton(self._dock)
        self._button.setText('test')
        self._button.setStyleSheet('QPushButton {background: rgb(255, 255, 255)}')
        self._button.pressed.connect(self._pressed)
        self._button.released.connect(self._released)
        self._button.resize(60, 60)
        self._button.move(5, 5)
        self._button.show()
        # TEST_PANEL
        self._bar = QWidget(self)
        self._bar.resize(340, 450)
        self._bar.move(int(self._sw * 0.7 - 425), 100)
        self._bar.show()
        self._bar.setVisible(False)
        # TEST_TOOL_BOX
        self._tool_box = QToolBox(self._bar)
        self._tool_box.resize(340, 450)
        self._tool_box.show()
        # RENDER
        self._renderer = vtk.vtkOpenGLRenderer()
        self._renderer.SetBackground((0, 0, 0))
        self._renderer.AddActor(self._axis_actor())
        self._renderer.AddActor(self._stl_actor())
        self._camera = self._renderer.GetActiveCamera()
        self._ren_win.AddRenderer(self._renderer)
        self._ren_win.Render()
        # CAMERA
        self._camera = self._renderer.GetActiveCamera()
        self._camera.SetPosition(13, 0, 0)
        self._vtk_widget.Start()
        # TIMER
        self._timer = QTimer()
        self._timer.setInterval(int(1000 / 60))
        self._timer.timeout.connect(self._render_once)
        self._timer.start()

    def _handle_event(self, widget, event):
        if event.type() in [QEvent.TouchBegin, QEvent.TouchUpdate, QEvent.TouchEnd]:
            touch_points = event.touchPoints()
            touch_point_number = len(touch_points)
            print(touch_point_number)
            if touch_point_number == 1:
                lpt = touch_points[0].lastNormalizedPos()  # 获取相对距离
                pt = touch_points[0].normalizedPos()
                dpt = pt - lpt
                self._camera.Azimuth(-dpt.x() * S_P1)  # 物体视觉上旋转与相机相反，为了逻辑符合，应取负值
                self._camera.Elevation(dpt.y() * S_P1)
                self._camera.OrthogonalizeViewUp()  # 屏蔽90度半球跳转问题
            elif touch_point_number == 2:
                if 'generic' in platform():
                    lpt0 = touch_points[0].lastNormalizedPos()
                    pt0 = touch_points[0].normalizedPos()
                    lpt1 = touch_points[1].lastNormalizedPos()
                    pt1 = touch_points[1].normalizedPos()
                    ldpt = lpt0 - lpt1
                    dpt = pt0 - pt1
                    # 缩放
                    ldis = ldpt.manhattanLength()  # 上一次两点间距
                    dis = dpt.manhattanLength()  # 本次两点间距
                    ddis = dis - ldis
                    scale = 1 + ddis if ddis > 0 else 1 / (1 - ddis)  # 根据距离差计算缩放
                    self._camera.Dolly(scale)
                    # 旋转
                    la = get_angle(ldpt)
                    a = get_angle(dpt)
                    da = a - la
                    self._camera.Roll(-degrees(da))  # 物体视觉上旋转与相机相反，为了逻辑符合，应取负值
            elif touch_point_number == 3:
                lpt = QPointF()
                pt = QPointF()
                for point in touch_points:
                    lpt += point.lastNormalizedPos()
                    pt += point.normalizedPos()
                dpt = pt - lpt
                self._camera.Yaw(dpt.x() * S_P3)
                self._camera.Pitch(dpt.y() * S_P3)
        widget.update()
        return True

    def _render_once(self):
        self._interactor.Render()

    def _pressed(self):
        self._tool_box.setStyleSheet('QToolBox {background-color: rgba(30, 30, 30, 1)}')
        self._bar.setVisible(True)
        self._button.setText('Pressed')

    def _released(self):
        self._bar.setVisible(False)
        self._button.setText('Released')


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

    def _stl_actor(self):
        actor = vtk.vtkActor()
        mapper = vtk.vtkPolyDataMapper()
        actor.SetMapper(mapper)
        stl = vtk.vtkSTLReader()
        if 'generic' in platform():
            stl.SetFileName('/home/xyz/Desktop/QtTouchEvent_2020101006PM/VTK/Board.stl')
        else:
            stl.SetFileName('VTK/Board.stl')
        mapper.SetInputConnection(stl.GetOutputPort())
        stl.Update()
        return actor

    def exit(self, signum=None, frame=None):
        self._ren_win.GetInteractor().DestroyTimer()
        self._timer.stop()
        self.close()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setOverrideCursor(Qt.BlankCursor)
    test = Test()
    test.show()
    sys.exit(app.exec_())
