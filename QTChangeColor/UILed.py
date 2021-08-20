from PyQt5.QtGui import QFont

led_colors = {

    'DARKGREEN': (0, 100, 0),
    'GREEN': (0, 255, 0),
    'YELLOW': (255, 255, 0),
    'RED': (255, 0, 0),
}


class UILed(object):

    def __init__(self, qt_btn, color='RED', text=None, tip=None, font_size=7):
        super().__init__()
        self._ui_btn = qt_btn
        # font = QFont()
        # font.setFamily('Arial')
        # font.setPointSize(font_size)
        # self._ui_btn.setFont(font)
        # self._font_size = font_size
        self._color = None
        self._text = None
        self._tip = None
        self.set_color(color)
        self.set_text(text)
        self.set_tip(tip)

    def set_appearance(self, color, text='', tip=''):
        self.set_color(color)
        self.set_text(text)
        self.set_tip(tip)

    def set_text(self, text):
        if text is None:
            text = ''
        if text == self._text:
            return
        self._text = text
        self._ui_btn.setText(text)

    def set_color(self, color, text_color='black', alpha=1):  # alpha=1 is 100%
        if color == self._color:
            return
        self._color = color
        rgb = led_colors[color]
        rgba = 'rgba({:.0f}, {:.0f}, {:.0f}, {:.0%})'.format(rgb[0], rgb[1], rgb[2], alpha)
        color_sheet = 'QPushButton {background-color: ' + rgba + '; border: none; color: ' + text_color + ';}'
        self._ui_btn.setStyleSheet(color_sheet)

    def set_tip(self, tip):
        if tip is None:
            return
        if tip == self._tip:
            return
        self._tip = tip
        self._ui_btn.setToolTip(tip)

    def set_stylesheet(self, style):
        self._ui_btn.setStyleSheet(style)
