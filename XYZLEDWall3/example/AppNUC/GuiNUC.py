from vtkmodules import all
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from example.AppNUC.UI.UI import Ui_MainWindow
import example.Utils.QTools as QTools
from XYZLedWall3.NUC.LedWall import LedWall
from XYZLedWall3.NUC.Vtk._vtkRenderer import VtkRenderer
from XYZLedWall3.Utils.CONST import CONST
from XYZLedWall3.Utils.Signal import SIGNAL


class GuiNUC(QMainWindow):

    def __init__(self, ui: Ui_MainWindow, led: LedWall):
        super().__init__()
        # SIGNAL
        SIGNAL.sign_is_online.connect(self._is_online)
        self._screen_size = QApplication.primaryScreen().size()
        # WIDGET
        self._widget = QWidget(self)
        self._widget.setAttribute(Qt.WA_TranslucentBackground)
        self.setCentralWidget(self._widget)
        self.resize(self._screen_size)
        self._widget.setStyleSheet("""
                        QWidget {
                            border: 1px solid black;
                            background-color: rgba(255, 255, 255, 0.2);
                            }
                        """)
        # VTK_WIDGET
        self._vtk_widget = QVTKRenderWindowInteractor(self._widget)
        self._vtk_widget.SetInteractorStyle(all.vtkInteractorStyleMultiTouchCamera())
        self._vtk_widget.resize(self._screen_size)
        self._ren_win = self._vtk_widget.GetRenderWindow()
        self._render = VtkRenderer(ren_win=self._ren_win)
        # SCREEN_SIZE
        sw, sh = self._screen_size.width(), self._screen_size.height()
        self.resize(int(sw * 0.7), int(sh * 0.7))
        self.move(int(sw * 0.3 / 2), int(sh * 0.3 / 2))
        # UI
        self._ui = ui
        self._ui.setupUi(self._widget)
        # TCP_LED
        self._tcp_led = {1: self._ui.led_bot1,
                     2: self._ui.led_bot2}
        # LED
        self._led = led
        self._led.set_render(render=self._render)
        # BTN
        self._ui.link.stateChanged.connect(self._set_link)
        # COLOR
        self._ui.btn_r.clicked.connect(self._set_r)
        self._ui.btn_g.clicked.connect(self._set_g)
        self._ui.btn_b.clicked.connect(self._set_b)
        self._ui.btn_colorful.clicked.connect(self._set_colorful)
        # SHOW
        self._ui.btn_img.clicked.connect(self._read_img)
        self._ui.btn_video.clicked.connect(self._read_video)
        # VTK_START
        self._vtk_widget.Start()

    def _is_online(self, bot_id, is_online, ip, port):
        QTools.set_led_style(ui_btn=self._tcp_led[bot_id],
                             color=[0, CONST.SHOW.COLOR[CONST.SHOW.G], 0] if is_online else [CONST.SHOW.COLOR[CONST.SHOW.R], 0, 0])

    def _set_r(self):
        for bot_id, ui_drv_id in {1: self._ui.drv_bot1, 2: self._ui.drv_bot2}.items():
            if ui_drv_id.isChecked():
                self._led[bot_id].set_r()

    def _set_g(self):
        for bot_id, ui_drv_id in {1: self._ui.drv_bot1, 2: self._ui.drv_bot2}.items():
            if ui_drv_id.isChecked():
                self._led[bot_id].set_g()

    def _set_b(self):
        for bot_id, ui_drv_id in {1: self._ui.drv_bot1, 2: self._ui.drv_bot2}.items():
            if ui_drv_id.isChecked():
                self._led[bot_id].set_b()

    def _set_colorful(self):
        for bot_id, ui_drv_id in {1: self._ui.drv_bot1, 2: self._ui.drv_bot2}.items():
            if ui_drv_id.isChecked():
                self._led[bot_id].set_colorful()

    def _read_img(self):
        img_id = self._ui.show.value()
        if img_id in [CONST.SHOW.WELCOME, CONST.SHOW.THANKS]:
            for bot_id, ui_drv_id in {1: self._ui.drv_bot1, 2: self._ui.drv_bot2}.items():
                if ui_drv_id.isChecked():
                    self._led[bot_id].read_img(img_id=img_id, bot_id=bot_id)
        else:
            print('\033[1;33m [LIQUID_TYPE_ERR] 无此节目 \033[0m')

    def _read_video(self):
        video_id = self._ui.show.value()
        if video_id in [CONST.SHOW.SEA, CONST.SHOW.SKY]:
            for bot_id, ui_drv_id in {1: self._ui.drv_bot1, 2: self._ui.drv_bot2}.items():
                if ui_drv_id.isChecked():
                    self._led[bot_id].read_video(video_id=video_id, bot_id=bot_id)
        else:
            print('\033[1;33m [LIQUID_TYPE_ERR] 无此节目 \033[0m')

    def _set_link(self, link: bool):
        self._led.set_link(link=link)
