import typing

from PyQt6 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self,) -> None:
        super(QtWidgets.QMainWindow, self).__init__()
        
        self.labelGames = QtWidgets.QLabel()
        self.labelGames.setObjectName("labelGames")
        self.labelProfiles = QtWidgets.QLabel()
        self.labelProfiles.setObjectName("labelProfiles")
        self.labelCurrentProfile = QtWidgets.QLabel()
        self.labelCurrentProfile.setObjectName("labelCurrentProfile")
        self.comboBoxGames = QtWidgets.QComboBox()
        self.comboBoxGames.setObjectName("comboBoxGames")
        self.comboBoxProfiles = QtWidgets.QComboBox()
        self.comboBoxProfiles.setObjectName("comboBoxProfiles")
        self.comboBoxCurrentProfile = QtWidgets.QComboBox()
        self.comboBoxCurrentProfile.setObjectName("comboBoxCurrentProfile")
        
        self.initUI()
        
    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(841, 582)
        
        layout = QtWidgets.QVBoxLayout()
        
        hbox1 = QtWidgets.QHBoxLayout()
        
        hbox1.addWidget(self.labelGames)
        hbox1.addWidget(self.comboBoxGames)
        hbox1.addWidget(self.labelProfiles)
        hbox1.addWidget(self.comboBoxProfiles)
        
        hbox2 = QtWidgets.QHBoxLayout()
        
        hbox2.addWidget(self.labelCurrentProfile)
        hbox2.addWidget(self.comboBoxCurrentProfile)
        hbox2.addSpacing(3)
        
        layout.addLayout(hbox1)
        layout.addLayout(hbox2)

        
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
        
        self.retranslateUi(self) 

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QT Nexus Mod Manager"))
        self.labelGames.setText(_translate("MainWindow", "Select a game"))
        self.labelProfiles.setText(_translate("MainWindow", "Select a profile"))
        self.labelCurrentProfile.setText(_translate("MainWindow", "Select current profile"))