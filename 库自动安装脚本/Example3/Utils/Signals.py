from PyQt5.QtCore import QObject, pyqtSignal

from Example3.Utils.Singleton import singleton


@singleton
class Signals(QObject):

    now_lib = pyqtSignal(str, str)  # lib, version
    latest_lib = pyqtSignal(str, str, bool)  # lib, version, can_be_updated
    is_installed = pyqtSignal(str, bool)  # lib, bool
    is_installing = pyqtSignal(str, bool)  # lib, installing
