from PyQt6 import QtCore, QtGui, QtWidgets

from dlgAddGame import dlgAddGame
from dlgAddMod import dlgAddMod
from dlgManageProfiles import dlgManageProfiles
from dlgSettings import dlgSettings

from ui.MainWindow import Ui_MainWindow

from Keyring import Keyring
from NexusModsAPI import *

import pprint

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.__keyring = Keyring()
        self.__api = NexusModsAPI()
        self.__games = {}
        self.actionAdd_Game.triggered.connect(self.ShowAddGame)
        self.actionAdd_Mod.triggered.connect(self.ShowAddMod)
        self.actionManage_Profiles.triggered.connect(self.ShowManageProfiles)
        self.action_Quit.triggered.connect(self.CloseApp)
        self.actionSettings.triggered.connect(self.ShowSettings)
        self.comboBoxGames.currentIndexChanged.connect(self.UpdateGame)
        self.comboBoxProfiles.currentTextChanged.connect(self.UpdateProfiles)
        
        self.GetConfiguration()
        self.UpdateStatusBar()
        
        
    def GetConfiguration(self) -> None:
        configuration = QtCore.QSettings('gusek', 'nexus-mod-manager')
        self.__games = configuration.value('games', {})
        self.InitComboBoxGame()
        self.__api.setApiKey(self.__keyring.get_api_key())
        
    def SaveConfiguration(self) -> None:
        configuration = QtCore.QSettings('gusek', 'nexus-mod-manager')
        configuration.setValue('games', self.__games)
        print(configuration.fileName())
        
    def ShowAddGame(self) -> None:
        add_game_dialog = dlgAddGame(self, )
        if add_game_dialog.exec():
            game = add_game_dialog.getGameName()
            try:
                response: Response = self.__api.getGameInformation(game)
            except NexusModNoAPIException:
                QtWidgets.QMessageBox.critical(self, "No API key", "API key for Nexusmod not set.")
                return
            except NexusModRequestExeption as ex:
                QtWidgets.QMessageBox.critical(self, "Unknown error", str(ex))
                return
            
            if response.status_code == 200:                  
                if not game in self.__games:
                    self.__games[game] = {}
                    self.__games[game]['data'] = response.json()
                    self.__games[game]['mods'] = {}
                    self.__games[game]['profiles'] = {}
                    self.__games[game]['current_profile'] = None
                    self.SaveConfiguration()
                    self.statusBar().showMessage(f"Game {game} added.")
                    try:
                        self.comboBoxGames.currentIndexChanged.disconnect(self.UpdateGame)
                    except:
                        pass
                    self.comboBoxGames.addItem(game)
                    self.comboBoxGames.model().sort(0)
                    index = self.comboBoxGames.findText(game)
                    self.comboBoxGames.currentIndexChanged.connect(self.UpdateGame)
                    self.comboBoxProfiles.setCurrentIndex(index)
            elif response.status_code == 404:
                QtWidgets.QMessageBox.critical(self, "Game not found", f"Game {game} does not exists at Nexusmod")
                return
            
    def ShowAddMod(self) -> None:
        game = self.comboBoxGames.currentText()
        add_mod_dialog = dlgAddMod(self)
        add_mod_dialog.labelGame.setText(f"Add mod to game {game}")
        if add_mod_dialog.exec():
            mod_id = add_mod_dialog.getModID()            
            try:
                response: Response = self.__api.getModInformation(game=game, mod_id=mod_id)
            except NexusModNoAPIException:
                QtWidgets.QMessageBox.critical(self, "No API key", "API key for Nexusmod not set.")
                return
            except NexusModRequestExeption as ex:
                QtWidgets.QMessageBox.critical(self, "Unknown error", str(ex))
                return 

            if response.status_code == 200:                  
                if not mod_id in self.__games[game]['mods']:
                    self.__games[game]['mods'][mod_id] = response.json()
                    self.SaveConfiguration()
                else:
                    mod_name = self.__games[game]['mods'][mod_id]['name']
                    QtWidgets.QMessageBox.warning(self, "Mod already added", f"Mod {mod_name} already added.")
                self.UpdateProfiles()
            elif response.status_code == 404:
                QtWidgets.QMessageBox.critical(self, "Mod not found", f"Mod with id {mod_id} does not exists at Nexusmod.")
                return
            
    def ShowManageProfiles(self) -> None:
        game = self.comboBoxGames.currentText()
        manage_profiles_dialog = dlgManageProfiles(self)
        if manage_profiles_dialog.exec():
            profile_name = manage_profiles_dialog.getProfileName()
            self.__games[game]['profiles'][profile_name] = {}
            self.__games[game]['profiles'][profile_name]['mods'] = ()
            self.comboBoxProfiles.currentTextChanged.disconnect(self.UpdateProfiles)
            self.comboBoxProfiles.addItem(profile_name)
            self.comboBoxProfiles.model().sort(0)
            index = self.comboBoxProfiles.findText(profile_name)
            self.comboBoxProfiles.currentTextChanged.connect(self.UpdateProfiles)
            self.comboBoxProfiles.setCurrentIndex(index)
            self.SaveConfiguration()
            self.statusBar().showMessage(f"Profile {profile_name} for {game} added.")
                           
                        
    def ShowSettings(self):
        settings = dlgSettings(self)
        result = settings.exec()
        if result:
            api_key = settings.getApiKey()
            if api_key != "":
                if self.__keyring.set_api_key(api_key):
                    self.__api.setApiKey(self.__keyring.get_api_key())
                    self.statusBar().showMessage('Nexusmod API key updated.')
                    
    def InitComboBoxGame(self):
        print("InitComboBoxGame")
        self.comboBoxGames.currentIndexChanged.disconnect(self.UpdateGame)
        if len(self.__games.keys()) > 0:
            for game in self.__games.keys():
                self.comboBoxGames.addItem(game)
                self.comboBoxGames.model().sort(0)
                self.comboBoxGames.currentIndexChanged.connect(self.UpdateGame)
                self.comboBoxGames.setCurrentIndex(0)
                self.UpdateGame()
                    
    def UpdateGame(self):
        print("UpdateGame")
        # get selected game
        currentGame = self.comboBoxGames.currentText()
        print(f"current game: {currentGame}")
        if currentGame in self.__games:
            self.comboBoxProfiles.clear()
            self.comboBoxCurrentProfile.clear()
            # update profiles combo box if there are profiles
            if len(self.__games[currentGame]['profiles']) > 0:
                print("UpdateGame: update profiles combobox")
                self.comboBoxProfiles.clear()
                for profile in self.__games[currentGame]['profiles'].keys():
                    self.comboBoxProfiles.addItem(profile)
                self.comboBoxProfiles.model().sort(0)
                # get current profile for selected game
                currentProfile = self.__games[currentGame]['current_profile']
                # select current profile in profiles combox box if set
                if currentProfile != None:
                    index = self.comboBoxProfiles.findText(currentProfile)
                    self.comboBoxProfiles.setCurrentIndex(index)
                else:
                    self.comboBoxProfiles.setCurrentIndex(0)
                # update current profile combo box
                
                for profile in self.__games[currentGame]['profiles'].keys():
                    self.comboBoxCurrentProfile.addItem(profile)
                self.comboBoxCurrentProfile.model().sort(0)
                # select current profile in profiles combox box if set
                if currentProfile != None:
                    index = self.comboBoxCurrentProfile.findText(currentProfile)
                    self.comboBoxCurrentProfile.setCurrentIndex(index)
                else:
                    self.comboBoxCurrentProfile.setCurrentIndex(0)    
      
    def UpdateProfiles(self) -> None:
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.__games)
        print("UpdateProfiles")
        currentProfile = self.comboBoxProfiles.currentText()
        currentGame = self.comboBoxGames.currentText()
        print(f"UpdateProfiles current profile: {currentProfile}")
        
        if currentProfile in self.__games[currentGame]['profiles']:
            self.listWidgetSelectedMods.clear()
            self.listWidgetAvailableMods.clear()
            for mod in self.__games[currentGame]['mods'].keys():
                if mod in self.__games[currentGame]['profiles'][currentProfile]['mods']:
                    self.listWidgetSelectedMods.addItem(self.__games[currentGame]['mods'][mod]['name'])
                else:
                    self.listWidgetAvailableMods.addItem(self.__games[currentGame]['mods'][mod]['name'])        
        
    def UpdateStatusBar(self):
        if self.__keyring.get_api_key() == None:
            self.statusBar().showMessage('Nexusmod API key is not available. Setup a key via Preferences->Settings.')
        else:
            self.statusBar().showMessage('Nexusmod API key found.')
            
    def CloseApp(self):
        print("Closing app.")
        self.close()