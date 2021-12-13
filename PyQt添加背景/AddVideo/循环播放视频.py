from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.Qt import QUrl, QVideoWidget
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt


class VideoPlayer(QMainWindow):

    def __init__(self):
        super(VideoPlayer, self).__init__()
        self._screen_size = QApplication.primaryScreen().size()
        sw, sh = self._screen_size.width(), self._screen_size.height()
        self.resize(sw, sh)
        self.setStyleSheet('background: black')
        # # PLAYER
        self._playList = QMediaPlaylist()
        self._playWidget = QVideoWidget(self)
        self._playWidget.resize(sw, sh)
        self._player = QMediaPlayer(self)
        self._player.setPlaylist(self._playList)
        self._player.setVideoOutput(self._playWidget)
        self._playList.addMedia(QMediaContent(
            QUrl.fromLocalFile('/Users/huangkai/Documents/PycharmProjects/AllTest/Qt插入背景/AddVideos/Videos/yellow.mov')))
        self._playList.setPlaybackMode(QMediaPlaylist.Loop)
        self._player.play()

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        key = a0.key()
        if key == Qt.Key_Escape:
            self.resize(100, 100)
            self._playWidget.resize(100, 100)
            self._player.stop()
        elif key in (Qt.Key_Return, Qt.Key_Enter):
            self.resize(self._screen_size.width(), self._screen_size.height())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = VideoPlayer()
    test.show()
    sys.exit(app.exec_())