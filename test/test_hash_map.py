# -------------------------------
#
# Folder: test
# Filename: test_hash_map
# Author: Ayano SASAKIDO
# Version 0.0
# Created: 08/26
#
# -------------------------------

from unittest import TestCase
from app.player_hashmap import PlayerHashMap
from app.player import Player
from app.player_list import PlayerList

class TestPlayerHashMap(TestCase):
    def setUp(self):
        self.player_hash_map = PlayerHashMap()
        self.my_player1 = Player("1", "Alice")
        self.my_player2 = Player("2", "Bob")
        self.my_player3 = Player("11", "Charlie")

    def test_get_player_list(self):
        """ Player1 ID:1, Name:Alice """
        self.player_hash_map[self.my_player1] = self.my_player1.name
        self.assertEqual(self.player_hash_map[self.my_player1], "Alice")

    def test_add_new_player(self):
        """ Add a new player to the hash map """
        self.player_hash_map[self.my_player1] = self.my_player1.name
        self.player_hash_map[self.my_player2] = self.my_player2.name
        self.assertEqual(self.player_hash_map[self.my_player1], "Alice")
        self.assertEqual(self.player_hash_map[self.my_player2], "Bob")


    def test_update_player_name(self):
        """ Update player name when the player in the list"""
        self.player_hash_map[self.my_player1] = self.my_player1.name
        self.player_hash_map[self.my_player3] = self.my_player3.name
        self.assertEqual(self.player_hash_map[self.my_player1], "Charlie")

    def test_remove_player(self):
        """ Remove a player from the hash map """
        self.player_hash_map[self.my_player1] = self.my_player1.name
        self.player_hash_map[self.my_player2] = self.my_player2.name
        self.player_hash_map.__delitem__(self.my_player1)
        count = len(self.player_hash_map)
        print(f"Count: {len(self.player_hash_map)}")
        self.assertEqual(count, 1)

    def test_count_players(self):
        """ Count the number of players in the hash map """
        # add one player
        self.player_hash_map[self.my_player1] = self.my_player1.name
        self.assertEqual(len(self.player_hash_map), 1)

        # add second player
        self.player_hash_map[self.my_player2] = self.my_player2.name
        self.assertEqual(len(self.player_hash_map), 2)





