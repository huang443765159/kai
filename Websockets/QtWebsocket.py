from PyQt5 import QtCore, QtWebSockets, QtNetwork, QtWidgets


class MyServer(QtCore.QObject):
    def __init__(self, parent):
        super(QtCore.QObject, self).__init__(parent)
        self.clients = []
        self.server = QtWebSockets.QWebSocketServer(serverObject.serverName(), serverObject.secureMode(), parent)
        if self.server.listen(QtNetwork.QHostAddress.LocalHost, 19955):
            print('Connected: ' + self.server.serverName() + ' : ' + self.server.serverAddress().toString() + ':' + str(
                self.server.serverPort()))
        else:
            print('error')
        self.server.newConnection.connect(self.onNewConnection)

        print(self.server.isListening())

    def onNewConnection(self):
        self.clientConnection = self.server.nextPendingConnection()
        self.clientConnection.textMessageReceived.connect(self.processTextMessage)

        self.clientConnection.binaryMessageReceived.connect(self.processBinaryMessage)
        self.clientConnection.disconnected.connect(self.socketDisconnected)

        self.clients.append(self.clientConnection)

    def processTextMessage(self, message):
        print(message)
        if (self.clientConnection):
            self.clientConnection.sendTextMessage(message)

    def processBinaryMessage(self, message):
        if (self.clientConnection):
            self.clientConnection.sendBinaryMessage(message)

    def socketDisconnected(self):
        if (self.clientConnection):
            self.clients.remove(self.clientConnection)
            self.clientConnection.deleteLater()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    serverObject = QtWebSockets.QWebSocketServer('My Socket', QtWebSockets.QWebSocketServer.NonSecureMode)
    server = MyServer(app)
    serverObject.closed.connect(app.quit)
    app.exec_()
