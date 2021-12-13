from Example4.ToolInstaller.Utils.Singleton import singleton
from Example4.ToolInstaller.TooInstaller import ToolInstaller


@singleton
class Devices:

    def __init__(self):
        self.tool = ToolInstaller()
