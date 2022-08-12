from typing import Optional
from PyQt5 import QtCore, QtWebSockets, QtNetwork

PORT = 18750


"""
1-使用终端 cd 到html同级目录下，然后python3 -m http.server 端口号.端口号可以省略。
2-使用浏览器打开localhost:8000即可
如果按file的方式加载html，无法加载相关依赖
"""


class WetScreen(QtCore.QObject):

    def __init__(self, parent: QtWebSockets.QWebSocketServer):
        super().__init__(parent)
        self._server = QtWebSockets.QWebSocketServer(parent.serverName(), parent.secureMode(), parent)
        if self._server.listen(QtNetwork.QHostAddress.LocalHost, PORT):
            print('Connected: ' + self._server.serverName() + ' : ' + self._server.serverAddress().toString() + ':' +
                  str(self._server.serverPort()))
        else:
            print('error')
        self._server.newConnection.connect(self._new_connection)
        self._client = None  # type: Optional[None, QtWebSockets.QWebSocket]

    def _new_connection(self):
        print('RECONNECTION')
        self._client = self._server.nextPendingConnection()
        self._client.textMessageReceived.connect(self.send_text_message)
        self._client.binaryMessageReceived.connect(self.send_binary_message)
        self._client.disconnected.connect(self.disconnect)

    def send_text_message(self, cmd: str):
        print(f'TX_MSG={cmd}')
        if self._client:
            self._client.sendTextMessage(cmd)

    def send_binary_message(self, cmd: bin):
        if self._client:
            self._client.sendBinaryMessage(cmd)

    def disconnect(self):
        self._client.deleteLater()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    s_parent = QtWebSockets.QWebSocketServer('My Socket', QtWebSockets.QWebSocketServer.NonSecureMode)
    server = WetScreen(parent=s_parent)
    s_parent.closed.connect(app.quit)
    app.exec_()
