# -------------------------------
#
# Folder: test
# Filename: player_test.py
# Author: Ayano SASAKIDO
# Version 0.0
# Created: 
#
# -------------------------------

from app.player import Player
from unittest import TestCase


class TestPlayer(TestCase):

    def test_player_uid(self):
        player = Player("08", "Ayano")
        self.assertEqual(player.uid, "08")

    def test_player_name(self):
        player = Player("13", "John")
        self.assertEqual(player.name, "John")

    def test_player_score(self):
        player = Player('11', "Test", 9)
        self.assertEqual(player.score, 9)

    def test_sort_players(self):
        players = [Player('01', "Alice", 10), Player('02', "Bob", 5), Player('03',"Charlie", 15)]

        # do **not** change the following code:
        sorted_players = sorted(players)
        #print(sorted_players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player('02',"Bob",  5), Player('01',"Alice", 10), Player('03',"Charlie", 15)]
        #print(manually_sorted_players)

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player('01', "Alice",  score=10)
        bob = Player('02', "Bob", score=5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(alice, bob)
        # or, event better
        self.assertGreater(alice, bob)

    def test_sort_descending_score(self):
        players = [Player('01', "Alice", 10), Player('02', "Bob", 5), Player('03', "Charlie", 15)]
        #print(Player.sort_quickly(players))
        expect_order = [Player(name="Charlie", uid="03", score=15), Player(name="Alice", uid='01', score=10), Player(name="Bob", uid='02', score=5)]
        self.assertEqual(Player.sort_quickly(players), expect_order)