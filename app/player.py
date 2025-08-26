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
    def __init__(self, _uid:str, _name:str, hash=None):
        self.uid =_uid
        self.name =_name
        self.info = (_uid, _name)

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value:str):
        self._uid = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value:str):
        self._name = value

    def __str__(self):
        return f"ID[{self.uid}]: {self.name}"

    def __hash__(self):
        return self.my_hash(self.uid)

    @classmethod
    def my_hash(cls, key: str) -> int:
        try:
            return int(key)
        except ValueError:
            return hash(key)

    def __eq__(self, other):
        return isinstance(other, Player) and self.uid == other.uid
