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
    def __init__(self, uid:str, name:str, score=0):
        self._uid = uid
        self._name = name
        self._score = score
        self.info = (uid, name)

    @property
    def uid(self):
        #print("getter for uid called")
        return self._uid

    @uid.setter
    def uid(self, value:str):
        #print("setter for uid called")
        self._uid = value

    @property
    def name(self):
        #rint("getter for name called")
        return self._name

    @name.setter
    def name(self, value:str):
        #print("setter for name called")
        self._name = value

    @property
    def score(self):
        #print("getter for score called")
        return self._score

    @score.setter
    def score(self, value: int):
        if value < 0:
            raise ValueError
        self._score = value

    # def __str__(self):
    #     return f"ID[{self.uid}]: {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, uid={self.uid}, score={self.score})"

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.uid == other.uid


# player = Player(1, "test")
# player.score = -1
# print(player)