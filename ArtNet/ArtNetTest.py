import sys
sys.path.append('/home/pi/Desktop')
import socket

DELAY = 1
PORT = 6454  # ArtNet 固定端口
OPCODE = [0x00, 0x50]  # 传输方式定义
VERSION = [0x00, 0x0e]  # ArtNet版本号
SEQUENCE = 0x00  # 禁止乱序自动排列功能
PHYSICAL = 0x00  # 物理端口，默认为0


class ArtNet(object):

    def __init__(self, pkt_len=512, ip='192.168.1.192'):
        self._ip = ip
        self._pkt_len = pkt_len
        # UDP
        self._udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # ATTR
        self._universe = 0
        self._head = bytearray()
        self._tx_data = bytearray(self._pkt_len)

    def _make_head(self):
        # TX_HEAD
        self._head = bytearray()
        self._head.extend(bytearray('Art-Net', 'utf8'))
        self._head.append(0x00)
        self._head.extend(OPCODE)
        self._head.extend(VERSION)
        self._head.append(SEQUENCE)
        self._head.append(PHYSICAL)
        self._head.append(self._universe & 0xff)
        self._head.append(self._universe >> 8 & 0xff)
        self._head.append(self._pkt_len >> 8 & 0xff)
        self._head.append(self._pkt_len & 0xff)

    def set_universe(self, universe):
        self._universe = universe
        self._make_head()

    def set_rgb(self, address, r, g, b):  # address - 1位为r, address位为g， address + 1位为b
        if address < 1 or address > 510:
            print('数据地址错误：正常地址应在1-511之间')
            return
        self._tx_data[address - 1] = r
        self._tx_data[address] = g
        self._tx_data[address + 1] = b

    def set_tx_data(self, tx_data):
        if len(tx_data) != self._pkt_len:
            return
        self._tx_data = tx_data

    def show(self):
        tx_msg = bytearray()
        tx_msg.extend(self._head)
        tx_msg.extend(self._tx_data)
        try:
            self._udp.sendto(tx_msg, (self._ip, CONST.ART_NET.PORT))
            print(tx_msg)
        except socket.error as err:
            print('TX_ERROR', err)

    def clear(self):
        self._tx_data = bytearray(self._pkt_len)

    def close(self):
        self._udp.close()


if __name__ == '__main__':
    test = ArtNet()
    test.set_universe(5)
    test.set_rgb(1, 255, 0, 0)
    test.show()

