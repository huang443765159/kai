from vtkmodules import all
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from PyQt5.QtCore import Qt
from _VtkPoints import VtkPoints
from VTK.VtkPoints._VtkLine import VtkLine


class PointsShow(QMainWindow):

    def __init__(self):
        super(PointsShow, self).__init__()
        self._screen_size = QApplication.primaryScreen().size()
        # WIDGET
        self._widget = QWidget(self)
        self._widget.setAttribute(Qt.WA_TranslucentBackground)
        self.setCentralWidget(self._widget)
        self._widget.resize(self._screen_size)
        # VTK
        self._vtk_widget = QVTKRenderWindowInteractor(self._widget)
        self._vtk_widget.SetInteractorStyle(all.vtkInteractorStyleMultiTouchCamera())
        self._vtk_widget.resize(self._screen_size)
        self._ren_win = self._vtk_widget.GetRenderWindow()
        self._render = all.vtkRenderer()
        sw, sh = self._screen_size.width(), self._screen_size.height()
        self.resize(int(sw * 0.9), int(sh * 0.9))
        self.move(int(sw * (1 - 0.8) / 2), int(sh * (1 - 0.8) / 2))
        # POINTS
        self._points = VtkPoints(size=3, opacity=1)
        self._render.AddActor(self._points.actor)
        # LINE
        self._lines = VtkLine(color=(1, 0, 0), width=4)
        self._lines.set_point([0.0, 0.0, 0.0])
        self._lines.set_point([1.0, 0.0, 0.0])
        self._lines.set_line(0, 0)
        self._render.AddActor(self._lines.actor)
        # COPY_FUN
        self.add_points = self._points.add_points
        self.set_color = self._points.set_color
        # SHOW
        self._ren_win.AddRenderer(self._render)
        self._vtk_widget.Start()
        self._render.Render()

    def render_once(self):
        self._vtk_widget.Render()


if __name__ == '__main__':
    import sys
    import random
    app = QApplication(sys.argv)
    test = PointsShow()
    points1 = list()
    for i in range(1000):
        one_point = [random.random(), random.random(), random.random()]
        points1.append(one_point)
    test.add_points(points1)
    test.render_once()

    # POINTS2
    points2 = list()
    for i in range(100):
        one_point = [random.random(), random.random(), random.random()]
        points2.append(one_point)
    test.add_points(points2)
    test.set_color(color=None, rgb_list=[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))])
    test.show()
    sys.exit(app.exec_())
