import time
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt
from ANETTEST.GUI.SERVER.UI.UI import Ui_MainWindow
from ANETTEST.AutoNET.NetServer import NetServer

SERVER_PORT = 10001


class GuiServer(QMainWindow, Ui_MainWindow):

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
        self._network = NetServer(tcp_recv_cb=self._recv_thread_safe,
                                  event_cb=self._event_thread_safe,
                                  error_cb=self._error_thread_safe,
                                  tcp_port=SERVER_PORT,
                                  launch_delay=5)
        self._network.set_device_type(device_type='X-SPACE')
        self._network.set_device_id(device_id=8)
        self._network.set_inviter_ena(ena=True)
        self._network.set_device_token(device_token='X-SPACE OPEN')
        # UI
        self.ui_server_ip.setText(self._network.get_my_ip())
        self.ui_server_port.setText(str(self._network.get_server_port()))
        self.ui_inviter_ena.stateChanged.connect(self._network.set_inviter_ena)
        # self.ui_token.currentTextChanged.connect(self._network.set_device_token)
        self.ui_device_token.setText(f'{self._network.get_device_token()}')
        self.ui_device_type.setText(f'{self._network.get_device_type()}')

    # CALLBACK -> GUI
    def _recv_thread_safe(self, rx_msg, ip):
        self.sign_recv.emit(rx_msg, ip)

    def _event_thread_safe(self, module, code, value):
        self.sign_event.emit(module, code, value)

    def _error_thread_safe(self, module, code, value):
        self.sign_error.emit(module, code, value)

    def _event(self, module, code, value):
        if module == 'ANET_TCP':
            if code == 'BIND':
                is_bound, (host_ip, host_port) = value
                self.ui_tcp_bind.setChecked(is_bound)
            elif code == 'CONNECT':
                is_connected, (client_ip, client_port) = value
                ui_items = self.ui_clients.findItems(client_ip, Qt.MatchExactly)
                if ui_items:
                    row = ui_items[0].row()
                else:
                    row = 0
                self.ui_clients.setItem(row, 0, QTableWidgetItem(client_ip))
                self.ui_clients.setItem(row, 1, QTableWidgetItem(str(is_connected)))
                self.ui_tcp_connected.setChecked(self._network.tcp.is_connected())
        if module == 'ANET_INVITER':
            self.ui_log_inviter.append(f'<{code}> {value} <{time.time()}>')
        else:
            self.ui_log_event.append(f'<{module}> <{code}> {value}')

    def _error(self, module, code, value):
        self.ui_log_error.append(f'<{code}> <{value}>')

    def _recv(self, rx_msg, ip):
        self.ui_log_recv.append(f'{rx_msg} ({ip}) <{time.time()}>')

    @pyqtSlot()
    def on_btn_tcp_send_clicked(self):
        msg = self.ui_tx_msg.text().encode()
        if self.ui_broadcast.isChecked():
            self._network.tcp.send_broadcast(msg)
        else:
            selected_item = self.ui_clients.item(self.ui_clients.currentRow(), 0)
            if selected_item:
                peer_ip = selected_item.text()
                self._network.tcp.send_to(msg, peer_ip)


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = GuiServer()
    window.show()
    sys.exit(app.exec_())
