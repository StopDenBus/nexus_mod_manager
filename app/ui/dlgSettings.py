# Form implementation generated from reading ui file '/home/micha/prog/python/nexus_mod_manager/app/uic/dlgSettings.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgSettings(object):
    def setupUi(self, dlgSettings):
        dlgSettings.setObjectName("dlgSettings")
        dlgSettings.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlgSettings)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(dlgSettings)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 371, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayoutSettings = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayoutSettings.setContentsMargins(0, 0, 0, 0)
        self.formLayoutSettings.setObjectName("formLayoutSettings")

        self.retranslateUi(dlgSettings)
        self.buttonBox.accepted.connect(dlgSettings.accept)
        self.buttonBox.rejected.connect(dlgSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgSettings)

    def retranslateUi(self, dlgSettings):
        _translate = QtCore.QCoreApplication.translate
        dlgSettings.setWindowTitle(_translate("dlgSettings", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgSettings = QtWidgets.QDialog()
    ui = Ui_dlgSettings()
    ui.setupUi(dlgSettings)
    dlgSettings.show()
    sys.exit(app.exec())