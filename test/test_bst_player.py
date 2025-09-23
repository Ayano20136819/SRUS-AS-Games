from app.player_bst import PlayerBST
from app.player_bnode import PlayerBNode
from app.player import Player
from unittest import TestCase
import random

class TestPlayerList(TestCase):

    def setUp(self):
        # player1 = Player("2", "John")
        # player2 = Player("1", "Ayano")
        # player3 = Player("3", "Test")
        # bst = PlayerBST()
        pass

    def test_insert_empty_tree(self):
        player1 = Player("2", "John")
        bst = PlayerBST()
        bst.insert(player1)
        print(bst)
        #self.assertEqual(PlayerBNode.player)