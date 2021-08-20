import vtk
import sys
sys.path.append('Desktop/')
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class VTK(QMainWindow):

    def __init__(self):
        super().__init__()
        # WINDOW
        self._widget = QWidget(self)
        self._widget.resize(500, 500)
        self.resize(500, 500)
        self.setCentralWidget(self._widget)
        self._widget.setAttribute(Qt.WA_AcceptTouchEvents | Qt.WA_TranslucentBackground)
        self._widget.setWindowFlags(Qt.NoDropShadowWindowHint)
        # VTK
        self._vtk_widget = QVTKRenderWindowInteractor(self._widget)
        self._vtk_widget.SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())
        self._vtk_widget.resize(500, 500)
        # WIDGET
        self._widget1 = QWidget(self._widget)
        self._widget1.resize(100, 100)
        self._widget1.setStyleSheet('background-color: rgba(120, 120, 120, 100)')
        self._widget1.move(100, 100)
        self._test_btn1 = QPushButton('jaiodhjiajd1', self._widget1)
        self._test_btn1.resize(70, 30)
        self._test_btn1.move(50, 30)
        self._test_btn1.show()
        self._widget2 = QWidget(self._widget)
        self._widget2.resize(100, 100)
        self._widget2.setStyleSheet('background-color: rgba(120, 120, 120, 100)')
        self._test_btn2 = QPushButton('sdoijajdiada', self._widget2)
        self._test_btn2.resize(70, 30)
        self._test_btn2.move(50, 50)
        self._widget2.move(150, 150)
        self._widget2.show()
        # UI
        self._btn = QPushButton('btn1', self._widget)
        self._btn.resize(30, 30)
        self._btn.move(300, 280)
        self._btn.clicked.connect(self._set_widget1_visible)
        self._btn.show()
        self._btn2 = QPushButton('btn2', self._widget)
        self._btn2.resize(30, 30)
        self._btn2.move(300, 300)
        self._btn2.clicked.connect(self._set_widget2_visible)
        self._btn2.show()
        # ATTR
        self._a = False
        self._b = False
        # RENDER
        self._render = vtk.vtkRenderer()
        self._ren_win = self._vtk_widget.GetRenderWindow()
        self._render.AddActor(self.axes())

    def _set_widget1_visible(self):
        self._a = not self._a
        if self._a:
            self._widget1.move(5000, 5000)
            self._widget1.setStyleSheet('background-color: rgba(120, 120, 120, 0)')
        else:
            self._widget1.move(100, 100)
            self._widget1.setStyleSheet('background-color: rgba(120, 120, 120, 100)')

    def _set_widget2_visible(self):
        self._b = not self._b
        if self._b:
            self._widget2.setStyleSheet('background-color: rgba(120, 120, 120, 0)')
        else:
            self._widget2.setStyleSheet('background-color: rgba(120, 120, 120, 100)')

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
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    _vtk = VTK()
    _vtk.show()

    sys.exit(app.exec_())
