import struct
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from ANETTEST.GUI.CLIENT.UI.UI import Ui_MainWindow
from ANETTEST.AutoNET.NetClient import NetClient
from ANETTEST.AutoNET.Socket._decode import TCP_HEAD, TCP_END

SERVER_PORT = 10001
TCP_LENGTH = 256


class GuiClient(QMainWindow, Ui_MainWindow):

    sign_event = pyqtSignal(object, object, object)
    sign_error = pyqtSignal(object, object, object)
    sign_recv = pyqtSignal(object, object)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sign_recv.connect(self._recv)
        self.sign_event.connect(self._event)
        self.sign_error.connect(self._error)
        # NETWORK
        self._network = NetClient(tcp_recv_cb=self._recv_thread_safe,
                                  tcp_port=SERVER_PORT,
                                  tcp_rx_len=TCP_LENGTH,
                                  event_cb=self._event_thread_safe,
                                  error_cb=self._error_thread_safe,
                                  launch_delay=5)
        self._network.set_device_type(device_type='X-SPACE')
        self._network.set_device_id(device_id=8)
        self._network.set_inviter_ena(ena=True)
        self._network.set_device_token(device_token='X-SPACE OPEN')
        # UI
        self.ui_my_ip.setText(self._network.get_my_ip())
        self.ui_server_port.setText(str(self._network.get_server_port()))
        self.ui_inviter_ena.stateChanged.connect(self._network.set_inviter_ena)
        self.ui_tcp_ena.stateChanged.connect(self._network.tcp.set_enable)
        # self.ui_token.currentTextChanged.connect(self._network.set_device_token)
        self.ui_device_type.setText(f'{self._network.get_device_type()}')
        self.ui_device_token.setText(f'{self._network.get_device_token()}')
        # TEST
        self.btn_bad_1_before.clicked.connect(lambda: self._test_tx(mode='ADD_BYTES_BEFORE'))
        self.btn_bad_2_more.clicked.connect(lambda: self._test_tx(mode='DATA_IS_MORE'))
        self.btn_bad_3_less.clicked.connect(lambda: self._test_tx(mode='DATA_IS_LESS'))
        self.btn_bad_4_empty.clicked.connect(lambda: self._test_tx(mode='DATA_IS_EMPTY'))
        self.btn_bad_5_x2.clicked.connect(lambda: self._test_tx(mode='GOOD_MSG x 2(WRONG CLIP)'))
        self.btn_send_large.clicked.connect(self._test_tx_large)
        self.btn_send_loop.clicked.connect(self._test_tx_loop)

    # CALLBACK -> GUI
    def _recv_thread_safe(self, rx_msg, ip):
        self.sign_recv.emit(rx_msg, ip)

    def _event_thread_safe(self, module, code, value):
        self.sign_event.emit(module, code, value)

    def _error_thread_safe(self, module, code, value):
        self.sign_error.emit(module, code, value)

    def _event(self, module, code, value):
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (server_ip, server_port) = value
                self.ui_server.setItem(0, 0, QTableWidgetItem(server_ip))
                self.ui_server.setItem(0, 1, QTableWidgetItem(str(is_connected)))
                self.ui_tcp_connected.setChecked(is_connected)
        if module == 'ANET_INVITER':
            self.ui_log_inviter.append(f'<{code}> {value}')
        else:
            self.ui_log_event.append(f'<{module}> <{code}> {value}')

    def _error(self, module, code, value):
        self.ui_log_error.append(f'{module} {code} {value}')

    def _recv(self, rx_msg, ip):
        self.ui_log_recv.append(f'{rx_msg} ({ip})')

    # BUTTONS
    @pyqtSlot()
    def on_btn_tcp_send_clicked(self):
        msg = self.ui_tx_msg.text().encode()
        self._network.tcp.send(data=msg)

    # UNIT_TEST
    def _test_tx(self, mode):
        data = self.ui_tx_msg.text().encode()
        if mode == 'ADD_BYTES_BEFORE':
            before = b'\xcc\xdd\xee\xff'
            msg = before + TCP_HEAD + struct.pack('!H', len(data)) + data + TCP_END
            self._network.tcp.send_direct(msg=msg)
        elif mode == 'DATA_IS_LESS':
            msg = TCP_HEAD + struct.pack('!H', len(data) + 5) + data + TCP_END
            self._network.tcp.send_direct(msg=msg)
        elif mode == 'DATA_IS_MORE':
            msg = TCP_HEAD + struct.pack('!H', len(data) - 2) + data + TCP_END
            self._network.tcp.send_direct(msg=msg)
        elif mode in ['GOOD_MSG x 2', 'GOOD_MSG x 2(WRONG CLIP)']:
            text = self.ui_tx_msg.text()
            text_1 = text + '_1'
            text_2 = text + '_2'
            data_1 = text_1.encode()
            data_2 = text_2.encode()
            msg_1 = TCP_HEAD + struct.pack('!H', len(data_1)) + data_1 + TCP_END
            msg_2 = TCP_HEAD + struct.pack('!H', len(data_2)) + data_2 + TCP_END
            msg = msg_1 + msg_2
            if mode == 'GOOD_MSG x 2':
                self._network.tcp.send_direct(msg=msg)
            elif mode == 'GOOD_MSG x 2(WRONG CLIP)':
                self._network.tcp.send_direct(msg=msg[:20])
                self._network.tcp.send_direct(msg=msg[20:])
        elif mode == 'DATA_IS_EMPTY':
            msg = TCP_HEAD + struct.pack('!H', 0) + TCP_END
            self._network.tcp.send_direct(msg=msg)
        print('TX_TEST', mode)

    def _test_tx_large(self):
        DATA_ZOOM = 10000000
        def to_bytes(lines_xy, lines_xz, lines_wheels, forward):
            bytes_msg = b'\xa7'
            bytes_msg += struct.pack('BBB?', len(lines_xy), len(lines_xz), len(lines_wheels), forward)
            for polyline in [lines_xy, lines_xz, lines_wheels]:
                for idx in range(len(polyline)):
                    one_point = polyline[idx]
                    x = int(one_point[0] * DATA_ZOOM)
                    y = int(one_point[1] * DATA_ZOOM)
                    z = int(one_point[2] * DATA_ZOOM)
                    bytes_msg += struct.pack('qqq', x, y, z)
            return bytes_msg
        one_lines = list()
        for idx in range(200):
            one_point = [0.342, 0.6645, 7.43]
            one_lines.append(one_point)
        _data = to_bytes(lines_xy=one_lines, lines_xz=one_lines, lines_wheels=one_lines, forward=True)
        msg = TCP_HEAD + struct.pack('!H', len(_data)) + _data + TCP_END
        self._network.tcp.send_direct(msg=msg)

    def _test_tx_loop(self):
        msg = TCP_HEAD + struct.pack('!H', len(b'Good')) + b'Good' + TCP_END
        for i in range(10000):
            self._network.tcp.send_direct(msg=msg)


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = GuiClient()
    window.show()
    sys.exit(app.exec_())
