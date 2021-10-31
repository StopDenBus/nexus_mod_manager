import typing

from PyQt6 import QtWidgets

from util import getWidgetText
from ui.dlgManageProfiles import Ui_dlgManageProfiles

class dlgManageProfiles(QtWidgets.QDialog, Ui_dlgManageProfiles):
    def __init__(self, parent: typing.Optional[QtWidgets.QDialog] = None) -> None:
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.__profile_edit = QtWidgets.QLineEdit()
        self.formLayoutManageProfiles.addRow("Add a profile name", self.__profile_edit)
    
    def getProfileName(self) -> str:
        return getWidgetText(self.formLayoutManageProfiles, self.__profile_edit)