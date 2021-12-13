import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QMovie, QFont


class Test(QWidget):

    def __init__(self):
        super(Test, self).__init__()
        self.label = QLabel('', self)
        self.label.move(0, 300)
        self.setFont(QFont('Arial'))
        self.setFixedSize(1500, 600)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        self.movie = QMovie("Images/1.gif")
        self.movie.setScaledSize(QSize(1500, 100))
        self.label.setMovie(self.movie)
        self.movie.start()

        self._label = QLabel('请向前行驶', self)
        self._label.move(650, 345)
        self._label.setStyleSheet('color: rgb(255, 255, 255)')
        font = self._label.font()
        font.setPixelSize(55)
        self._label.setFont(font)
        self._label.show()

        self.btn = QPushButton(self)
        self.btn.move(100, 100)
        self.btn.setText('TEST')
        self.btn.clicked.connect(self.change_gif)

    def change_gif(self):
        self.movie.stop()
        self._label.setText('')
        self._label.setStyleSheet('color: rgb(255, 255, 255)')
        self.movie = QMovie('Images/1.gif')
        self.movie.setScaledSize(QSize(1500, 100))
        self.label.setMovie(self.movie)
        self.movie.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loadingGitWin = Test()
    loadingGitWin.show()
    sys.exit(app.exec_())