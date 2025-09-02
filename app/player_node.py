# -------------------------------
#
# Folder: app
# Filename: player_node
# Author: Ayano SASAKIDO
# Version 0.0
# Created: 
#
# -------------------------------

from app.player import Player

class PlayerNode:
    def __init__(self, player: Player, next = None, prev = None):
        self._player = player
        self._next = next
        self._prev = prev

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player_info):
        self._player = player_info

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_info):
        self._next = next_info

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_info):
        self._prev = prev_info

    def key(self):
        return str(self.player.uid)

    def __str__(self):
        return (f"Player Name: {self._player.name}, NextNode: {self.next}, PreviousNode:"
                f" {self.prev}")



