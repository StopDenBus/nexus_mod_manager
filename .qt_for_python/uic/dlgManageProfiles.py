# Form implementation generated from reading ui file '/home/micha/prog/python/nexus_mod_manager/app/uic/dlgManageProfiles.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgManageProfiles(object):
    def setupUi(self, dlgManageProfiles):
        dlgManageProfiles.setObjectName("dlgManageProfiles")
        dlgManageProfiles.resize(382, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlgManageProfiles)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(dlgManageProfiles)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayoutManageProfiles = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayoutManageProfiles.setContentsMargins(0, 0, 0, 0)
        self.formLayoutManageProfiles.setObjectName("formLayoutManageProfiles")

        self.retranslateUi(dlgManageProfiles)
        self.buttonBox.accepted.connect(dlgManageProfiles.accept)
        self.buttonBox.rejected.connect(dlgManageProfiles.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgManageProfiles)

    def retranslateUi(self, dlgManageProfiles):
        _translate = QtCore.QCoreApplication.translate
        dlgManageProfiles.setWindowTitle(_translate("dlgManageProfiles", "Manage Profiles"))
