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
        player = Player(11, "Test", 9)
        self.assertEqual(player.score, 9)