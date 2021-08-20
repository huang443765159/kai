import vtk
import sys
sys.path.append('Desktop/')
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from VTK.UI.UI import Ui_MainWindow
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class VTK(QMainWindow):

    def __init__(self):
        super().__init__()
        self._vtk_widget = QVTKRenderWindowInteractor()
        self._renderer = vtk.vtkRenderer()
        self._renderer_win = self._vtk_widget.GetRenderWindow()
        self._renderer_win.AddRenderer(self._renderer)
        self._renderer_win.GetInteractor().SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())

        self._renderer_win.GetInteractor().AddObserver('TimerEvent', self._render_timer)
        self._renderer_win.GetInteractor().CreateRepeatingTimer(1000)

        self._renderer.AddActor(self.axes())
        self._renderer_win.GetInteractor().Initialize()
        self._vtk_widget.Start()
        self._vtk_widget.showFullScreen()

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 半透明
        self.move(20, int((QApplication.primaryScreen().size().height() - self.size().height()) / 2) ) # 距离左侧20中心

        self._ui.btn_add_sphere.clicked.connect(lambda: self._renderer.AddActor(self.sphere_actor()))
        self._ui.btn_quit.clicked.connect(self.exit)
        self._ui.btn_add_line.clicked.connect(lambda: self._renderer.AddActor(self.line()))
        # self._ui.btn_remove_line.clicked.connect(lambda: self._renderer.RemoveActor(self.sphere_actor()))
        self._ui.btn_remove_line.clicked.connect(lambda: self._renderer.AddActor(self.remove_line()))
        self._line = None

    def sphere_actor(self):
        sphere = vtk.vtkSphereSource()
        sphere.SetCenter(random.random(), random.random(), random.random())
        sphere.SetRadius(0.1)
        sphere.SetPhiResolution(100)
        sphere.SetThetaResolution(100)
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(sphere.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(random.random(), random.random(), random.random())
        return actor

    def axes(self):
        axes_actor = vtk.vtkAxesActor()
        axes_actor.SetTotalLength(2, 2, 2)
        axes_actor.SetShaftType(1)
        axes_actor.SetCylinderRadius(0.01)
        axes_actor.GetXAxisCaptionActor2D().SetWidth(0.01)
        axes_actor.GetYAxisCaptionActor2D().SetWidth(0.01)
        axes_actor.GetZAxisCaptionActor2D().SetWidth(0.01)
        return axes_actor

    def line(self):
        line = vtk.vtkLineSource()
        self._line = line
        p0 = [1.0, 0.0, 0.0]
        p1 = [1.0, 0.0, 2.0]
        line.SetPoint1(p0)
        line.SetPoint2(p1)
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(line.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(1, 1, 0)
        actor.GetProperty().SetLineWidth(2)
        return actor

    def remove_line(self):
        p3 = [1.0, 0.0, 0.0]
        p4 = [1.0, 0.0, 0.5]
        self._line.SetPoint1(p3)
        self._line.SetPoint2(p4)
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(self._line.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(1, 1, 0)
        actor.GetProperty().SetLineWidth(2)
        return actor

    def _render_timer(self, obj, event):
        obj.GetRenderWindow().Render()

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
