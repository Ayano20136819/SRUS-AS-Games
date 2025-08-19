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

    """find tail from the list"""
    def find_tail(self):
        if not self.head:
            return None
        current = self.head
        while current.next is not None:
            current = current.next
        self.tail = current
        #print(f"Tail is {self.tail.player.name}")
        return self.tail



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

    """insert an item at the tail of the list"""
    def insert_tail(self, uid, name):
        new_player = Player(uid, name)
        new_node = PlayerNode(new_player)

        current_tail = self.find_tail()
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            current_tail.next = new_node
            new_node.prev = current_tail
            self.tail = new_node

    """delete a node from the head of the list"""
    def delete_head(self):
        if self.is_empty():
            return
        current_head = self.head
        current_head.pre = None
        self.head = current_head.next

    """delete an item from the tail of a list"""
    def delete_tail(self):
        if self.is_empty():
            return
        # when there is ONE item in the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        # when more than one item in the list
        current_tail = self.tail
        current_tail.next = None
        self.tail = current_tail.prev

    """delete an item from the linked list based on its key
        (key = uid)   
    """
    def delete_key(self, key):
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


    """display list from head to tail (forward=True), 
       from tail to head (forward=False)"""
    def display(self, forward=True):
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





