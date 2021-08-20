import vtk
import time
import random
import threading
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from VTK.UI.UI import Ui_MainWindow


class QVtk(QMainWindow):

    def __init__(self):
        super().__init__()

        self.points = vtk.vtkPoints()

        self._vtk_widget = QVTKRenderWindowInteractor()
        self._render = vtk.vtkRenderer()
        self._render.AddActor(self.points_actor())
        self._render.SetBackground(0, 0, 0)
        self._ren_win = self._vtk_widget.GetRenderWindow()
        self._ren_win.AddRenderer(self._render)
        self._ren_win.GetInteractor().SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())

        self._ren_win.GetInteractor().AddObserver('TimerEvent', self._render_timer)
        self._ren_win.GetInteractor().CreateRepeatingTimer(10)

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 半透明
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setWindowOpacity(1)
        self.move(20, (QApplication.primaryScreen().size().height() - self.size().height()) / 2)

        self._thread = threading.Thread(target=self._working)
        self._thread_switch = False
        self._thread.daemon = True
        self._thread.start()

        self._ren_win.SetSize(700, 700)
        self._vtk_widget.Start()
        self._vtk_widget.showFullScreen()

        self._ui.btn_quit.clicked.connect(self.quit)

    def points_actor(self):
        poly = vtk.vtkPolyData()
        poly.SetPoints(self.points)
        mapper = vtk.vtkPointGaussianMapper()
        mapper.SetInputData(poly)
        mapper.EmissiveOff()
        mapper.SetScaleFactor(0.0)
        actor = vtk.vtkActor()
        actor.GetProperty().SetRepresentationToPoints()  # 没有明显帮助
        actor.SetMapper(mapper)
        actor.GetProperty().SetPointSize(1)
        actor.GetProperty().SetColor((1, 0, 0))
        return actor

    def _render_timer(self, obj, event):
        obj.GetRenderWindow().Render()

    def _add_random_points(self, random_points_num=1):  # 10.29 sec
        for i in range(random_points_num):
            xyz = (random.random() * 10, random.random() * 10, random.random() * 10)
            self.points.InsertNextPoint(xyz)
        self.points.Modified()

    def _working(self):
        thread_ts = time.time()
        while 1:
            self._add_random_points(random_points_num=2000)
            if self.points.GetNumberOfPoints() > 1000000:
                print(f'TS = {time.time()-thread_ts}')
            time.sleep(0.01)

    def quit(self):
        self._ren_win.WaitForCompletion()
        self._ren_win.GetInteractor().DestroyTimer()
        self._vtk_widget.close()
        self.close()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    q_vtk = QVtk()
    q_vtk.show()

    sys.exit(app.exec_())
