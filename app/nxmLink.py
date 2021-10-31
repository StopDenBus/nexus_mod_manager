import re

class nxmLinkNotParseable(Exception):
    pass

class nxmLink():
    def __init__(self, link: str) -> None:
        self.__link: str = link
        self.__game: str = None
        self.__mod_id: str = None
        self.__file_id: str = None
        self.__key: str = None
        self.__expire: str = None
        self.__user_id: str = None
        
    def ParseLink(self) -> None:
        pattern = re.compile('nxm://(?P<game>.*)/mods/(?P<mod_id>\d+)/files/(?P<file_id>\d+)\?key=(?P<key>.*)expires=(?P<expire>\d+)&user_id=(?P<user_id>\d+)')
        match = pattern.match(self.__link)
        if match:
            self.__game = match.group('game')
            self.__mod_id = match.group('mod_id')
            self.__file_id = match.group('file_id')
            self.__key = match.group('key')
            self.__expire = match.group('expire')
            self.__user_id = match.group('user_id')
        else:
            raise nxmLinkNotParseable
        
    def GetGame(self) -> str:
        return self.__game
    
    def GetModID(self) -> str:
        return self.__mod_id
    
    def GetFileID(self) -> str:
        return self.__file_id
    
    def GetKey(self) -> str:
        return self.__key
    
    def GetExpire(self) -> str:
        return self.__expire
    
    def GetUserID(self) -> str:
        return self.__user_id
