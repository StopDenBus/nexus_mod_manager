import sys

#from PyQt6 import QtGui, QtCore, QtNetwork
from PyQt6 import QtCore, QtGui, QtWidgets, QtNetwork

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
            print("## SingleApplication: start server")
            self._running = False
            if not self._memory.create(1):
                raise RuntimeError( self._memory.errorString() )
            self._server = QtNetwork.QLocalServer(self)
            print(self._server.newConnection.connect(self.handleMessage))
            print(self._server.listen(self._key))
            
    def isRunning(self):
        return self._running
    
    def handleMessage(self):
        socket = self._server.nextPendingConnection()
        if socket.waitForReadyRead(self._timeout):
            self.messageAvailable.emit(bytes(socket.readAll().data()).decode('utf-8'))
            socket.disconnectFromServer()
        else:
            QtCore.qDebug(socket.errorString())    

class SingleApplicationWithMessaging(SingleApplication):
    def __init__(self, argv, key):
        print("## SingleApplicationWithMessaging init")
        SingleApplication.__init__(self, argv, key)
        self._key = key
        self._timeout = 1000
        #self._server = QtNetwork.QLocalServer(self)

        #if not self.isRunning():
        #    print("## starting listen")
        #    print(self._server.newConnection.connect(self.handleMessage))
        #    print(self._server.listen(self._key))

    #def handleMessage(self):
    #    print("## handleMessage")
    #    socket = self._server.nextPendingConnection()
    #    if socket.waitForReadyRead(self._timeout):
    #        self.emit(QtCore.SIGNAL('messageAvailable'), bytes(socket.readAll().data()).decode('utf-8') )
    #        socket.disconnectFromServer()
    #    else:
    #        QtCore.qDebug(socket.errorString())

    def sendMessage(self, message):
        print("## sendMessage")
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

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.edit = QtWidgets.QLineEdit(self)
        self.edit.setMinimumWidth(300)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.edit)

    def handleMessage(self, message):
        print("## Window handleMessage")
        self.edit.setText(message)

if __name__ == '__main__':

    key = 'foobarfoobar'

    # if parameter no. 1 was set then we'll use messaging between app instances
    if len(sys.argv) > 1:
        app = SingleApplicationWithMessaging(sys.argv, key)
        if app.isRunning():
            msg = ''
            # checking if custom message was passed as cli argument
            if len(sys.argv) > 2:
                msg = sys.argv[2]
            else:
                msg = 'APP ALREADY RUNNING'
            app.sendMessage( msg )
            print( "app is already running, sent following message: \n\"{0}\"".format( msg ) )
            sys.exit(1)
    else:
        print("## creating SingleApplication")
        app = SingleApplication(sys.argv, key)
        if app.isRunning():
            print('app is already running, no message has been sent')
            sys.exit(1)

    window = Window()
    app.messageAvailable.connect(window.handleMessage)
    window.show()

    sys.exit(app.exec())