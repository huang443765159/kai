from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
import threading
import random
import time
import vtk
from VTK.UI.UI import Ui_MainWindow
from VTK.VTK_LINE.VTKLine import OneLine


class GuideLine(QMainWindow):

    def __init__(self):
        super().__init__()
        # DATA
        self._lines = dict()
        self._lines[1] = OneLine((1, 0, 0), 3)
        self._lines[2] = OneLine((0, 0, 1), 3)
        self._lines[1].set_points([0.72, 0.63, 0.0], [0.72, 0.63, 5.0])
        self._lines[2].set_points([7.0, 0.63, 0.0], [7.0, 0.63, 5.0])

        # VTK
        self._vtk_widget = QVTKRenderWindowInteractor()
        self._renderer = vtk.vtkRenderer()
        self._renderer.AddActor(self._lines[1].actor)
        self._renderer.AddActor(self._lines[2].actor)
        self._ren_win = self._vtk_widget.GetRenderWindow()
        self._ren_win.AddRenderer(self._renderer)
        self._ren_win.GetInteractor().SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())

        # TIMER
        self._ren_win.GetInteractor().AddObserver('TimerEvent', self._render_timer)
        self._ren_win.GetInteractor().CreateRepeatingTimer(10)

        # QT
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 半透明
        self.move(20, (QApplication.primaryScreen().size().height() - self.size().height()) / 2)
        self._ui.btn_quit.clicked.connect(self.exit)

        # LAUNCH
        self._ren_win.SetSize(700, 700)
        self._vtk_widget.Start()
        self._vtk_widget.showFullScreen()

        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            num = random.randint(0, 1)
            if num == 0:
                self._lines[1].set_points([0.72, 0.63, 0.0], [0.72, 0.63, 2.0])
                self._lines[2].set_points([7.0, 0.63, 0.0], [7.0, 0.63, 1.0])
            # elif num == 1:
            #     self._lines[1].set_points([0.72, 0.63, 0.0], [0.72, 0.63, 2.5])
            # elif num == 2:
            #     self._lines[2].set_points([7.0, 0.63, 0.0], [7.0, 0.63, 5.0])
            elif num == 1:
                self._lines[1].set_points([0.72, 0.63, 0.0], [0.72, 0.63, 5.0])
                self._lines[2].set_points([7.0, 0.63, 0.0], [7.0, 0.63, 5.0])
            #     print(type(self._lines[2]))
            time.sleep(1)

    def _render_timer(self, obj, event):
        obj.GetRenderWindow().Render()

    def exit(self):
        self._ren_win.WaitForCompletion()
        self._ren_win.GetInteractor().DestroyTimer()
        self._vtk_widget.close()
        self.close()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    _lines = GuideLine()
    _lines.show()

    sys.exit(app.exec_())
