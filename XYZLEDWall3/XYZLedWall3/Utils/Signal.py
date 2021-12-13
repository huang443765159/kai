from PyQt5.QtCore import QObject, pyqtSignal


class _Signal(QObject):

    sign_is_online = pyqtSignal(int, bool, str, int)  # bot_id, is_online, ip, port


SIGNAL = _Signal()
