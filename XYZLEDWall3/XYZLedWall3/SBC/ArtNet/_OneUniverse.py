import socket
from XYZLedWall3.Utils.CONST import CONST


class OneUniverse(object):

    def __init__(self, universe, art_net, ip='192.168.1.192'):
        self._ip = ip
        self._art_net = art_net
        self._universe = universe
        # ATTR
        self._pkt_len = CONST.ARTNET.PKT_LEN
        self._tx_head = bytearray()
        self._tx_data = bytearray(self._pkt_len)
        self.make_head()

    def make_head(self):
        # TX_HEAD
        self._tx_head = bytearray()
        self._tx_head.extend(bytearray('Art-Net', 'utf8'))
        self._tx_head.append(0x00)
        self._tx_head.extend(CONST.ARTNET.OPCODE)
        self._tx_head.extend(CONST.ARTNET.VERSION)
        self._tx_head.append(CONST.ARTNET.SEQUENCE)
        self._tx_head.append(CONST.ARTNET.PHYSICAL)
        self._tx_head.append(self._universe & 0xff)
        self._tx_head.append(self._universe >> 8 & 0xff)
        self._tx_head.append(self._pkt_len >> 8 & 0xff)
        self._tx_head.append(self._pkt_len & 0xff)

    def set_rgb(self, address, r, g, b):  # address-1: r, address: g, address+1: b
        if address < 1 or address > 510:
            print('address error: 正确地址在1-511之间')
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
        tx_msg.extend(self._tx_head)
        tx_msg.extend(self._tx_data)
        try:
            self._art_net.sendto(tx_msg, (self._ip, CONST.ARTNET.PORT))
        except socket.error as err:
            print('tx error', err)

    def close(self):
        self._art_net.close()
