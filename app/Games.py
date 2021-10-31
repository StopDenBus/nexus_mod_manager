import os
import shutil

from PyQt6.QtCore import QStandardPaths
from pathlib import Path

class Games():

    def __init__(self) -> None:
        self.__application_directory = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppDataLocation)
        self.InitDirectories()
        
    def InitDirectories(self) -> None:
        
        Path(self.__application_directory).mkdir(parents=True, exist_ok=True)
        
    def AddGame(self, game: str) -> None:
        
        Path(f"{self.__application_directory}/{game}").mkdir(parents=True, exist_ok=True)
            
    def GetGames(self) -> list:
        
        return [ f.name for f in os.scandir(self.__application_directory) if f.is_dir() ]
    
    def RemoveGame(self, game: str) -> None:
        
        shutil.rmtree(f"{self.__application_directory}/{game}")