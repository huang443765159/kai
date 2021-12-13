import struct
from PyQt5.QtCore import QObject, pyqtSignal
from INTERACTION2.DRIVER.AutoNET.NetServer import NetServer
from INTERACTION2.DRIVER.Interaction.Guides._OneSensor import OneSensor
from INTERACTION2.DRIVER.Interaction.Guides._GuidesDisplay import GuidesDisplay

TCP_PORT = 20013


class Guides(QObject):

    sign_data = pyqtSignal(list)  # guides_data
    sign_event = pyqtSignal(str, str, tuple)  # event_type, code, value
    sign_error = pyqtSignal(str, str, object)  # error_type, code, error

    def __init__(self, pi, device_type, device_token):
        super().__init__()
        # NETWORK
        self._network = NetServer(event_cb=self._event, error_cb=self._error, tcp_recv_cb=self._recv, tcp_port=TCP_PORT)
        self._network.set_device_id(2)
        self._network.set_invitation_broadcast_ena(True)
        self._network.set_device_type(device_type)
        self._network.set_device_token(device_token)
        # GUIDES
        self.display = GuidesDisplay(dev_addr=0x10, slave_addrs=[1, 2, 3, 4])
        self._display_key = 1
        self._display_key1 = 1
        self._guides = dict()
        self._guides_data = {0: None, 1: None}
        self._memory_data = True
        self._guides_memory = dict()
        for sid, pin in enumerate([21, 26]):
            self._guides[sid] = OneSensor(pi=pi, sid=sid, pin=pin, data_cb=self._data)
        # COPY FUN
        self.get_my_ip = self._network.get_my_ip
        self.get_client_ips = self._network.get_client_ips
        self.get_server_port = self._network.get_server_port

    def _data(self, sid, data):
        self._guides_data[sid] = data
        if None not in self._guides_data.values():
            if self._guides_memory != self._guides_data.copy():
                self._guides_memory = self._guides_data.copy()
                print(self._guides_memory)
                guides_data = list(self._guides_memory.values())
                self.sign_data.emit(guides_data)
                msg = struct.pack('B', len(guides_data))
                for data in guides_data:
                    msg += struct.pack('?', data)
                self._network.tcp.send_broadcast(msg)
                if not guides_data[0] and guides_data[1]:
                    print('forward')
                    self._display_key = 1
                    self._memory_data = guides_data[0]
                    if self._display_key1 == 1:
                        pass
                    else: 
                        self.display.set_display_key('NEXT')
                if not self._memory_data and guides_data[0] and guides_data[1]:
                    print('stop')
                    self._display_key1 = 2
                    _key = 'LAST' if self._display_key == 1 else 'NEXT'
                    self.display.set_display_key(_key)
                if guides_data[0] and not guides_data[1]:
                    print('back')
                    self._display_key = 2
                    self.display.set_display_key('BACK')
            for sid in self._guides_data.keys():
                self._guides_data[sid] = None

    def _event(self, module, code, value):
        self.sign_event.emit(module, code, value)

    def _error(self, module, code, value):
        self.sign_error.emit(module, code, value)

    def _recv(self, rx_msg, ip=None):
        pass

    def exit(self):
        self._network.exit()


if __name__ == '__main__':
    import os
    import pigpio

    _pi = pigpio.pi()
    if not _pi.connected:
        os.system('sudo pigpiod')
        _pi = pigpio.pi()

    guides = Guides(pi=_pi, device_type='GUIDES', device_token='OPEN GUIDES')
