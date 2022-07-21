import struct

from XYZChemicals4.Utils.CODEC import CODEC
from XYZChemicals4.Utils.CONST import CONST
from XYZChemicals4.Utils.Signals import Signals
from XYZChemicals4.OneSide._Network import Network
from XYZChemicals4.OneSide._Channels import Channels
from XYZChemicals4.OneSide._WaterPump import WaterPump


class OneSide:

    def __init__(self, bot_id: int, mcu_addr: tuple):
        self._bot_id = bot_id
        self._network = Network(bot_id=bot_id, mcu_ip=mcu_addr[0], mcu_port=mcu_addr[1])  # 要2个功能，一个发Mcu，一个发界面
        self._network.udp.sign_recv.connect(self._signal_udp_recv)
        # CHANNELS
        self._water_pump = WaterPump(bot_id=bot_id, network=self._network)
        self._channels = Channels(bot_id=bot_id, network=self._network, water_pump=self._water_pump)
        # SIGNAL  发送界面成
        self.sign = Signals()
        self.sign.pump_ena.connect(self._signal_pump_ena)
        self.sign.cur_flow.connect(self._signal_cur_flow)
        self.sign.cur_level.connect(self._signal_cur_level)
        self.sign.cur_pressure.connect(self._signal_cur_pressure)
        self.sign.channel_switch.connect(self._signal_channel_switch)
        # ITEMS
        self._items = {CONST.DEVICES.M3: self._channels.m3, CONST.DEVICES.ACID: self._channels.acid,
                       CONST.DEVICES.WHEELS: self._channels.wheels, CONST.DEVICES.WAX: self._channels.wax}

    # SIGNAL
    def _signal_udp_recv(self, data: bytes):
        head = data[0: 1]
        if head == CODEC.WRITE:
            chem_id, switch = data[2], data[3]
            self.set_channel_switch(chem_id=chem_id, ena=bool(switch))
        elif head == CODEC.READ:  # READ_ALL 按照从下往上，从左往右的顺序返回
            for i in range(5):
                dev_id, ena = struct.unpack('!B?', data[2 + i * 2: 2 + (i + 1) * 2])
                if dev_id in self._items.keys():
                    self.set_channel_switch(chem_id=dev_id, ena=ena)
                elif dev_id == CONST.PUMP:
                    self._water_pump.set_ena(ena=ena)
        elif head == CODEC.LEVEL:
            for i in range(4):
                chem_id, level = struct.unpack('!BH', data[2 + i * 3: 2 + (i + 1) * 3])
                self._items.get(chem_id).sync_current_level(level=level)
        elif head == CODEC.PRESSURE:  # 只有1套
            for chem_id, one_channel in self._items.items():
                if one_channel.get_ena():
                    self._items[chem_id].sync_current_pressure(pressure=data[2])
                    break
        elif head == CODEC.FLOW:  # 只有1套
            for chem_id, one_channel in self._items.items():
                if one_channel.get_ena():
                    self._items[chem_id].sync_current_workflow(flow=struct.unpack('f', data[2:])[0])
        elif head == CODEC.SENSORS:
            temp, humi = struct.unpack('!f', data[2: 6])[0], struct.unpack('!f', data[6: 10])[0]
            self.sign.temp_humi_data.emit(self._bot_id, temp, humi)

    # SIGNALS 同步给界面层
    def _signal_pump_ena(self, bot_id: int,  ena: bool):
        if bot_id == self._bot_id:
            pass

    def _signal_cur_flow(self, bot_id: int, chem_id: int, flow: float):
        if bot_id == self._bot_id:
            pass

    def _signal_cur_level(self, bot_id: int, chem_id: int, level: int):
        if bot_id == self._bot_id:
            pass

    def _signal_cur_pressure(self, bot_id: int, chem_id: int, pressure: int):
        if bot_id == self._bot_id:
            pass

    def _signal_channel_switch(self, bot_id: int, chem_id: int, switch: bool):
        if bot_id == self._bot_id:
            pass

    # LINK
    def set_link(self, link: bool):
        for dev in self._items.values():
            dev.set_link(link=link)
            if link:
                dev.set_ena(ena=False)
        if link:
            self._water_pump.set_ena(ena=False)

    def get_link(self) -> bool:
        return self._channels.m3.get_link()

    # API
    def set_channel_switch(self, chem_id: int, ena: bool):  # 只能开一路，不可以同时开启
        for _chem_id, one_item in self._items.items():
            if one_item.get_ena() and _chem_id != chem_id:
                one_item.set_ena(ena=False)
        print(f'CHEM_ID={chem_id}, ENA={ena}')
        self._items[chem_id].set_ena(ena=ena)

    def get_channel_switch(self, chem_id: int) -> bool:
        return self._items.get(chem_id).get_ena()

    def set_water_pump_ena(self, ena: bool):  # 关闭之前先看化学有没有开，如果有开着的不可关闭，是否需要加这个逻辑
        self._water_pump.set_ena(ena=ena)

    def get_water_pump_ena(self) -> bool:
        return self._water_pump.get_ena()

    def get_cur_flow(self, chem_id: int) -> float:
        return self._items[chem_id].get_current_workflow()

    def get_cur_level(self, chem_id: int) -> int:
        return self._items[chem_id].get_current_level()

    def get_cur_pressure(self, chem_id: int) -> int:
        return self._items[chem_id].get_current_pressure()

    def get_mcu_ip(self) -> str:
        return self._network.get_mcu_ip()

    def stop_all(self):
        self._channels.m3.set_ena(ena=False)
        self._channels.acid.set_ena(ena=False)
        self._channels.wax.set_ena(ena=False)
        self._channels.wheels.set_ena(ena=False)
        self._water_pump.set_ena(ena=False)

    def exit(self):
        self.stop_all()
        self._network.exit()
