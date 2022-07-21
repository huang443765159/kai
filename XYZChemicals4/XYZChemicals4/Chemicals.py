from typing import Dict

from XYZUtil4.log import log_chemicals
from XYZUtil4.config import config_chemicals, ConfigChemicals

from XYZChemicals4.Utils.Signals import Signals
from XYZChemicals4.OneSide.OneSide import OneSide


class Chemicals:

    def __init__(self, config: ConfigChemicals = None):
        self._sides = dict()  # type: Dict[int, OneSide]
        config = config if config is not None else config_chemicals
        for bot_id, infos in config.raw_dict.items():
            mcu_addr = (infos['mcu_ip'], infos['mcu_port'])
            self._sides[bot_id] = OneSide(bot_id=bot_id, mcu_addr=mcu_addr)
        # SIGNAL
        self.sign = Signals()

    def get_one_side(self, bot_id: int) -> OneSide:
        return self._sides.get(bot_id)

    def set_link(self, link: bool):
        for bot_id in self._sides.keys():
            self._sides.get(bot_id).set_link(link=link)

    def get_link(self) -> bool:
        return self._sides.get(1).get_link()

    def get_mcu_addr(self, bot_id: int) -> str:
        return self._sides[bot_id].get_mcu_ip()

    def stop_all(self):
        for one_side in self._sides.values():
            one_side.stop_all()

    def exit(self):
        self.stop_all()
        for one_side in self._sides.values():
            one_side.exit()


if __name__ == '__main__':
    chem = Chemicals()
