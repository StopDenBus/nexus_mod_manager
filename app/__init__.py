import sys

from PyQt6 import QtWidgets

from MainApplication import SingleApplication, SingleApplicationWithMessaging
from MainWindow2 import MainWindow
#from MainWindow import MainWindow
#from main import MainWindow

if __name__ == "__main__":
    
    app_name = "nexus_mod_manager"
    
    if len(sys.argv) > 1:
        app = SingleApplicationWithMessaging(sys.argv, app_name)
        if app.isRunning():
            app.sendMessage(' '.join(sys.argv[1:]))
            sys.exit(1)
    else:
        app = SingleApplication(sys.argv, app_name)
        if app.isRunning():
            sys.exit(1)    
    
    app.setApplicationName(app_name)
    
    window = MainWindow()
    app.messageAvailable.connect(window.handleMessage)
    window.show()
    
    sys.exit(app.exec())