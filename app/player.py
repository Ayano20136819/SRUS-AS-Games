# -------------------------------
#
# Folder: app
# Filename: player.py
# Author: Ayano SASAKIDO
# Version 0.0
# Created: 05/08/2025
#
# -------------------------------

class Player:
    def __init__(self, _uid:str, _name:str):
        self.uid =_uid
        self.name =_name

    def uid(self):
        return self.uid

    def name(self):
        return self.name

    def __str__(self):
        return f"ID[{self.uid}]: {self.name}"