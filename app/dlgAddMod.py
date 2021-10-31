import typing

from PyQt6 import QtGui, QtWidgets

from util import getWidgetText
from ui.dlgAddMod import Ui_dlgAddMod

class dlgAddMod(QtWidgets.QDialog, Ui_dlgAddMod):
    def __init__(self, parent: typing.Optional[QtWidgets.QDialog] = None) -> None:
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.__mod_line_edit: QtWidgets.QLineEdit = QtWidgets.QLineEdit()
        validator = QtGui.QIntValidator()
        self.__mod_line_edit.setValidator(validator)
        self.formLayoutAddMod.addRow("Mod id to add", self.__mod_line_edit)
        
    def getModID(self) -> str:
        return getWidgetText(self.formLayoutAddMod, self.__mod_line_edit) 