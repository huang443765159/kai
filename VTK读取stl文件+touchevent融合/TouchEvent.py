import sys
sys.path.append('Desktop/')
import vtk
import types
import signal
from math import atan, degrees, pi
from PyQt5.QtCore import Qt, QEvent, QTimer, QPointF
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QToolBox
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from TouchEvent_V1.InteractorStyle import InteractorStyle
# from VTK读取stl文件+touchevent融合.test import One

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
        # WIDGET
        self._widget = QWidget(self)
        self.setCentralWidget(self._widget)
        self.resize(900, 900)
        self._widget.event = types.MethodType(self._handle_event, self._widget)
        self._widget.setAttribute(Qt.WA_AcceptTouchEvents | Qt.WA_TranslucentBackground)
        self._widget.setWindowFlags(Qt.NoDropShadowWindowHint)
        # VTK
        self._vtk_widget = QVTKRenderWindowInteractor(self._widget)
        self._vtk_widget.resize(900, 900)
        self._ren_win = self._vtk_widget.GetRenderWindow()
        self._interactor = self._ren_win.GetInteractor()
        self._vtk_widget.SetInteractorStyle(InteractorStyle())
        # # TEST_WIDGET
        self._test_widget = QWidget(self)
        self._test_widget.resize(300, 300)
        self._test_widget.setStyleSheet('QWidget {background: rgb(60, 60, 60)}')
        # TEST_BTN
        self._button = QPushButton(self._test_widget)
        self._button.setText('test')
        self._button.setStyleSheet('QPushButton {background: rgb(255, 255, 255)}')
        self._button.pressed.connect(self._pressed)
        self._button.released.connect(self._released)
        self._button.resize(100, 30)
        self._button.move(100, 200)
        self._test_widget1 = QToolBox(self._test_widget)
        self._test_widget1.resize(100, 100)
        self._test_widget1.show()
        self._button.show()
        self._test_widget.show()

        # RENDER
        self._renderer = vtk.vtkOpenGLRenderer()
        self._renderer.SetBackground((0, 0, 0))
        self._renderer.AddActor(self._axis_actor())
        for actor in self._stl_actor().values():
            self._renderer.AddActor(actor)
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
            self._touch_point_number = len(touch_points)
            print(self._touch_point_number)
            if self._touch_point_number == 1:
                lpt = touch_points[0].lastNormalizedPos()  # 获取相对距离
                pt = touch_points[0].normalizedPos()
                dpt = pt - lpt
                self._camera.Azimuth(-dpt.x() * S_P1)  # 物体视觉上旋转与相机相反，为了逻辑符合，应取负值
                self._camera.Elevation(dpt.y() * S_P1)
            elif self._touch_point_number == 2:
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
            elif self._touch_point_number == 3:
                lpt = QPointF()
                pt = QPointF()
                for point in touch_points:
                    lpt += point.lastNormalizedPos()
                    pt += point.normalizedPos()
                dpt = pt - lpt
                self._camera.Yaw(dpt.x() * S_P3)
                self._camera.Pitch(dpt.y() * S_P3)
        # widget.update()
        return True

    def _render_once(self):
        self._interactor.Render()

    def _pressed(self):
        self._test_widget1.setStyleSheet('QToolBox {background-color: rgb(255, 0, 0)}')
        self._test_widget1.setVisible(True)
        self._button.setText('Pressed')

    def _released(self):
        self._test_widget1.setVisible(False)
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
        stls = dict()
        actors = dict()
        mappers = dict()
        for i, stl in enumerate(['/home/xyz/Desktop/VTK读取stl文件+touchevent融合/Board.stl', '/home/xyz/Desktop/VTK读取stl文件+touchevent融合/Arm.stl']):
            actors[i] = vtk.vtkActor()
            mappers[i] = vtk.vtkPolyDataMapper()
            actors[i].SetMapper(mappers[i])
            stls[i] = vtk.vtkSTLReader()
            stls[i].SetFileName(stl)
            mappers[i].SetInputConnection(stls[i].GetOutputPort())
            stls[i].Update()
        return actors

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
