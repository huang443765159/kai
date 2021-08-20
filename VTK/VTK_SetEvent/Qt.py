import vtk
import sys
sys.path.append("Desktop/")
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from VTK.VTK_SetEvent.UI.UI import Ui_MainWindow
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from VTK.VTK_SetEvent.test_v2 import MyEvent


class VTK(QMainWindow):

    def __init__(self):
        super().__init__()
        self._vtk_widget = QVTKRenderWindowInteractor()
        self._renderer = vtk.vtkRenderer()
        self._renderer_win = self._vtk_widget.GetRenderWindow()
        self._renderer_win.AddRenderer(self._renderer)
        self._renderer_win.GetInteractor().SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())
        # self._vtk_widget.SetInteractorStyle(MyEvent())

        self._renderer.AddActor(self.axes())
        self._renderer_win.GetInteractor().Initialize()
        self._vtk_widget.Start()
        self._vtk_widget.showFullScreen()

        # axesActor = vtk.vtkAxesActor()
        # axes = vtk.vtkOrientationMarkerWidget()
        # axes.SetOrientationMarker(axesActor)
        # axes.SetInteractor(self._vtk_widget)
        # axes.EnabledOn()
        # axes.InteractiveOn()

        self._screen_size = QApplication.primaryScreen().size()

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.resize(self._screen_size)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 半透明
        self.move(20, int((QApplication.primaryScreen().size().height() - self.size().height()) / 2))  # 距离左侧20中心

        self._ui.btn_add_sphere.clicked.connect(lambda: self._renderer.AddActor(self.sphere_actor()))
        self._ui.btn_quit.clicked.connect(self.exit)
        self._ui.btn_add_line.clicked.connect(lambda: self._renderer.AddActor(self.line()))
        self._ui.btn_remove_line.clicked.connect(lambda: self._renderer.AddActor(self.remove_line()))

    def axes(self):
        axes_actor = vtk.vtkAxesActor()
        axes_actor.SetTotalLength(2, 2, 2)
        axes_actor.SetShaftType(1)
        axes_actor.SetCylinderRadius(0.01)
        axes_actor.GetXAxisCaptionActor2D().SetWidth(0.01)
        axes_actor.GetYAxisCaptionActor2D().SetWidth(0.01)
        axes_actor.GetZAxisCaptionActor2D().SetWidth(0.01)
        return axes_actor

    def mouse_wheel_forward(self, obj, event):
        print('mouse wheel forward')
        self.OnRightButtonUp()

    def mouse_wheel_backward(self, obj, event):
        self.OnRightButtonDown()

    def exit(self):
        self._renderer_win.WaitForCompletion()
        self._renderer_win.GetInteractor().DestroyTimer()
        self._vtk_widget.close()
        self.close()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    _vtk = VTK()
    _vtk.show()

    sys.exit(app.exec_())
