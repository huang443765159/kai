from PyQt5.QtWidgets import QSlider, QWidget, QStyle, QMainWindow, QVBoxLayout, QStyleOptionSlider
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import sys


class Slider(QSlider):  # QScrollBar

    def __init__(self):
        super().__init__()
        self._slider_text = str()

    def set_text(self, text: str):
        self._slider_text = text

    def paintEvent(self, event):
        super().paintEvent(event)
        option = QStyleOptionSlider()
        self.initStyleOption(option)
        self.setOrientation(Qt.Horizontal)
        painter = QPainter(self)
        slider_rect = self.style().subControlRect(QStyle.CC_Slider,  # CC_ScrollBar
                                                  option, QStyle.SC_SliderHandle, self)  # SC_ScrollBarSlider
        text_width = self.fontMetrics().width(self._slider_text)
        if text_width > slider_rect.width():
            slider_width = (text_width - slider_rect.width()) / 2
            slider_rect.adjust(int(-slider_width), 0, int(slider_width), 0)
        painter.drawText(slider_rect, Qt.AlignCenter, self._slider_text)


class Test(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self._widget = QWidget(self)
        self._widget.resize(500, 500)
        self.setCentralWidget(self._widget)
        layout = QVBoxLayout(self._widget)
        # SLIDER
        slider = Slider()
        slider.set_text('1')
        layout.addWidget(slider)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    example = Test()
    example.show()
    sys.exit(app.exec_())
