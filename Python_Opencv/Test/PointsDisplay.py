import nu3mpy as np
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtCore import Qt
from vtkmodules import all
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from Test.test import rgb_data
from Test.VTK._Points import Points


class PointsDisplay(QMainWindow):

    def __init__(self):
        super(PointsDisplay, self).__init__()
        # WIDGET
        self.resize(2000, 1000)
        self._widget = QWidget(self)
        self._widget.setAttribute(Qt.WA_TranslucentBackground)
        self.setCentralWidget(self._widget)
        self._widget.resize(2000, 1000)
        # VTK_WIDGET
        self._vtk_widget = QVTKRenderWindowInteractor(self._widget)
        self._vtk_widget.SetInteractorStyle(all.vtkInteractorStyleMultiTouchCamera())
        self._ren_win = self._vtk_widget.GetRenderWindow()
        self._render = all.vtkRenderer()
        self._vtk_widget.resize(2000, 1000)
        # POINTS
        self._points = Points(render=self._render)
        self._ren_win.AddRenderer(self._render)
        self._vtk_widget.Start()
        # RENDER
        rgb_dict = dict()
        for idx, rgb in enumerate(rgb_data):
            rgb_dict[idx] = rgb
        new_rgb_dict = rgb_dict
        self._render.Render()
        a = list()
        for i in range(9600):
            a.append(i)
        b = np.array(a).reshape(64, 150)
        c = list(b)
        for idx, one_list in enumerate(c):
            if idx % 2 != 0:
                c[idx] = list(reversed(one_list))
        d = np.array(c)
        cid = 0
        for one_list in list(d.T):
            for id in one_list:
                new_rgb_dict[id] = rgb_dict[cid]
                # print(f'new={id} old={cid}')
                cid += 1
        for key, rgb in new_rgb_dict.items():
            self._points.set_point_color(key, rgb)
        self._render.Render()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    display = PointsDisplay()
    display.show()
    sys.exit(app.exec_())
