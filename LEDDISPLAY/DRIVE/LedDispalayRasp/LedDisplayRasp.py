import time
import RPi.GPIO as GPIO
from PyQt5.QtCore import QObject, pyqtSignal
from LEDDISPLAY.DRIVE.AutoNET.NetServer import NetServer

TCP_PORT = 20010
LED_DISPLAY = {0x01: 'WELCOME', 0x02: 'FORWARD', 0x03: 'STOP', 0x04: 'BACK', 0x05: 'WASH START', 0x06: 'WASH END'}


class LedDisplay(QObject):

    sign_display = pyqtSignal(str, bool)  # show, is_display
    sign_connection = pyqtSignal(bool, str, int)  # is_connected, ip, port
    sign_error = pyqtSignal(str, str, object)  # error_type, code, error

    def __init__(self, pins):
        super().__init__()
        self._pins = pins
        # GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        for pin in self._pins:
            GPIO.setup(pin, GPIO.OUT)
        # SHOW
        self._show = {'WELCOME': [1, 1, 1, 1, 1], 'FORWARD': [1, 1, 1, 1, 0], 'STOP': [1, 1, 1, 0, 1],
                      'BACK': [1, 1, 0, 1, 1], 'WASH START': [1, 0, 1, 1, 1], 'WASH END': [0, 1, 1, 1, 1]}
        # NETWORK
        self._network = NetServer(event_cb=self._event, error_cb=self._error, tcp_recv_cb=self._recv, tcp_port=TCP_PORT)
        # COPY FUN
        self.get_my_ip = self._network.get_my_ip
        self.get_client_ips = self._network.get_client_ips
        self.get_server_port = self._network.get_server_port

    def set_display(self, show):
        if show in self._show.keys():
            for idx, state in enumerate(self._show[show]):
                GPIO.output(self._pins[idx], state)
        self.sign_display.emit(show, True)

    def _event(self, module, code, value):
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (ip, port) = value
                self.sign_connection.emit(is_connected, ip, port)

    def _error(self, module, code, value):
        self.sign_error.emit(module, code, value)

    def _recv(self, rx_msg, ip=None):
        if rx_msg[0] in LED_DISPLAY.keys():
            self.set_display(LED_DISPLAY[rx_msg[0]])


if __name__ == '__main__':

    _pins = [35, 36, 37, 38, 40]
    led = LedDisplay(pins=_pins)
    led.set_display('FORWARD')
    time.sleep(2)
    led.set_display('STOP')
    time.sleep(2)
    led.set_display('BACK')
    time.sleep(2)
    led.set_display('WASH START')
    time.sleep(2)
    led.set_display('WASH END')
    time.sleep(2)
    led.set_display('WELCOME')
