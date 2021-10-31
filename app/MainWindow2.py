from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

from nxmLink import nxmLink, nxmLinkNotParseable
from ui.MainWindow2 import Ui_MainWindow
from util import getFileNameFromDownloadLink, FileNameNotFoundExeption, VersionNotFoundException, getVersionFromFileName

from Keyring import Keyring
from Games import Games
from Mods import ModAlreadyExist, ModVersionAlreadyExist, Mods
from NexusModsAPI import *
from pathlib import Path
from pyunpack import Archive

import pprint
import re

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        
        self.__api = NexusModsAPI()
        self.__config = {}
        self.__games = Games()
        self.__keyring = Keyring()
        self.__mods = Mods()
                
        self.GetConfiguration()
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        
        for game in self.__games.GetGames():
            self.comboBoxGames.addItem(game)
            self.listWidgetGames.addItem(game)
                
        self.comboBoxGames.model().sort(0)
        self.comboBoxGames.currentIndexChanged.connect(self.UpdateApplication)
        self.comboBoxGames.setCurrentIndex(0)
        
        self.listWidgetGames.sortItems(QtCore.Qt.SortOrder.AscendingOrder)
        
        self.__mods.GetMods(self.comboBoxGames.currentText())
        
        self.lineEditNewGame.returnPressed.connect(self.AddGame)
        
        self.pushButtonRemoveGames.clicked.connect(self.RemoveGame)
        
        self.UpdateApplication(self.comboBoxGames.currentText())
        
    def handleMessage(self, message: str) -> None:
        # nxm://valheim/mods/92/files/6559?key=RO03hQ1-2FVhF1DohcN0Ww&expires=1633881645&user_id=78204018
        if message.startswith('nxm'):
            # parse nxm link
            try:                
                nxm = nxmLink(message)
                nxm.ParseLink()
            except nxmLinkNotParseable:
                QtWidgets.QMessageBox.critical(self, "Parse nxm link error", f"Could not parse {message} as a nxm link.")
                return
            
            # get downloadlink for mod
            try:
                download_link = self.__api.getDownloadLink(nxm=nxm)
            except Exception as ex:
                QtWidgets.QMessageBox.critical(self, "Get download link", f"Could not get download link:\n{str(ex)}")
                return
            
            # get file name from link
            try:
                file_name = getFileNameFromDownloadLink(download_link)
            except FileNameNotFoundExeption:
                QtWidgets.QMessageBox.critical(self, "Get download link", f"Could not get filename from link:\n{str(download_link)}")
                return                
                
            # get mod version from file name
            try:
                mod_version = getVersionFromFileName(file_name)
            except VersionNotFoundException:
                QtWidgets.QMessageBox.critical(self, "Get mod version", f"Could not get mod version from filename:\n{str(file_name)}")
                return                   
                
            download_response = requests.get(download_link, stream=True)
            if download_response.status_code == 200:
                try:
                    self.__mods.AddMod(nxm.GetGame(), nxm.GetModID(), {})
                except ModAlreadyExist:
                    pass
                try:
                    self.__mods.AddModVersion(nxm.GetGame(), nxm.GetModID(), mod_version)
                except ModVersionAlreadyExist:
                    QtWidgets.QMessageBox.critical(self, "mod version", f"Mod version {mod_version} already exists.")
                response_headers = download_response.headers
                content_length = response_headers['Content-Length']
                mod_directory =  self.__mods.GetModDirectory(nxm.GetGame(), nxm.GetModID(), mod_version)
                with open(f"{mod_directory}/{file_name}", 'wb') as f:
                    for chunk in download_response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                if Path(f"{mod_directory}/{file_name}").is_file():
                    try:
                        Archive(f"{mod_directory}/{file_name}").extractall(directory=mod_directory)
                    except Exception as ex:
                        QtWidgets.QMessageBox.critical(self, "Extract archive", f"Could not extract archive {mod_directory}/{file_name}:\n{str(ex)}")
                        return
                self.statusBar().showMessage(f"Mod {nxm.GetModID()} for game {nxm.GetGame()} added.")
        
    def GetConfiguration(self) -> None:
        print("GetConfiguration")
        configuration = QtCore.QSettings('gusek', 'nexus-mod-manager')
        self.__config = configuration.value('config', {})
        self.__api.setApiKey(self.__keyring.get_api_key())
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(self.__config)
        
        
    def SaveConfiguration(self) -> None:
        configuration = QtCore.QSettings('gusek', 'nexus-mod-manager')
        configuration.setValue('config', self.__config)
        
    def UpdateApplication(self, current_game: str = None) -> None:
        if current_game == None:
            current_game = self.comboBoxGames.currentText()
            
        if not current_game == '':
            pass
    
    def AddGame(self) -> None:
        game = self.lineEditNewGame.text()        
        if game in self.__games.GetGames():
            QtWidgets.QMessageBox.information(self, "Add a game", f"Game {game} already added.", QtWidgets.QMessageBox.StandardButton.Ok)
        else:
            self.__games.AddGame(game=game)
        
        self.lineEditNewGame.setText("")
        self.listWidgetGames.addItem(game)
        self.listWidgetGames.sortItems(QtCore.Qt.SortOrder.AscendingOrder)
        
    def RemoveGame(self) -> None:
        print("## RemoveGame")
        for game in self.listWidgetGames.selectedItems():
            self.__games.RemoveGame(game=game.text())
        self.listWidgetGames.takeItem(self.listWidgetGames.indexFromItem(game).row())
        
    def closeApp(self):
        
        self.SaveConfiguration()
        self.close()