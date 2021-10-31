from PyQt6 import QtCore, QtWidgets, QtNetwork

import pathlib

class SingleApplication(QtWidgets.QApplication):
    messageAvailable = QtCore.pyqtSignal(object)
    def __init__(self, argv, key):
        QtWidgets.QApplication.__init__(self, argv)
        self._key = key
        self._timeout = 1000
        self._memory = QtCore.QSharedMemory(self)
        self._memory.setKey(key)
        if self._memory.attach():
            self._running = True
        else:
            self._running = False
            if not self._memory.create(1):
                raise RuntimeError( self._memory.errorString() )
            self._server = QtNetwork.QLocalServer(self)
            self._server.newConnection.connect(self.handleMessage)
            if not self._server.listen(self._key):                
                raise RuntimeError("Server could'nt listen.")
            sockfile_path = pathlib.Path(self._server.fullServerName())
            print(f'socket path: {sockfile_path}')
            
    def isRunning(self):
        return self._running
    
    def handleMessage(self):
        print("## handleMessage")
        socket = self._server.nextPendingConnection()
        if socket.waitForReadyRead(self._timeout):
            self.messageAvailable.emit(bytes(socket.readAll().data()).decode('utf-8'))
            socket.disconnectFromServer()
        else:
            QtCore.qDebug(socket.errorString())    

class SingleApplicationWithMessaging(SingleApplication):
    def __init__(self, argv, key):
        SingleApplication.__init__(self, argv, key)

    def sendMessage(self, message):
        if self.isRunning():
            socket = QtNetwork.QLocalSocket(self)
            socket.connectToServer(self._key, QtCore.QIODeviceBase.OpenModeFlag.WriteOnly)
            if not socket.waitForConnected(self._timeout):
                print(socket.errorString())
                return False
            socket.write(str(message).encode('utf-8'))
            if not socket.waitForBytesWritten(self._timeout):
                print(socket.errorString())
                return False
            socket.disconnectFromServer()
            return True
        return False