from python_opencv_handleRGB_Image._HandleRGB import HandleRGB
import os
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from vtkmodules import all
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from python_opencv_handleRGB_Image.VTK._Points import Points


class LedShow(QMainWindow):

    def __init__(self):
        super(LedShow, self).__init__()
        self.resize(2000, 1500)
        # WIDGET
        self._widget = QWidget(self)
        self.setCentralWidget(self._widget)
        self._widget.setAttribute(Qt.WA_TranslucentBackground)
        self._widget.resize(2000, 1500)
        # VTK
        self._vtk_widget = QVTKRenderWindowInteractor(self._widget)
        self._vtk_widget.SetInteractorStyle(all.vtkInteractorStyleMultiTouchCamera())
        self._ren_win = self._vtk_widget.GetRenderWindow()
        self._render = all.vtkRenderer()
        self._vtk_widget.resize(2000, 1500)
        # POINTS
        self._points = Points(render=self._render)
        self._ren_win.AddRenderer(self._render)
        self._vtk_widget.Start()
        # HANDLE
        self._handle = HandleRGB(rgb_callback=self._rgb_callback, img_path=os.getcwd())

    def _rgb_callback(self, rgb_dict):
        # pass
        for p_id, rbg in rgb_dict.items():
            self._points.set_point_color(p_id=p_id, color=rbg)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    led = LedShow()
    led.show()
    sys.exit(app.exec_())
