from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from Example3.Utils.CONST import LIBS
from Example3.test.Gui.UI.UI import Ui_MainWindow
from Example3.AutoInstall.AutoInstall import AutoInstall
import Example3.test.Utils.QTools as QTools


class Gui:

    def __init__(self, ui: Ui_MainWindow):
        self._ui = ui
        # AUTO_INSTALL
        self._auto_install = AutoInstall()
        self._sign = self._auto_install.sign
        self._sign.now_lib.connect(self._signal_now_lib)
        self._sign.latest_lib.connect(self._signal_latest_lib)
        self._sign.is_installed.connect(self._signal_is_installed)
        self._sign.is_installing.connect(self._signal_is_installing)
        QTools.table_init(table=self._ui.table_libs, column_width_list=[130, 130, 130, 100])
        for row_id, one_lib in enumerate(LIBS):
            self._ui.table_libs.item(row_id, 0).setText(one_lib)
        # BTN
        self._ui.btn_install.clicked.connect(self._install)
        self._ui.btn_check_libs.clicked.connect(self._auto_install.check_lib)

    # SIGNAL
    def _signal_now_lib(self, lib: str, version: str):
        item = self._ui.table_libs.findItems(lib, Qt.MatchContains)
        self._ui.table_libs.item(item[0].row(), 1).setText(version)

    def _signal_latest_lib(self, lib: str, version: str, can_be_updated: bool):
        item = self._ui.table_libs.findItems(lib, Qt.MatchContains)
        version = '▲' + version if not can_be_updated else version
        self._ui.table_libs.item(item[0].row(), 2).setText(version)

    def _signal_is_installed(self, lib: str, is_installed: bool):
        item = self._ui.table_libs.findItems(lib, Qt.MatchContains)
        self._ui.table_libs.item(item[0].row(), 3).setText(f'{is_installed}')

    def _signal_is_installing(self, lib: str, is_installing: bool):
        item = self._ui.table_libs.findItems(lib, Qt.MatchContains)
        self._ui.table_libs.item(item[0].row(), 3).setText(f'installing')

    def _install(self):
        libs = list()
        select = self._ui.table_libs.selectedItems()
        for one_lib in select:
            libs.append(one_lib.text())
        if self._auto_install.get_is_installing():
            QMessageBox.about(self, "WARNINGS", "上次安装还未完毕，请稍后再试")
        self._auto_install.install_libs(libs=libs)
