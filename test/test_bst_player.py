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
        self.assertEqual(str(bst),
                         "PlayerBST(PlayerBNode(PlayerName=Player(name=John, uid=2, "
                               "score=0), left=None, right=None)")

    def test_insert_two_people(self):
        player1 = Player("2", "1Test")
        player2 = Player("3", "2Test")
        bst = PlayerBST()
        bst.insert(player1)
        bst.insert(player2)
        print(bst)
        self.assertEqual(str(bst),
                         "PlayerBST(PlayerBNode(PlayerName=Player(name=1Test, uid=2, "
                         "score=0), left=None, right=PlayerBNode(PlayerName=Player("
                         "name=2Test, uid=3, score=0), left=None, right=None)")

    def test_search_node(self):
        player1 = Player("2", "1Test")
        player2 = Player("3", "2Test")
        bst = PlayerBST()
        bst.insert(player1)
        bst.insert(player2)
        result = bst.search("1Test")
        self.assertEqual(result, "1Test")

    def test_search_unexisting_node(self):
        player1 = Player("2", "1Test")
        player2 = Player("3", "2Test")
        bst = PlayerBST()
        bst.insert(player1)
        bst.insert(player2)
        result = bst.search("Dummy")
        self.assertEqual(str(result), "None")
