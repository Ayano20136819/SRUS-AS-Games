# -------------------------------
#
# Folder: test
# Filename: player_list_test
# Author: Ayano SASAKIDO
# Version 0.0
# Created: 08/08/2025
#
# -------------------------------
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from app.player_list import PlayerList

class TestPlayerList(TestCase):


    def test_insert_empty_list(self):
        """when the list is empty"""
        test_list1 = PlayerList()
        test_list1.insert("1", "Test1")
        self.assertEqual(test_list1.head.player.uid, "1")
        self.assertIsNone(test_list1.head.prev)
        self.assertIsNone(test_list1.head.next)


    def test_insert_list(self):
        """when the list is not empty"""
        test_list1 = PlayerList()
        test_list1.insert("1", "Test1")
        test_list1.insert("2", "Test2")
        test_list1.insert("3", "Test3")
        self.assertEqual(test_list1.head.player.uid, "3")
        self.assertEqual(test_list1.tail.player.uid, "1")
        self.assertEqual(test_list1.head.next.player.uid, "2")
        self.assertEqual(test_list1.tail.prev.player.uid, "2")


    def test_insert_tail(self):
        """insert as item at the tail"""
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


    def test_delete_head_one_item(self):
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        test_list1.delete_head()
        self.assertIsNone(test_list1.head)
        self.assertIsNone(test_list1.tail)

    def test_delete_head(self):
        """delete an item from the head of the list"""
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        test_list1.insert_tail("2", "Test2")
        test_list1.delete_head()
        self.assertEqual(test_list1.head.player.uid, "2")
        self.assertIsNone(test_list1.head.prev)


    def test_delete_tail(self):
        """delete an item from the tail of a list"""
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


    def test_delete_key_middle(self):
        """delete an item from the linked list based on its key"""
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        test_list1.insert_tail("2", "Test2")
        test_list1.insert_tail("3", "Test3")
        test_list1.delete_key("2")
        self.assertEqual(test_list1.head.next.player.uid, "3")
        self.assertEqual(test_list1.tail.prev.player.uid, "1")
        self.assertIsNone(test_list1.head.prev)
        self.assertIsNone(test_list1.tail.next)

    def test_delete_key_head(self):
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        test_list1.insert_tail("2", "Test2")
        test_list1.insert_tail("3", "Test3")
        test_list1.delete_key("1")
        self.assertEqual(test_list1.head.player.uid, "2")
        self.assertIsNone(test_list1.head.prev)

    def test_delete_key_tail(self):
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        test_list1.insert_tail("2", "Test2")
        test_list1.insert_tail("3", "Test3")
        test_list1.delete_key("3")
        self.assertEqual(test_list1.tail.player.uid, "2")
        self.assertIsNone(test_list1.tail.next)

    def test_delete_key_not_exist(self):
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        test_list1.delete_key("0")
        self.assertEqual(test_list1.head.player.uid, "1")
        self.assertEqual(test_list1.tail.player.uid, "1")


    # display list forward
    def test_display(self):
        test_list1 = PlayerList()
        test_list1.insert_tail("1", "Test1")
        test_list1.insert_tail("2", "Test2")
        test_list1.insert_tail("3", "Test3")

        with patch('sys.stdout', new=StringIO()) as stdout:
            test_list1.display(True)
            self.assertEqual(stdout.getvalue(), "('1', 'Test1'), ('2', 'Test2'), ('3', 'Test3'), ")

        with patch('sys.stdout', new=StringIO()) as stdout:
            test_list1.display(False)
            self.assertEqual(stdout.getvalue(), "('3', 'Test3'), ('2', 'Test2'), ('1', 'Test1'), ")














