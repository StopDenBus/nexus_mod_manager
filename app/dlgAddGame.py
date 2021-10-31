import typing

from PyQt6 import QtWidgets

from util import getWidgetText
from ui.dlgAddGame import Ui_dlgAddGame

class dlgAddGame(QtWidgets.QDialog, Ui_dlgAddGame):
    def __init__(self, parent: typing.Optional[QtWidgets.QDialog] = None) -> None:
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.__game_line_edit: QtWidgets.QLineEdit = QtWidgets.QLineEdit()
        self.formLayoutAddGame.addRow("Game name to add", self.__game_line_edit)
        
    def getGameName(self) -> str:
        return getWidgetText(self.formLayoutAddGame, self.__game_line_edit)