import threading
from typing import Dict

from Example4.ToolInstaller.Utils.CONST import LIBS
from Example4.ToolInstaller.Utils.Signals import Signals
from Example4.ToolInstaller.OneLib.OneLib import OneLib


class ToolInstaller:

    def __init__(self):
        self._libs = dict()  # type: Dict[str, OneLib]
        for one_lib in LIBS:
            self._libs[one_lib] = OneLib(lib=one_lib)
        self._is_installing = False
        self._is_checking = False
        self._installed_libs = list()
        self._need_install_libs = list()
        # SIGNALS
        self.sign = Signals()
        self.sign.is_installed.connect(self._signal_is_installed)

    # SIGNAL
    def _signal_is_installed(self, lib: str, is_installed: bool):
        self._installed_libs.append(lib)
        if self._installed_libs == self._need_install_libs:
            self._installed_libs.clear()
            self._is_installing = False

    def _working(self, libs: dict):
        self._is_installing = True
        for lib, lib_version in libs.items():
            self._libs[lib].install(lib=lib, lib_version=lib_version)

    def install_libs(self, libs: dict):
        self._need_install_libs = list(libs.keys())
        thread = threading.Thread(target=self._working, args=(libs, ), daemon=True)
        thread.start()

    def get_installing(self) -> bool:
        return self._is_installing

    def get_checking(self) -> bool:
        is_checking = True if True in [one_lib.get_checking() for one_lib in self._libs.values()] else False
        return is_checking
