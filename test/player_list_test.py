# -------------------------------
#
# Folder: test
# Filename: player_list_test
# Author: Ayano SASAKIDO
# Version 0.0
# Created: 08/08/2025
#
# -------------------------------

from unittest import TestCase
from app.player_list import PlayerList

class TestPlayerList(TestCase):

    """when the list is empty"""
    def test_insert_empty_list(self):
        test_list1 = PlayerList()
        test_list1.insert("1", "Test1")
        self.assertEqual(test_list1.head.player.uid, "1")

    """when the list is not empty"""
    def test_insert_list(self):
        test_list1 = PlayerList()
        test_list1.insert("1", "Test1")
        test_list1.insert("2", "Test2")
        test_list1.insert("3", "Test3")
        self.assertEqual(test_list1.head.player.uid, "3")





