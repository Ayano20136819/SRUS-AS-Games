# -------------------------------
#
# Folder: app
# Filename: player_node
# Author: Ayano SASAKIDO
# Version 0.0
# Created: 
#
# -------------------------------

from player import Player

class PlayerNode:
    def __init__(self, _player: Player, _next = None, _pre = None):
        self._player = _player
        self._next = _next
        self._pre = _pre

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player_info):
        self._player = player_info

    @property
    def next(self):
        return self._next

    @property
    def pre(self):
        return self._pre

    def key(self):
        return self.player.uid

    def __str__(self):
        return (f"Player Name: {self._player.name}, NextNode: {self.next}, PreviousNode:"
                f" {self.pre}")




player = Player("2","Test")
print(player)
node = PlayerNode(player)
print(node)