import socket
from ArtNetClass.Utils.CONST import CONST


class OneUniverse(object):

    def __init__(self, universe, art_net, pkt_len=512, ip='192.168.1.192'):
        self._universe = universe
        self._ip = ip
        self._art_net = art_net
        self._pkt_len = pkt_len
        # ATTR
        self._head = bytearray()
        self._tx_data = bytearray(pkt_len)
        self.make_head()

    def make_head(self):
        # TX_HEAD
        self._head = bytearray()
        self._head.extend(bytearray('Art-Net', 'utf8'))
        self._head.append(0x00)
        self._head.extend(CONST.ART_NET.OPCODE)
        self._head.extend(CONST.ART_NET.VERSION)
        self._head.append(CONST.ART_NET.SEQUENCE)
        self._head.append(CONST.ART_NET.PHYSICAL)
        self._head.append(self._universe & 0xff)
        self._head.append(self._universe >> 8 & 0xff)
        self._head.append(self._pkt_len >> 8 & 0xff)
        self._head.append(self._pkt_len & 0xff)

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

    def clear(self):
        self._tx_data = bytearray(self._pkt_len)

    def show(self):
        tx_msg = bytearray()
        tx_msg.extend(self._head)
        tx_msg.extend(self._tx_data)
        try:
            self._art_net.sendto(tx_msg, (self._ip, CONST.ART_NET.PORT))
        except socket.error as err:
            print('TX_ERROR', err)

    def close(self):
        self._art_net.close()
