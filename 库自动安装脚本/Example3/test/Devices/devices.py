from Example3.Utils.Singleton import singleton
from Example3.AutoInstall.AutoInstall import AutoInstall


@singleton
class Devices:

    def __init__(self):
        self.auto = AutoInstall()
