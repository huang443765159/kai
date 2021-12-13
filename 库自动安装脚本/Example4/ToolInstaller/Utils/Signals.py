from PyQt5.QtCore import QObject, pyqtSignal

from Example4.ToolInstaller.Utils.Singleton import singleton


@singleton
class Signals(QObject):

    pip3_version = pyqtSignal(str, str)  # lib, version
    git_versions = pyqtSignal(str, str, bool, dict)  # lib, latest_version, can_be_updated, all_versions
    is_installed = pyqtSignal(str, bool)  # lib, bool
    is_installing = pyqtSignal(str, bool)  # lib, installing
