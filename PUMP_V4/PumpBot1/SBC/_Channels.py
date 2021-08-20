from PyQt5.QtCore import QObject, pyqtSignal
from PumpBot1.SBC._OneRelay import I2CRelay, GPIORelay
from PumpBot1.Util.DEFINES import CHANNEL


class Channels(QObject):

    sign_channel_ena = pyqtSignal(int, int, int)  # bot_id, cid, state(0, 1)

    def __init__(self, bot_id, config_dir, dev_address=(0x10, 0x11), slave_address=(1, 2, 3, 4),
                 pins=(19, 13, 6, 5, 9, 10, 22, 27)):
        super().__init__()
        self._bot_id = bot_id
        self._config_dir = config_dir
        # RELAYS
        self._relays = dict()
        self._relays['I2C'] = [I2CRelay(dev_address=i, slave_address=j) for i in dev_address for j in slave_address]
        self._relays['GPIO'] = [GPIORelay(pin=pin) for pin in pins]
        # PUMP INSTRUCT
        self._liquid_types = {CHANNEL.CH_WHL: [self._relays['GPIO'][0], self._relays['I2C'][0], self._relays['I2C'][4]],
                              CHANNEL.CH_A: [self._relays['GPIO'][1], self._relays['I2C'][1], self._relays['GPIO'][4]],
                              CHANNEL.CH_B: [self._relays['GPIO'][2], self._relays['I2C'][2], self._relays['GPIO'][4]],
                              CHANNEL.CH_WAX: [self._relays['GPIO'][3], self._relays['I2C'][3], self._relays['GPIO'][4]],
                              CHANNEL.WATER: [self._relays['GPIO'][5]]}

    def set_channel_ena(self, cid, ena):
        if cid in self._liquid_types.keys():
            for relay in self._liquid_types[cid]:
                relay.set_ena(ena=ena)
            self.sign_channel_ena.emit(self._bot_id, cid, ena)
        else:
            print(f'\033[1;33m [LIQUID_TYPE_ERR] {cid} \033[0m')

    def stop_all(self):
        for relay_list in self._relays.values():
            for relay in relay_list:
                relay.set_ena(False)
