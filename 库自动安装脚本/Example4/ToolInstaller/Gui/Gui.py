from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QMessageBox, QTableWidgetItem

from Example4.ToolInstaller.Utils.CONST import LIBS
import Example4.ToolInstaller.Gui.Utils.QTools as QTools
from Example4.ToolInstaller.Gui.UI.UI import Ui_MainWindow
from Example4.ToolInstaller.TooInstaller import ToolInstaller


class Gui:

    def __init__(self, ui: Ui_MainWindow):
        self._ui = ui
        # AUTO_INSTALL
        self._tool = ToolInstaller()
        self._sign = self._tool.sign
        self._sign.pip3_version.connect(self._signal_now_lib)
        self._sign.git_versions.connect(self._signal_git_versions)
        self._sign.is_installed.connect(self._signal_is_installed)
        self._sign.is_installing.connect(self._signal_is_installing)
        # TABLE_WIDGET
        self._btn_check = dict()
        QTools.table_init(table=self._ui.table_libs, column_width_list=[30, 100, 100, 120, 60])
        for i in range(self._ui.table_libs.rowCount()):
            self._btn_check[i] = QTableWidgetItem()
            self._btn_check[i].setCheckState(False)
            self._ui.table_libs.setItem(i, 0, self._btn_check[i])
        # DROP_BOX
        self._drop_box = dict()
        for row_id, one_lib in enumerate(LIBS):
            self._drop_box[row_id] = QComboBox()
            font = self._drop_box[row_id].font()
            font.setPointSize(8)
            self._drop_box[row_id].setFont(font)
            self._drop_box[row_id].setStyleSheet('QComboBox {combobox-popup: 0}')
            self._drop_box[row_id].setMaxVisibleItems(10)
            self._ui.table_libs.item(row_id, 1).setText(one_lib)
        # BTN
        self._ui.btn_install.setEnabled(False)
        self._ui.btn_install.clicked.connect(self._install)
        self._ui.all_select.clicked.connect(self._select_all)

    # SIGNAL
    def _signal_now_lib(self, lib: str, version: str):
        item = self._ui.table_libs.findItems(lib, Qt.MatchContains)
        self._ui.table_libs.item(item[0].row(), 2).setText(version)

    def _signal_git_versions(self, lib: str, latest_version: str, can_be_updated: bool, git_versions: dict):
        item = self._ui.table_libs.findItems(lib, Qt.MatchContains)
        latest_version = '▲' + latest_version if can_be_updated else latest_version
        self._drop_box[item[0].row()].addItem(latest_version)
        for previous_ver in list(git_versions.values()):
            self._drop_box[item[0].row()].addItem(previous_ver)
        self._ui.table_libs.setCellWidget(item[0].row(), 3, self._drop_box[item[0].row()])
        if not self._tool.get_checking():
            self._ui.btn_install.setEnabled(True)

    def _signal_is_installed(self, lib: str, is_installed: bool):
        item = self._ui.table_libs.findItems(lib, Qt.MatchContains)
        self._ui.table_libs.item(item[0].row(), 4).setText(f'{"Installed" if is_installed else "NOT Installed"}')
        if not self._tool.get_installing():
            self._ui.btn_install.setEnabled(True)

    def _signal_is_installing(self, lib: str, is_installing: bool):
        item = self._ui.table_libs.findItems(lib, Qt.MatchContains)
        self._ui.table_libs.item(item[0].row(), 4).setText(f'installing')

    def _select_all(self, ena: bool):
        for one_check in self._btn_check.values():
            one_check.setCheckState(2 if ena else 0)

    def _install(self):
        self._ui.btn_install.setEnabled(False)
        libs = dict()
        for row in range(self._ui.table_libs.rowCount()):
            state = self._ui.table_libs.item(row, 0).checkState()
            if state:
                lib = self._ui.table_libs.item(row, 1).text()
                release_ver = self._ui.table_libs.cellWidget(row, 3).currentText()
                # release_idx = self._ui.table_libs.cellWidget(row, 3).findText(release_ver, Qt.MatchContains)
                libs[lib] = release_ver
        if not libs:
            return
        if self._tool.get_installing():
            QMessageBox.about(None, "WARNINGS", "上次安装还未完毕，请稍后再试")
        elif self._tool.get_checking():
            QMessageBox.about(None, 'WARNINGS', '还在检查版本中，请稍后再试')
        else:
            self._tool.install_libs(libs=libs)
