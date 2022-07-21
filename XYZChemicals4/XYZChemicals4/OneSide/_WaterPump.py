import struct

from ._Network import Network
from XYZChemicals4.Utils.CONST import CONST
from XYZChemicals4.Utils.CODEC import CODEC
from XYZChemicals4.Utils.Signals import Signals


class WaterPump:

    def __init__(self, bot_id: int, network: Network):
        self._bot_id = bot_id
        self._network = network
        # ATTR
        self._ena = False
        self._link = False
        self._sign = Signals()

    def set_ena(self, ena: bool):
        if self._ena != ena:
            self._ena = ena
            if self._link:
                write_count = self._network.get_write_count()
                self._network.send(
                    CODEC.WRITE + struct.pack('B', write_count) + struct.pack('B', CONST.PUMP) + struct.pack('?', ena))
            self._sign.pump_ena.emit(self._bot_id, ena)

    def get_ena(self) -> bool:
        return self._ena
