import vtk
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from CARGUIDE.GUI.NUCGui._VTKLine import OneLine
from CARGUIDE.GUI.NUCGui.UI.UI import Ui_MainWindow
from CARGUIDE.DRIVER.GuideRemote.GuideRemote import GuideRemote


class NucVTK(QMainWindow):

    def __init__(self):
        super().__init__()
        # SIGNAL
        self._nuc = GuideRemote()
        self._nuc.sign_data.connect(self._data)
        self._nuc.sign_event.connect(self._event)
        self._nuc.sign_error.connect(self._error)

        # DATA
        self._lines = dict()
        self._lines[1] = OneLine([1, 0, 0], 3)
        self._lines[2] = OneLine([0, 0, 1], 3)
        self._lines[1].set_points([0.72, 0.63, 0.0], [0.72, 0.63, 4.8])
        self._lines[2].set_points([7.0, 0.63, 0.0], [7.0, 0.63, 4.8])

        # VTK
        self._vtk_widget = QVTKRenderWindowInteractor()
        self._render = vtk.vtkRenderer()
        self._render.AddActor(self._lines[1].actor)
        self._render.AddActor(self._lines[2].actor)
        self._render.SetBackground(1, 1, 1)
        self._ren_win = self._vtk_widget.GetRenderWindow()
        self._ren_win.AddRenderer(self._render)
        self._ren_win.GetInteractor().SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())

        # TIMER
        self._ren_win.GetInteractor().AddObserver('TimerEvent', self._render_timer)
        self._ren_win.GetInteractor().CreateRepeatingTimer(10)

        # QT
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 半透明
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setWindowOpacity(1)
        self.move(20, (QApplication.primaryScreen().size().height() - self.size().height()) / 2)

        # LAUNCH
        self._ren_win.SetSize(700, 700)
        self._vtk_widget.Start()
        self._vtk_widget.showFullScreen()

        # QT BTN
        self._ui.tcp_works.stateChanged.connect(self._set_tcp_launch)
        self._ui.btn_quit.clicked.connect(self.exit)

    def _data(self, count, data_dict):
        self._ui.data_log.append(f'[DATA] {count} {data_dict}')
        self._ui.sensor_box1.setValue(list(data_dict.values())[0])
        self._ui.sensor_box2.setValue(list(data_dict.values())[1])
        self._ui.sensor_box3.setValue(list(data_dict.values())[2])
        if list(data_dict.values())[0] == 1:
            self._lines[1].set_points([0.72, 0.63, 0.0], [0.72, 0.63, 5.0])
        if list(data_dict.values())[0] == 0:
            self._lines[1].set_points([0.72, 0.63, 0.0], [0.72, 0.63, 2.0])
        if list(data_dict.values())[1] == 1:
            self._lines[2].set_points([7.0, 0.63, 0.0], [7.0, 0.63, 5.0])
        if list(data_dict.values())[1] == 0:
            self._lines[2].set_points([7.0, 0.63, 0.0], [7.0, 0.63, 2.0])

    def _error(self, error_type, code, value):
        self._ui.event_log.append(f'[ERROR] {error_type} {code} {value}')

    def _event(self, event_type, code, value):
        if event_type == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (ip, port) = value
                self._ui.tcp_connected_btn.setChecked(is_connected)
                self._ui.tcp_ip_edit.setText(f'{ip}')
                self._ui.tcp_port_edit.setText(f'{port}')
                self._ui.tcp_type_edit.setText(f'{self._nuc.get_inviter_type()}')
        if event_type == 'ANET_INVITER':
            self._ui.inviter_log.append(f'[INVITER]  <{code}> {value}')
        else:
            self._ui.event_log.append(f'[EVENT]    <{event_type}> <{code}> {value}')

    def _set_tcp_launch(self, switch):
        # print(switch)
        if switch:
            self._nuc.launch()
        else:
            self._nuc.stop()

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

    _nuc = NucVTK()
    _nuc.show()

    sys.exit(app.exec_())
