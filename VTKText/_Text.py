import vtk


class Text(object):

    def __init__(self, color, size, bold):
        self._color = color
        self._size = size
        # TEXT INIT
        self.txt = vtk.vtkTextActor()
        self._property = self.txt.GetTextProperty()
        self.set_color(color)
        self.set_font_size(size)
        self.set_bold(bold)
        # 居中是按照给的坐标设置的
        self._property.SetJustification(1)  # 左右居中
        self._property.SetVerticalJustification(1)  # 上下居中
        # 设置字体样式
        self._property.SetFontFamilyToArial()
        # self._property.SetFontFamily(vtk.VTK_FONT_FILE)  # 自定义设置字体样式
        # self._property.SetFontFile("FangZhengKaiTiJianTi-1.ttf")

    def set_input(self, text: str):
        self.txt.SetInput(str(text))

    def set_color(self, color):
        self._property.SetColor(color)

    def set_font_size(self, size):
        self._property.SetFontSize(size)

    def set_font_pos(self, pos1, pos2):
        self.txt.SetDisplayPosition(pos1, pos2)

    def set_opacity(self, opacity):
        self._property.SetOpacity(opacity)

    def set_bold(self, bold: bool):
        self._property.BoldOn() if bold else self._property.BoldOff()

