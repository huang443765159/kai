import struct

from ._Network import Network
from ._WaterPump import WaterPump
from XYZChemicals4.Utils.CODEC import CODEC
from XYZChemicals4.Utils.CONST import CONST
from XYZChemicals4.Utils.Signals import Signals
from XYZChemicals4.Utils.XYZLog import msg, LEVEL


CHEM_ID_TO_SR = {CONST.DEVICES.M3: 'm3', CONST.DEVICES.ACID: '酸',
                 CONST.DEVICES.WHEELS: '轮毂', CONST.DEVICES.WAX: '水蜡'}


class OneChannel:

    def __init__(self, bot_id: int, chem_id: int, network: Network, water_pump: WaterPump):
        self._bot_id = bot_id
        self._chem_id = chem_id
        self._network = network
        # SIGNAL
        self._sign = Signals()
        # PUMP
        self._pump = water_pump
        # ATTR
        self._link = False
        self._switch = False
        self._cur_flow = 0.0
        self._cur_level = 0
        self._cur_pressure = 0

    def set_ena(self, ena: bool):  # 是否会有延迟问题，都充满水之后是否有延迟
        if self._switch != ena:
            self._switch = ena
            if self._link:
                write_count = self._network.get_write_count()
                self._network.send(CODEC.WRITE + struct.pack('B', write_count) +
                                   struct.pack('B', self._chem_id) + struct.pack('?', ena))
            self._sign.channel_switch.emit(self._bot_id, self._chem_id, ena)
        if ena and not self._pump.get_ena():
            self._pump.set_ena(ena=True)

    def get_ena(self) -> bool:
        return self._switch

    def sync_current_workflow(self, flow: float):
        self._cur_flow = flow
        self._sign.cur_flow.emit(self._bot_id, self._chem_id, flow)
        # 如果水泵和电磁阀已经开启，但是数据小于某个值证明没有开启成功，闭环思想
        if self._switch and self._pump.get_ena() and flow < 0.3:
            msg(info='化学流量不正常', level=LEVEL.ERROR)

    def get_current_workflow(self) -> float:
        return self._cur_flow

    def sync_current_pressure(self, pressure: int):
        self._cur_pressure = pressure
        self._sign.cur_pressure.emit(self._bot_id, self._chem_id, pressure)
        # 如果水泵和电磁阀已经开启，但是数据小于某个值证明没有开启成功，闭环思想
        if self._switch and self._pump.get_ena() and pressure < 5:
            msg(info='水泵未开启', level=LEVEL.ERROR)

    def get_current_pressure(self) -> int:
        return self._cur_pressure

    def sync_current_level(self, level: float):
        self._cur_level = level
        self._sign.cur_level.emit(self._bot_id, self._chem_id, level)
        # 液位低于7cm，上报需要添加，走LOG上报
        if level <= 70:
            msg(info=f'{CHEM_ID_TO_SR[self._chem_id]}化学液马上用完，请加液')

    def get_current_level(self) -> int:
        return self._cur_level

    def set_link(self, link: bool):
        if self._link != link:
            self._link = link

    def get_link(self) -> bool:
        return self._link
