import typing

from PyQt6 import QtWidgets

from util import getWidgetText
from ui.dlgSettings import Ui_dlgSettings

class dlgSettings(QtWidgets.QDialog, Ui_dlgSettings):
    def __init__(self, parent: typing.Optional[QtWidgets.QDialog] = None) -> None:
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.__api_line_edit = QtWidgets.QLineEdit()
        self.formLayoutSettings.addRow("Nexus Mod API Key", self.__api_line_edit)
    
    def getApiKey(self) -> str:
        return getWidgetText(self.formLayoutSettings, self.__api_line_edit)