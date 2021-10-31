import requests
from requests.models import Response

from nxmLink import nxmLink

class NexusModNoAPIException(Exception):
    pass

class NexusModRequestExeption(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class NexusModsAPI():
    def __init__(self) -> None:
        self.__api_key = None
        
    def setApiKey(self, key: str) -> None:
        self.__api_key = key
        
    def getInformation(self, url) -> Response:
        
        if self.__api_key == None:
            raise NexusModNoAPIException
        
        headers = {
            "accept": "application/json",
            "apikey": self.__api_key
        }
        return requests.get(url=url, headers=headers)
        
    def getGameInformation(self, game: str) -> Response:
        
        url = f"https://api.nexusmods.com/v1/games/{game}.json"
        
        try:
            response = self.getInformation(url=url)
        except NexusModNoAPIException:
            raise NexusModNoAPIException
        except Exception as ex:
            raise NexusModRequestExeption(ex)
        
        return response
    
    def getModInformation(self, game: str, mod_id: str) -> Response:
        
        url = f"https://api.nexusmods.com/v1/games/{game}/mods/{mod_id}.json"
        
        try:
            response = self.getInformation(url=url)
        except NexusModNoAPIException:
            raise NexusModNoAPIException
        except Exception as ex:
            raise NexusModRequestExeption(ex)
        
        return response
    
    def getDownloadLink(self, nxm: nxmLink) -> str:
        print('## NexusModsAPI::getDownloadLink')
        url = f"https://api.nexusmods.com/v1/games/{nxm.GetGame()}/mods/{nxm.GetModID()}/files/{nxm.GetFileID()}/download_link.json?key={nxm.GetKey()}&expires={nxm.GetExpire()}"
        print(f"## NexusModsAPI::getDownloadLink url: {url}")
        try:
            response = self.getInformation(url=url)
        except Exception as ex:
            raise ex
                
        if response.status_code == 200:
        
            result = response.json()
        
            if 'URI' in result[0]:
                return result[0]['URI']
            
        raise Exception(response.text)
        