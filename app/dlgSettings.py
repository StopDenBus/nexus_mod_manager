import typing

from PyQt6 import QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices

from util import getWidgetText
from ui.dlgSettings import Ui_dlgSettings

class dlgSettings(QtWidgets.QDialog, Ui_dlgSettings):
    def __init__(self, parent: typing.Optional[QtWidgets.QDialog] = None) -> None:
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.__link_button = QtWidgets.QCommandLinkButton("Nexus account", self)
        self.__link_button.clicked.connect(self.open_nexus_myaccount)
        self.__api_line_edit = QtWidgets.QLineEdit()
        self.formLayoutSettings.addRow("Nexus my account site", self.__link_button)
        self.formLayoutSettings.addRow("Nexus Mod API Key", self.__api_line_edit)
    
    def getApiKey(self) -> str:
        return getWidgetText(self.formLayoutSettings, self.__api_line_edit)
    
    def open_nexus_myaccount(self):
        QDesktopServices.openUrl(QUrl('https://www.nexusmods.com/users/myaccount?tab=api'))
        