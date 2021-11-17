import keyring
import platform

if platform.system() == 'Windows':
    from keyring.backends import Windows

class Keyring():
    def __init__(self) -> None:
        self.__servicename = "nexus_mod_manager"
        
    def set_api_key(self, key) -> bool:
        try:
            keyring.set_password(self.__servicename, "api", key)
        except:
            return False
        return True
        
    def get_api_key(self) -> str:
        try:
            return keyring.get_password(self.__servicename, "api")
        except:
            return ""