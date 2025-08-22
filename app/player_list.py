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



    def is_empty(self):
        """Return true when the list is empty"""
        if self.head is None:
            return True
        return False

    def insert(self, uid, name):
        """insert a new node at the head of the list"""
        new_player = Player(uid, name)
        new_node = PlayerNode(new_player)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node


    def insert_tail(self, uid, name):
        """insert an item at the tail of the list"""
        new_player = Player(uid, name)
        new_node = PlayerNode(new_player)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def delete_head(self):
        """delete a node from the head of the list"""
        if self.is_empty():
            return
        current_head = self.head
        current_head.prev = None
        self.head = current_head.next

    def delete_tail(self):
        """delete an item from the tail of a list"""
        if self.is_empty():
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None



    def delete_key(self, key):
        """delete an item from the linked list based on its key
                (key = uid)
            """
        if self.is_empty():
            return

        current = self.head

        # search for node to delete
        while current is not None and current.player.uid != key:
            current = current.next

        if current is None:
            return

        # delete head
        if current.prev is None:
            self.head = current.next
            if self.head:
                current.next.prev = None

        # delete tail
        elif current.next is None:
            self.tail = current.prev
            if self.tail:
                current.prev.next = None

        # node found and update pointers
        else:
            current.prev.next = current.next
            current.next.prev = current.prev


    def display(self, forward=True):
        """display list from head to tail (forward=True),
               from tail to head (forward=False)"""
        players = []
        if forward:
            current = self.head
            while current:
                players.append(current.player.info)
                current = current.next
            print(players)
        else:
            current = self.tail
            while current:
                players.append(current.player.info)
                current = current.prev
            print(players)





