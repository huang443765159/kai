import vtk
import time
import types
import signal
import threading
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt, QEvent, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from QtTouchEvent_New.InteractorStyle import MyEvent


class Test(QMainWindow):

    def __init__(self, window_zoom=0.1):
        super().__init__()
        signal.signal(signal.SIGINT, self.exit)
        # WINDOW
        # self._screen_size = QApplication.primaryScreen().size()
        self.resize(1800, 1200)
        self._center_widget = QWidget(self)
        self._center_widget.setWindowFlags(Qt.NoDropShadowWindowHint)
        self._center_widget.resize(1800, 1200)
        self._vtk_widget = QVTKRenderWindowInteractor(self._center_widget)
        self._vtk_widget.resize(1800, 1200)
        self.setCentralWidget(self._center_widget)
        self._center_widget.setFocus()
        self._ren_win = self._vtk_widget.GetRenderWindow()
        self._interactor = self._ren_win.GetInteractor()
        QApplication.setStyle('Fusion')
        self.setWindowFlags(Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # LABEL_WIDGET
        self._label_widget = QWidget(self._center_widget)
        self._label_widget.resize(300, 200)
        # POS_LABEL
        self._pos_label = QLabel(self._label_widget)
        self._pos_label.move(20, 50)
        self._pos_label.resize(200, 30)
        self._pos_label.setStyleSheet('QLabel {color: red}')
        self._pos_label.setText('pos: ')
        # TOUCH_POINT_LABEL
        self._touch_points = 0
        self._touch_point_label = QLabel(self._label_widget)
        self._touch_point_label.move(20, 80)
        self._touch_point_label.resize(100, 30)
        self._touch_point_label.setStyleSheet('QLabel {color: red}')
        self._touch_point_label.setText('touch points: ')
        self._label_widget.setAttribute(Qt.WA_TranslucentBackground)
        self._label_widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self._label_widget.show()
        # WIDGET
        self._widget = QWidget(self._center_widget)
        self._widget.resize(1800, 1200)
        self._widget.event = types.MethodType(self._handle_event, self._widget)
        self._widget.setAttribute(Qt.WA_AcceptTouchEvents)  # 与半透明分开设置
        # # POS_LABEL
        # self._pos_label = QLabel(self._widget)
        # self._pos_label.move(1500, 50)
        # self._pos_label.resize(250, 30)
        # self._pos_label.setStyleSheet('QLabel {color: red}')
        # self._pos_label.setText('pos: ')
        # # TOUCH_POINT_LABEL
        # self._touch_points = 0
        # self._touch_point_label = QLabel(self._widget)
        # self._touch_point_label.move(1500, 80)
        # self._touch_point_label.resize(100, 30)
        # self._touch_point_label.setStyleSheet('QLabel {color: red}')
        # self._touch_point_label.setText('touch points: ')
        self._timer = QTimer()
        self._widget.setAttribute(Qt.WA_TranslucentBackground)
        self._widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self._widget.show()
        # TIMER
        self._timer.setInterval(int(1000 / 60))
        self._timer.timeout.connect(self._render_once)
        self._timer.start()
        # RENDER
        self._renderer = vtk.vtkOpenGLRenderer()
        self._renderer.SetBackground((0, 0, 0))
        self._renderer.AddActor(self._axis_actor())
        self._ren_win.AddRenderer(self._renderer)
        # CAMERA
        self._camera = self._renderer.GetActiveCamera()
        self._camera_pose = [0, 0, 13]
        self._last_camera_pose = [0, 0, 0]
        self._camera_view = [0, 0, 0]
        self._last_camera_view = [0, 0, 0]
        self.set_camera_pose(pos=[0, 0, 13.0], center=[0, 0, 0], view=[0, 0, 0])
        self._vtk_widget.Start()
        # MOUSE_POS_THREAD
        self._thread_switch = False
        self._mouse_pos = self._widget.mapFromGlobal(QCursor.pos())
        self._last_mouse_pos = self._widget.mapFromGlobal(QCursor.pos())
        self._thread = None

    def _get_mouse_pos(self):
        while self._thread_switch:
            self._mouse_pos = self._widget.mapFromGlobal(QCursor.pos())
            if self._last_mouse_pos != self._mouse_pos:
                move_x = self._mouse_pos.x() - self._last_mouse_pos.x()
                move_y = self._mouse_pos.y() - self._last_mouse_pos.y()
                self._last_mouse_pos = self._mouse_pos
                if move_x > 0:
                    self._camera_pose[0] += 0.05
                elif move_x < 0:
                    self._camera_pose[0] -= 0.05
            time.sleep(1 / 60)

    # @staticmethod
    def _handle_event(self, widget, event):
        if event.type() in [QEvent.TouchBegin, QEvent.TouchUpdate, QEvent.TouchEnd]:
            touch_points = event.touchPoints()
            self._touch_points = len(touch_points)
            print(len(touch_points))
            if len(touch_points) == 1 and touch_points[0].state() == Qt.TouchPointMoved:
                pos = touch_points[0].pos()
                last_pos = touch_points[0].lastPos()
                dif_pos_x = pos.x() - last_pos.x()
                dif_pos_y = pos.y() - last_pos.y()
                if dif_pos_x > 0:
                    self._camera_pose[0] += 0.05
                elif dif_pos_x < 0:
                    self._camera_pose[0] -= 0.05
            elif len(touch_points) == 2:
                if touch_points[0].state() == Qt.TouchPointMoved or touch_points[1].state() == Qt.TouchPointMoved:
                    pos1 = touch_points[0].pos()
                    last_pos1 = touch_points[0].lastPos()
                    pos2 = touch_points[1].pos()
                    last_pos2 = touch_points[1].lastPos()
                    diff_new = pos1 - pos2
                    diff_old = last_pos1 - last_pos2
                    if diff_new.y() - diff_old.y() > 0:
                        self._camera_pose[1] -= 0.05
                    elif diff_new.y() - diff_old.y() < 0:
                        self._camera_pose[1] += 0.05
            elif len(touch_points) == 3:
                if touch_points[0].state() == Qt.TouchPointMoved or touch_points[1].state() == Qt.TouchPointMoved or \
                        touch_points[2].state() == Qt.TouchPointMoved:
                    pos1 = touch_points[0].pos()
                    last_pos1 = touch_points[0].lastPos()
                    pos2 = touch_points[1].pos()
                    last_pos2 = touch_points[1].lastPos()
                    pos3 = touch_points[2].pos()
                    last_pos3 = touch_points[2].lastPos()
                    if pos1.x() - last_pos1.x() > 0:
                        self._camera_pose[0] += 0.05
                    elif pos1.x() - last_pos1.x() < 0:
                        self._camera_pose[0] -= 0.05
                    if pos1.y() - last_pos1.y() > 0:
                        self._camera_pose[1] += 0.05
                    elif pos1.y() - last_pos1.y() < 0:
                        self._camera_pose[1] -= 0.05
            elif len(touch_points) == 4:
                pass
            elif len(touch_points) == 5:
                pass
        elif event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.LeftButton:
                self._thread_switch = True
                self._thread = threading.Thread(target=self._get_mouse_pos)
                self._thread.daemon = True
                self._thread.start()
        elif event.type() == QEvent.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                self._thread_switch = False
        widget.update()
        return True

    # CAMERA
    def set_camera_pose(self, pos, center, view):
        self._camera.SetPosition(pos)
        self._camera.SetFocalPoint(center)
        self._camera.SetViewUp(view)
        self._render_once()

    def _render_once(self):
        self._touch_point_label.setText(f'touch points: {self._touch_points}')
        for idx, pos in enumerate(self._last_camera_pose):
            if self._last_camera_pose[idx] != self._camera_pose[idx]:
                self._last_camera_pose[idx] = self._camera_pose[idx]
                self._pos_label.setText(f'pos: {round(self._camera_pose[0], 2)}  {round(self._camera_pose[1], 2)}  '
                                        f'{round(self._camera_pose[2], 2)}')
                self._camera.SetPosition(self._camera_pose)
                self._interactor.Render()
            if self._last_camera_view[idx] != self._camera_view[idx]:
                self._last_camera_view[idx] = self._camera_view[idx]
                self._camera.SetViewUp(self._camera_view)
                self._interactor.Render()

    def mousePressEvent(self, event):
        print('mouse pressed')

    def mouseReleaseEvent(self, event):
        print('mouse release')

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

    def exit(self, signum=None, frame=None):
        self._ren_win.GetInteractor().DestroyTimer()
        self._timer.stop()
        self.close()

    def test(self):
        self._touch_points += 1
        self._pos_label.setText(f'{self._touch_points}')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setOverrideCursor(Qt.BlankCursor)
    test = Test()
    test.show()
    sys.exit(app.exec_())
