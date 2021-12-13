from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsTextItem, QGraphicsScene, QGraphicsView, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QGraphicsVideoItem
from PyQt5.Qt import QUrl, QSizeF
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt


class Video(QMainWindow):

    def __init__(self):
        super(Video, self).__init__()
        self.resize(1920, 1080)
        # ITEM
        self._item = QGraphicsVideoItem()
        self._textItem = QGraphicsTextItem()
        self._view = QGraphicsView()
        self._scene = QGraphicsScene()
        self._view.resize(1920, 1080)
        self._view.setScene(self._scene)
        self._scene.addItem(self._item)
        self._scene.addItem(self._textItem)
        self._textItem.setPlainText('SRT TEXT')
        self._textItem.setDefaultTextColor(Qt.red)
        font = self._textItem.font()
        font.setPixelSize(50)
        self._textItem.setFont(font)
        self._view.show()
        self._item.setSize(QSizeF(1920, 1080))
        self._player = QMediaPlayer(self)
        self._player.setMedia(QMediaContent(
            QUrl.fromLocalFile('/Users/huangkai/Documents/PycharmProjects/AllTest/Qt插入背景/AddVideos/Videos/yellow.mov')))
        self._player.setVideoOutput(self._item)
        self._player.play()
        self.setCentralWidget(self._view)
        self._item.setPos(400, 500)
        # BUTTON
        self._btn = QPushButton(self)
        self._btn.resize(100, 50)
        self._btn.move(500, 500)
        self._btn.setText('test')
        self._btn.clicked.connect(self._change_text)

    def _change_text(self):
        self._textItem.setPlainText('Fighting')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = Video()
    test.show()
    sys.exit(app.exec_())