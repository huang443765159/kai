from ._Network import Network
from ._WaterPump import WaterPump
from ._OneChannel import OneChannel
from XYZChemicals4.Utils.CONST import CONST


class Channels:

    def __init__(self, bot_id: int, network: Network, water_pump: WaterPump):
        self.m3 = OneChannel(bot_id=bot_id, chem_id=CONST.DEVICES.M3,  network=network, water_pump=water_pump)
        self.acid = OneChannel(bot_id=bot_id, chem_id=CONST.DEVICES.ACID, network=network, water_pump=water_pump)
        self.wheels = OneChannel(bot_id=bot_id, chem_id=CONST.DEVICES.WHEELS, network=network, water_pump=water_pump)
        self.wax = OneChannel(bot_id=bot_id, chem_id=CONST.DEVICES.WAX, network=network, water_pump=water_pump)
