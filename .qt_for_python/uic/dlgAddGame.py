# Form implementation generated from reading ui file '/home/micha/prog/python/nexus_mod_manager/src/app/uic/dlgAddGame.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgAddGame(object):
    def setupUi(self, dlgAddGame):
        dlgAddGame.setObjectName("dlgAddGame")
        dlgAddGame.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlgAddGame)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(dlgAddGame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 371, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayoutAddGame = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayoutAddGame.setContentsMargins(0, 0, 0, 0)
        self.formLayoutAddGame.setObjectName("formLayoutAddGame")

        self.retranslateUi(dlgAddGame)
        self.buttonBox.accepted.connect(dlgAddGame.accept)
        self.buttonBox.rejected.connect(dlgAddGame.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgAddGame)

    def retranslateUi(self, dlgAddGame):
        _translate = QtCore.QCoreApplication.translate
        dlgAddGame.setWindowTitle(_translate("dlgAddGame", "Add a game"))
