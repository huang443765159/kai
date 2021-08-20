from vtkmodules import all
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from VTKLed._point import Point


class Vtk(QMainWindow):

    def __init__(self):
        super(Vtk, self).__init__()
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
        self._points = Point(pos=(10, 10, 10), size=1, color=(100, 0, 0))
        self._render.AddActor(self._points.actor)
        for column in range(1):
            for row in range(1):
                self._points.points.InsertNextPoint(row * 0.125, 1 - column * 0.016, 0)
        self._points.points.Modified()
        # VTK_SHOW
        self._ren_win.AddRenderer(self._render)
        self._vtk_widget.Start()
        self._render.Render()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    nuc = Vtk()
    nuc.show()
    sys.exit(app.exec_())
