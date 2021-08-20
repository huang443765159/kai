import vtk
import signal
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from VTKText.UI.UI import Ui_MainWindow
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from VTKText._Text import Text


class VTK(QMainWindow):

    def __init__(self):
        super().__init__()
        self._vtk_widget = QVTKRenderWindowInteractor()
        self._ren = vtk.vtkRenderer()
        self._ren_win = self._vtk_widget.GetRenderWindow()
        self._ren_win.AddRenderer(self._ren)
        self._ren_win.GetInteractor().SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())
        self._ren_win.GetInteractor().AddObserver('TimerEvent', self._render_timer)
        self._ren_win.GetInteractor().CreateRepeatingTimer(100)
        # ADD ACTOR
        self._ren.AddActor(self.axes())
        self._ren_win.GetInteractor().Initialize()
        self._ren.SetTexturedBackground(True)
        # self._ren.SetBackgroundTexture()
        self._vtk_widget.Start()
        self._vtk_widget.showFullScreen()
        # UI
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 半透明
        self.move(20, int((QApplication.primaryScreen().size().height() - self.size().height()) / 2))  # 距离左侧20中心
        # TEXT
        self._txt = Text(color=(1, 0, 0), size=250, bold=True)
        self._txt.set_input('forward')
        self._txt1 = Text(color=(0, 1, 0), size=150, bold=True)
        self._txt1.set_font_pos(500, 500)
        self._txt1.set_input('I am your dad')
        self._ren.AddActor(self._txt1.txt)
        win_size = self._vtk_widget.GetSize()
        self._txt.set_font_pos(int(win_size[0] / 2), int(win_size[1] / 2 + 200))  # 设置字体在屏幕中间
        # BTN
        self._ui.btn_stop.clicked.connect(self.exit)
        self._ui.btn_welcome.clicked.connect(lambda: self._txt.set_input('welcome'))
        self._ui.btn_forward.clicked.connect(lambda: self._txt.set_input('forward'))
        self._ui.btn_back.clicked.connect(lambda: self._txt.set_input('back'))
        self._ui.btn_add_text.clicked.connect(lambda: self._ren.AddActor(self._txt.txt))
        self._ui.btn_del_text.clicked.connect(lambda: self._ren.RemoveActor(self._txt.txt))
        # SIGNAL
        signal.signal(signal.SIGINT, self.closeEvent)

    def axes(self):
        axes_actor = vtk.vtkAxesActor()
        axes_actor.SetTotalLength(2, 2, 2)
        axes_actor.SetShaftType(1)
        axes_actor.SetCylinderRadius(0.01)
        axes_actor.GetXAxisCaptionActor2D().SetWidth(0.01)
        axes_actor.GetYAxisCaptionActor2D().SetWidth(0.01)
        axes_actor.GetZAxisCaptionActor2D().SetWidth(0.01)
        return axes_actor

    def _render_timer(self, obj, event):
        obj.GetRenderWindow().Render()

    def exit(self):
        self._ren_win.WaitForCompletion()
        self._ren_win.GetInteractor().DestroyTimer()
        self._vtk_widget.close()
        self.close()

    def closeEvent(self, event_signum=None, frame=None):
        self.close()

    def del_actor(self):
        self._ren.RemoveActor(self._txt.txt)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    _vtk = VTK()
    _vtk.show()

    sys.exit(app.exec_())
