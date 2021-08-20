from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QEvent
import types
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class Test(QMainWindow):

    def __init__(self):
        super().__init__()
        # WIDGET
        self._widget = QWidget(self)
        self._widget.setAttribute(Qt.WA_TranslucentBackground)
        self.setCentralWidget(self._widget)
        self.resize(900, 900)
        self._widget.event = types.MethodType(self._handle_event, self._widget)
        self._widget.setAttribute(Qt.WA_AcceptTouchEvents)  # 与半透明分开设置
        # VTK
        self._vtk_widget = QVTKRenderWindowInteractor(self._widget)
        self._vtk_widget.resize(900, 900)
        self._ren_win = self._vtk_widget.GetRenderWindow()
        self._ren_win.GetInteractor().SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())
        self._renderer = vtk.vtkOpenGLRenderer()
        self._renderer.SetBackground((0, 0, 0))
        self._renderer.AddActor(self._axis_actor())
        self._ren_win.AddRenderer(self._renderer)
        self._vtk_widget.Start()
        # BUTTON WIDGET
        widget = QWidget(self._widget)
        widget.resize(200, 200)
        widget.setStyleSheet('QWidget {background: red}')
        widget.setToolTip('button test')
        widget.show()
        button = QPushButton(widget)
        button.setStyleSheet('QPushButton {background: blue}')
        button.setText('test')
        button.clicked.connect(lambda: print('clicked'))
        button.show()

    @staticmethod
    def _handle_event(widget, event):
        if event.type() in [QEvent.TouchBegin, QEvent.TouchUpdate, QEvent.TouchEnd]:
            touch_points = event.touchPoints()
            print(touch_points)
            widget.update()
        return True

    def _axis_actor(self):
        actor = vtk.vtkAxesActor()
        actor.SetTotalLength(2, 2, 2)
        actor.SetShaftType(0)
        actor.SetCylinderRadius(0.01)
        actor.GetXAxisCaptionActor2D().SetWidth(0.01)
        actor.GetYAxisCaptionActor2D().SetWidth(0.01)
        actor.GetZAxisCaptionActor2D().SetWidth(0.01)
        return actor


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setOverrideCursor(Qt.BlankCursor)
    test = Test()
    test.show()
    sys.exit(app.exec_())
