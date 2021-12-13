import threading
from typing import Dict

from Example3.Utils.CONST import LIBS
from Example3.Utils.Signals import Signals
from Example3.AutoInstall._OneLib import OneLib


class AutoInstall:

    def __init__(self):
        self._libs = dict()  # type: Dict[str, OneLib]
        for one_lib in LIBS:
            self._libs[one_lib] = OneLib(lib=one_lib)
        self._is_installing = False
        self._installed_libs = list()
        self._need_install_libs = list()
        # SIGNALS
        self.sign = Signals()
        self.sign.is_installed.connect(self._signal_is_installed)

    # SIGNAL
    def _signal_is_installed(self, lib: str, is_installed: bool):
        self._installed_libs.append(lib)
        if self._installed_libs == self._need_install_libs:
            self._is_installing = False

    def _working(self, libs: list):
        self._is_installing = True
        for one_lib in libs:
            self._libs[one_lib].install()

    def check_lib(self):
        for one_lib in self._libs.values():
            one_lib.check_lib()

    def install_libs(self, libs: list):
        self._need_install_libs = libs
        thread = threading.Thread(target=self._working, args=(libs, ), daemon=True)
        thread.start()

    def get_is_installing(self) -> bool:
        return self._is_installing
