from example.Gui.GuiCmd import GuiCmd
from example.Gui.GuiSystem import GuiSystem
from example.Gui.UI.UI import Ui_MainWindow


class Gui:

    def __init__(self, ui: Ui_MainWindow):
        self._cmd = GuiCmd(ui=ui)
        self._sys = GuiSystem(ui=ui)
