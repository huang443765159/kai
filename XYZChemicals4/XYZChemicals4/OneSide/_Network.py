import struct

from XYZUtil4.network.UDP import UDP

from XYZChemicals4.Utils.CODEC import CODEC


class Network:

    def __init__(self, bot_id: int, mcu_ip: str, mcu_port: int):
        self._bot_id = bot_id
        self._mcu_ip = mcu_ip
        self._mcu_port = mcu_port
        self.udp = UDP(is_nuc=True)
        self.udp.set_peer_address(address=(mcu_ip, mcu_port))
        self.udp.sign_is_online.connect(self._signal_udp_is_online)
        self._read_count = 0
        self._write_count = 0

    def _signal_udp_is_online(self, ip: str, port: int, is_online: bool):
        if is_online:
            self.send(data=CODEC.READ + struct.pack('B', self._read_count))
            self._read_count += 1
            self._read_count = 0 if self._read_count == 256 else self._read_count

    def send(self, data: bytes):
        self.udp.send_to(data=data, ip=self._mcu_ip, port=self._mcu_port)
        self._write_count += 1
        self._write_count = 0 if self._write_count == 256 else self._write_count

    def get_write_count(self) -> int:
        return self._write_count

    def is_online(self) -> bool:
        return self.udp.get_peer_online()

    def get_mcu_ip(self) -> str:
        return self._mcu_ip

    def exit(self):
        self.udp.exit()


if __name__ == '__main__':
    a = b'\x01\x00\x02\x03\x04\x05\x06\x07\x08'
    b = list(struct.unpack('!hhhh', a[1:]))
    print(b)
