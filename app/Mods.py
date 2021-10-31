import json
import os
import re
import requests

from PyQt6.QtCore import QStandardPaths
from pathlib import Path

from nxmLink import nxmLink
from NexusModsAPI import NexusModsAPI

class GameNotFoundException(Exception):
    pass

class ModNotFoundException(Exception):
    pass

class ModAlreadyExist(Exception):
    pass

class ModVersionAlreadyExist(Exception):
    pass

class Mods():
        
    def __init__(self) -> None:
        self.__application_directory = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppDataLocation)
        print(f"application_directory: {self.__application_directory}")
        
    def AddMod(self, game: str, mod_id: int, mod_info: dict) -> None:
        
        if not Path(f"{self.__application_directory}/{game}").is_dir():
            raise GameNotFoundException
        
        if Path(f"{self.__application_directory}/{game}/{mod_id}").is_dir():
            raise ModAlreadyExist
        
        Path(f"{self.__application_directory}/{game}/{mod_id}").mkdir(parents=False, exist_ok=False)
        
        with open(f"{self.__application_directory}/{game}/{mod_id}/info.json", 'w') as f:
            json.dump(mod_info, f)
            
    def AddModVersion(self, game: str, mod_id: int, version: str) -> None:
        
        if not Path(f"{self.__application_directory}/{game}").is_dir():
            raise GameNotFoundException
        
        if not Path(f"{self.__application_directory}/{game}/{mod_id}").is_dir():
            raise ModNotFoundException
        
        if Path(f"{self.__application_directory}/{game}/{mod_id}/{version}").is_dir():
            raise ModVersionAlreadyExist
        
        Path(f"{self.__application_directory}/{game}/{mod_id}/{version}").mkdir(parents=False, exist_ok=False)
        
    def GetModVersions(self, game: str, mod_id: int) -> list:
        
        return [ f.name for f in os.scandir(f"{self.__application_directory}/{game}/{mod_id}") if f.is_dir() ]
    
    def GetModDirectory(self, game: str, mod_id: int, version: str) -> str:
        
        return f"{self.__application_directory}/{game}/{mod_id}/{version}"
    
    def GetMods(self, game:str) -> list:
        print(f"Getting mods for game {game}")
        
    def DownloadMod(self, link: nxmLink, api: NexusModsAPI) -> None:
        pass
            
        
