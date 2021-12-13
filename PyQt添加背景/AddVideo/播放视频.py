from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QGraphicsTextItem, QGraphicsScene, QGraphicsView
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QGraphicsVideoItem
from PyQt5.Qt import QUrl, QVideoWidget, QSizeF
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt


class Video(QMainWindow):

    def __init__(self):
        super(Video, self).__init__()
        self.resize(1920, 1080)
        self._item = QGraphicsVideoItem()
        self._view = QGraphicsView()
        self._scene = QGraphicsScene()
        self._view.resize(1920, 1080)
        self._view.setScene(self._scene)
        self._scene.addItem(self._item)
        self._view.show()
        self._item.setSize(QSizeF(1920, 1080))
        self._player = QMediaPlayer(self)
        self._player.setMedia(QMediaContent(
            QUrl.fromLocalFile('/Users/huangkai/Documents/PycharmProjects/AllTest/Qt插入背景/AddVideos/Videos/yellow.mov')))
        self._player.setVideoOutput(self._item)
        self._player.play()
        self.setCentralWidget(self._view)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = Video()
    test.show()
    sys.exit(app.exec_())