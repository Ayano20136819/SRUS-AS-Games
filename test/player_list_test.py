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
        tail = test_list1.find_tail()
        self.assertEqual(test_list1.head.player.uid, "3")
        self.assertEqual(tail.player.uid, "1")

    """insert as item at the tail"""
    def test_insert_tail(self):
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        test_list1.insert_tail("2", "Test2")
        test_list1.insert_tail("3", "Test3")
        self.assertEqual(test_list1.tail.player.uid, "3")

    def test_insert_tail_empty(self):
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        self.assertEqual(test_list1.head.player.uid, "1")
        self.assertEqual(test_list1.tail.player.uid, "1")


    """delete an item from the head of the list"""
    def test_delete_head(self):
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        test_list1.insert_tail("2", "Test2")
        test_list1.delete_head()
        self.assertEqual(test_list1.head.player.uid, "2")

    """delete an item from the tail of a list"""
    def test_delete_tail(self):
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        test_list1.insert_tail("2", "Test2")
        test_list1.insert_tail("3", "Test3")
        test_list1.delete_tail()
        self.assertEqual(test_list1.tail.player.uid, "2")

    def test_delete_tail_one_item(self):
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        test_list1.delete_tail()
        self.assertIsNone(test_list1.head)
        self.assertIsNone(test_list1.tail)

    """delete an item from the linked list based on its key"""
    def test_delete_key(self):
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        test_list1.insert_tail("2", "Test2")
        test_list1.insert_tail("3", "Test3")
        test_list1.delete_key("2")
        # test_list1.display()
        self.assertEqual(test_list1.head.next.player.uid, "3")

    def test_delete_key_head(self):
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        test_list1.insert_tail("2", "Test2")
        test_list1.insert_tail("3", "Test3")
        test_list1.delete_key("1")
        self.assertEqual(test_list1.head.player.uid, "2")

    def test_delete_key_tail(self):
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        test_list1.insert_tail("2", "Test2")
        test_list1.insert_tail("3", "Test3")
        test_list1.delete_key("3")
        self.assertEqual(test_list1.tail.player.uid, "2")

    # display list forward
    def test_display_forward(self):
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        test_list1.insert_tail("2", "Test2")
        test_list1.insert_tail("3", "Test3")
        test_list1.display(True)
        self.assertEqual(test_list1.head.player.uid, "1")








