# -------------------------------
#
# Folder: app
# Filename: player_list.py
# Author: Ayano SASAKIDO
# Version 0.0
# Created: 08/08/2025
#
# -------------------------------

from app.player import Player
from app.player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self.head = None
        self.tail = None

    """Return true when the list is empty"""
    def is_empty(self):
        if self.head is None:
            return True
        return False

    """insert a new node at the head of the list"""
    def insert(self, uid, name):
        new_player = Player(uid, name)
        new_node = PlayerNode(new_player)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node



    def display(self):
        players = []
        current = self.head
        while current:
            players.append(current.player.info)
            current = current.next
        print(players)


list = PlayerList()
list.insert(1, "test1")
list.display()


