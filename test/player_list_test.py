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

    def setUp(self):
        # when one item in the list
        self.list_one = PlayerList()
        self.list_one.insert_tail("1", "Test1")

        # when multiple items in the list
        self.list_multi = PlayerList()
        self.list_multi.insert_tail("1", "Test1")
        self.list_multi.insert_tail("2", "Test2")
        self.list_multi.insert_tail("3", "Test3")



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
        self.list_one.delete_head()
        self.assertIsNone(self.list_one.head)
        self.assertIsNone(self.list_one.tail)

    def test_delete_head(self):
        """delete an item from the head of the list"""
        self.list_multi.delete_head()
        self.assertEqual(self.list_multi.head.player.uid, "2")
        self.assertIsNone(self.list_multi.head.prev)


    def test_delete_tail(self):
        """delete an item from the tail of a list"""
        self.list_multi.delete_tail()
        self.assertEqual(self.list_multi.tail.player.uid, "2")

    def test_delete_tail_one_item(self):
        self.list_one.delete_tail()
        self.assertIsNone(self.list_one.head)
        self.assertIsNone(self.list_one.tail)


    def test_delete_key_middle(self):
        """delete an item from the linked list based on its key"""
        self.list_multi.delete_key("2")
        self.assertEqual(self.list_multi.head.next.player.uid, "3")
        self.assertEqual(self.list_multi.tail.prev.player.uid, "1")
        self.assertIsNone(self.list_multi.head.prev)
        self.assertIsNone(self.list_multi.tail.next)

    def test_delete_key_head(self):
        self.list_multi.delete_key("1")
        self.assertEqual(self.list_multi.head.player.uid, "2")
        self.assertIsNone(self.list_multi.head.prev)

    def test_delete_key_tail(self):
        self.list_multi.delete_key("3")
        self.assertEqual(self.list_multi.tail.player.uid, "2")
        self.assertIsNone(self.list_multi.tail.next)

    def test_delete_key_not_exist(self):
        self.list_one.delete_key("0")
        self.assertEqual(self.list_one.head.player.uid, "1")
        self.assertEqual(self.list_one.tail.player.uid, "1")


    # display list forward
    def test_display(self):

        with patch('sys.stdout', new=StringIO()) as stdout:
            self.list_multi.display(True)
            self.assertEqual(stdout.getvalue(), "('1', 'Test1'), ('2', 'Test2'), ('3', 'Test3'), ")

        with patch('sys.stdout', new=StringIO()) as stdout:
            self.list_multi.display(False)
            self.assertEqual(stdout.getvalue(), "('3', 'Test3'), ('2', 'Test2'), ('1', 'Test1'), ")














