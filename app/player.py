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
    def __init__(self, uid:str, name:str, hash=None):
        self._uid =uid
        self._name =name
        self.info = (uid, name)

    @property
    def uid(self):
        print("getter for uid called")
        return self._uid

    @uid.setter
    def uid(self, value: str):
        print("setter for uid called")
        self._uid = value

    @property
    def name(self):
        print("getter for name called")
        return self._name

    @name.setter
    def name(self, value: str):
        print("setter for name called")
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
