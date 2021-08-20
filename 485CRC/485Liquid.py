import time
import struct
import threading
"""
注意：485是半双工，只能发一条接收一条然后再发下一条接收下一条
"""


def get_crc_data(msg: bytes):
    crc_init = 0xffff
    for data in msg:
        data = data & 0x00ff
        crc_init ^= data
        for i in range(0, 8):
            if crc_init & 0x0001:
                crc_init >>= 1
                crc_init ^= 0xa001
            else:
                crc_init >>= 1
    crc_high, crc_low = crc_init & 0xff, crc_init >> 8
    return struct.pack('B', crc_high), struct.pack('B', crc_low)


class OneLiquid(object):

    def __init__(self, chem_id, ser, chem_level_cb):
        self._chem_id = chem_id
        self._dev_id = chem_id + 1
        self._ser = ser
        self._chem_level_cb = chem_level_cb
        self._msg = bytes()

        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            if self._ser is not None:
                msg = struct.pack('B', self._dev_id) + b'\x03\x00\x01\x00\x01'
                crc_high, crc_low = get_crc_data(msg=msg)
                self._ser.write(msg + crc_high + crc_low)
                data = self._ser.read()
                if data:
                    self._msg += data
                    recv_crc_high, recv_crc_low = get_crc_data(self._msg[0: -2])
                    if recv_crc_high == self._msg[-2: -1] and recv_crc_low == self._msg[-1:]:
                        if self._msg[1: 2] == b'\x03':
                            data = self._msg[3] * 256 + self._msg[4]
                            self._chem_level_cb(chem_id=self._chem_id, level_data=data)
                            print(self._msg)
                        self._msg = bytes()
                time.sleep(0.5)

                msg = b'\x02' + b'\x03\x00\x01\x00\x01'
                crc_high, crc_low = get_crc_data(msg=msg)
                self._ser.write(msg + crc_high + crc_low)
                data = self._ser.read()
                if data:
                    self._msg += data
                    recv_crc_high, recv_crc_low = get_crc_data(self._msg[0: -2])
                    if recv_crc_high == self._msg[-2: -1] and recv_crc_low == self._msg[-1:]:
                        if self._msg[1: 2] == b'\x03':
                            data = self._msg[3] * 256 + self._msg[4]
                            self._chem_level_cb(chem_id=self._chem_id, level_data=data)
                            print(self._msg)
                        self._msg = bytes()
                time.sleep(0.5)

    def get_level(self):
        if self._ser is not None:
            msg = struct.pack('B', self._dev_id) + b'\x03\x00\x01\x00\x01'
            crc_high, crc_low = get_crc_data(msg=msg)
            self._ser.write(msg + crc_high + crc_low)

    def set_dev_id(self, dev_id: int):
        msg = struct.pack('B', self._dev_id) + b'\x06\x00\x04\x00' + struct.pack('B', dev_id)
        crc_high, crc_low = get_crc_data(msg)
        self._ser.write(msg + crc_high + crc_low)


if __name__ == '__main__':

    import platform
    if 'Linux' in platform.system():
        import serial
        ser = serial.Serial(port='/dev/ttyS1', baudrate=9600)
    else:
        ser = None

    def _chem_level_callback(chem_id, level_data):
        print('chem_id_', chem_id, level_data)

    test = OneLiquid(chem_id=0, chem_level_cb=_chem_level_callback, ser=ser)
    while 1:
        # test.get_level()
        # time.sleep(3)
        # test1.get_level()
        time.sleep(1)
