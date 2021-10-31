import re

from PyQt6 import QtWidgets

class FileNameNotFoundExeption(Exception):
    pass

class VersionNotFoundException(Exception):
    pass

def getWidgetText(formLayout: QtWidgets.QFormLayout, lineEdit: QtWidgets.QLineEdit) -> str:
    i, j  =  formLayout.getWidgetPosition(lineEdit)
    widget_item = formLayout.itemAt(i, QtWidgets.QFormLayout.ItemRole(j))
    widget = widget_item.widget()
    return widget.text()

def getFileNameFromDownloadLink(link: str) -> str:
    pattern = re.compile('https://.*/\w+/\d+/\d+/(?P<file_name>.*)\?md5=(?P<md5>.*)&expires=\d+&user_id=\d+')
    match = pattern.match(link)
    if match:
        return match.group('file_name')
    
    raise FileNameNotFoundExeption

def getVersionFromFileName(file_name: str) -> str:
    pattern = re.compile('.*-\d+-(?P<mod_version>\d+-\d+-\d+)-\d+\.\w+')
    match = pattern.match(file_name)
    if match:
        version = match.group('mod_version')
        return '.'.join(version.split('-'))
          
    raise VersionNotFoundException