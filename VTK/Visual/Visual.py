from typing import Union
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

import vtkmodules.all as vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

# from example.NUC.Gui.UI.UI import Ui_Form


class Visual(QMainWindow):

    def __init__(self, render_frequency: float, window_zoom: int = 0.7):
        super().__init__()
        self._screen_size = QApplication.primaryScreen().size()
        self._central_widget = QWidget(self)
        self._central_widget.setAttribute(Qt.WA_AcceptTouchEvents | Qt.WA_TranslucentBackground)
        self._central_widget.setWindowFlags(Qt.NoDropShadowWindowHint)
        self._central_widget.resize(self._screen_size)
        self._vtk_widget = QVTKRenderWindowInteractor(self._central_widget)
        self._vtk_widget.SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())
        self._vtk_widget.resize(self._screen_size)
        self.setCentralWidget(self._central_widget)
        sw, sh = self._screen_size.width(), self._screen_size.height()
        self.resize(sw * window_zoom, sh * window_zoom)
        self.move(sw * (1 - window_zoom) / 2, sh * (1 - window_zoom) / 2)
        self._central_widget.setFocus()
        # UI
        # self._ui = Ui_Form()
        # self._ui.setupUi(Form=self._central_widget)
        for widget in self._central_widget.children():
            widget.setStyleSheet(f"""
                    QGroupBox {{
                    background-color: rgba(200, 200, 200, 1); 
                    border-radius: 5; 
                    }}""")
        # QT_STYLE
        self.setWindowFlags(Qt.NoDropShadowWindowHint)
        self._render = vtk.vtkRenderer()
        self._ren_win = self._vtk_widget.GetRenderWindow()
        self._ren_win.AddRenderer(self._render)
        self._interactor = self._ren_win.GetInteractor()
        # TIMER
        self._timer = QTimer()
        self._timer.setInterval(int(1000 / render_frequency))
        self._timer.timeout.connect(self._working)
        self._is_running = False
        self.set_render_ena(False)

    def _working(self):
        if self._is_running:
            self._interactor.Render()

    def set_render_ena(self, ena: bool):
        if ena != self._is_running:
            self._is_running = bool(ena)
            if ena:
                self._timer.start()
            else:
                self._timer.stop()

    def add_actor(self, actor: Union[vtk.vtkProp3D,
                                     vtk.vtkOpenGLTextActor,
                                     vtk.vtkAxesActor,
                                     vtk.vtkScalarBarActor,
                                     vtk.vtkOpenGLActor,
                                     list]):
        if actor.__class__ in [vtk.vtkProp3D, vtk.vtkOpenGLTextActor, vtk.vtkAxesActor, vtk.vtkAssembly,
                               vtk.vtkOpenGLActor]:
            self._render.AddActor(actor)
        elif actor.__class__ in [vtk.vtkScalarBarActor]:
            self._render.AddActor2D(actor)
        elif actor.__class__ == list:
            for this_actor in actor:
                self._render.AddActor(this_actor)

    def del_actor(self, actor: vtk.vtkProp3D):
        self._render.RemoveActor(actor)

    def render_once(self):
        self._interactor.Render()

    def get_ui_form(self) -> Ui_Form:
        return self._ui

    def show(self):
        self._vtk_widget.GetRenderWindow().GetInteractor().Initialize()
        self._vtk_widget.GetRenderWindow().GetInteractor().Start()
        super().show()

    def exit(self):
        self._interactor.DestroyTimer()
        self._timer.stop()
        self.close()
