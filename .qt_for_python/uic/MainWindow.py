# Form implementation generated from reading ui file '/home/micha/prog/python/nexus_mod_manager/app/uic/MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 463)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 871, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelGames = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelGames.setObjectName("labelGames")
        self.horizontalLayout.addWidget(self.labelGames)
        self.comboBoxGames = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxGames.sizePolicy().hasHeightForWidth())
        self.comboBoxGames.setSizePolicy(sizePolicy)
        self.comboBoxGames.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.comboBoxGames.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAlphabetically)
        self.comboBoxGames.setObjectName("comboBoxGames")
        self.horizontalLayout.addWidget(self.comboBoxGames)
        self.labelProfiles = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelProfiles.setObjectName("labelProfiles")
        self.horizontalLayout.addWidget(self.labelProfiles)
        self.comboBoxProfiles = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxProfiles.sizePolicy().hasHeightForWidth())
        self.comboBoxProfiles.setSizePolicy(sizePolicy)
        self.comboBoxProfiles.setObjectName("comboBoxProfiles")
        self.horizontalLayout.addWidget(self.comboBoxProfiles)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBoxCurrentProfile = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxCurrentProfile.setObjectName("comboBoxCurrentProfile")
        self.horizontalLayout_2.addWidget(self.comboBoxCurrentProfile)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonUpdateProfile = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonUpdateProfile.setObjectName("pushButtonUpdateProfile")
        self.horizontalLayout_4.addWidget(self.pushButtonUpdateProfile)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listWidgetAvailableMods = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidgetAvailableMods.setDragEnabled(True)
        self.listWidgetAvailableMods.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetAvailableMods.setDefaultDropAction(QtCore.Qt.DropAction.MoveAction)
        self.listWidgetAvailableMods.setObjectName("listWidgetAvailableMods")
        self.horizontalLayout_3.addWidget(self.listWidgetAvailableMods)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.listWidgetSelectedMods = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidgetSelectedMods.setDragEnabled(True)
        self.listWidgetSelectedMods.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetSelectedMods.setDefaultDropAction(QtCore.Qt.DropAction.MoveAction)
        self.listWidgetSelectedMods.setObjectName("listWidgetSelectedMods")
        self.horizontalLayout_3.addWidget(self.listWidgetSelectedMods)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 19))
        self.menubar.setObjectName("menubar")
        self.menuGame = QtWidgets.QMenu(self.menubar)
        self.menuGame.setObjectName("menuGame")
        self.menu_Preferences = QtWidgets.QMenu(self.menubar)
        self.menu_Preferences.setObjectName("menu_Preferences")
        self.menuMods = QtWidgets.QMenu(self.menubar)
        self.menuMods.setObjectName("menuMods")
        self.menuProfiles = QtWidgets.QMenu(self.menubar)
        self.menuProfiles.setObjectName("menuProfiles")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionAdd_Game = QtGui.QAction(MainWindow)
        self.actionAdd_Game.setObjectName("actionAdd_Game")
        self.action_Select_Game = QtGui.QAction(MainWindow)
        self.action_Select_Game.setObjectName("action_Select_Game")
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.actionAdd_api_key = QtGui.QAction(MainWindow)
        self.actionAdd_api_key.setObjectName("actionAdd_api_key")
        self.action_API_key = QtGui.QAction(MainWindow)
        self.action_API_key.setObjectName("action_API_key")
        self.action_Settingd = QtGui.QAction(MainWindow)
        self.action_Settingd.setObjectName("action_Settingd")
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAdd_Mod = QtGui.QAction(MainWindow)
        self.actionAdd_Mod.setObjectName("actionAdd_Mod")
        self.actionManage_Profiles = QtGui.QAction(MainWindow)
        self.actionManage_Profiles.setObjectName("actionManage_Profiles")
        self.menuGame.addAction(self.actionAdd_Game)
        self.menuGame.addAction(self.action_Quit)
        self.menu_Preferences.addAction(self.actionSettings)
        self.menuMods.addAction(self.actionAdd_Mod)
        self.menuProfiles.addAction(self.actionManage_Profiles)
        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuProfiles.menuAction())
        self.menubar.addAction(self.menuMods.menuAction())
        self.menubar.addAction(self.menu_Preferences.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QT Nexus Mod Manager"))
        self.labelGames.setText(_translate("MainWindow", "Select a game"))
        self.labelProfiles.setText(_translate("MainWindow", "Select a profile"))
        self.label.setText(_translate("MainWindow", "Select current profile"))
        self.pushButtonUpdateProfile.setText(_translate("MainWindow", "Update profile"))
        self.label_2.setText(_translate("MainWindow", "Available plugins"))
        self.label_3.setText(_translate("MainWindow", "Selected plugins"))
        self.listWidgetAvailableMods.setSortingEnabled(True)
        self.menuGame.setTitle(_translate("MainWindow", "&Game"))
        self.menu_Preferences.setTitle(_translate("MainWindow", "&Preferences"))
        self.menuMods.setTitle(_translate("MainWindow", "&Mods"))
        self.menuProfiles.setTitle(_translate("MainWindow", "Profiles"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionAdd_Game.setText(_translate("MainWindow", "&Add Game"))
        self.action_Select_Game.setText(_translate("MainWindow", "&Select Game"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.actionAdd_api_key.setText(_translate("MainWindow", "Add api key"))
        self.action_API_key.setText(_translate("MainWindow", "&API key"))
        self.action_Settingd.setText(_translate("MainWindow", "&Settingd"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionAdd_Mod.setText(_translate("MainWindow", "Add Mod"))
        self.actionManage_Profiles.setText(_translate("MainWindow", "Manage Profiles"))
