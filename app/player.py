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
    def __init__(self, uid:str, name:str):
        self._uid =uid
        self._name =name
        self.info = (uid, name)

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value: str):
        self._uid = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    def __str__(self):
        return f"ID[{self.uid}]: {self.name}"

    def __hash__(self):
        return self.my_hash(self.uid)

    @staticmethod
    def my_hash(key: str) -> int:
        try:
            return int(key)
        except ValueError:
            return hash(key)

    def __eq__(self, other):
        """
        In this case, isinstance is used,
        so it returns False when comparing objects do not have uid.
        If isinstance is omitted, it returns an AttributeError.
        """
        return isinstance(other, Player) and self.uid == other.uid


