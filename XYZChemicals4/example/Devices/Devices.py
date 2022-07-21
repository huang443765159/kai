from XYZChemicals4.Chemicals import Chemicals
from XYZChemicals4.Utils.Singleton import singleton


@singleton
class Devices:

    def __init__(self):
        self.chemicals = Chemicals()
