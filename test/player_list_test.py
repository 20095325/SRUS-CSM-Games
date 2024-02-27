import unittest
from player_list import PlayerList, LinkedListException
from player import Player


class PlayerListTest(unittest.TestCase):

    def test_player_list(self):
        sut = PlayerList([Player('123', 'John')])
        self.assertIsNotNone(sut._head)
        self.assertIsNotNone(sut._tail)

    def test_player_list_is_empty(self):
        sut = PlayerList()
        self.assertTrue(sut.is_empty())

    def test_player_list_is_not_empty(self):
        sut = PlayerList([Player('123', 'John')])
        self.assertFalse(sut.is_empty())

    def test_player_list_insert_not_empty(self):
        sut = PlayerList([Player('123', 'John')])
        sut.insert(Player('456', 'Marry'))
        self.assertEqual(str(sut.head), 'PlayerNode: Player: 456, Marry | Player: 123, John | None')
        self.assertEqual(str(sut.tail), 'PlayerNode: Player: 123, John | None | Player: 456, Marry')

    def test_player_list_insert_empty(self):
        sut = PlayerList()
        sut.insert(Player('456', 'Marry'))
        self.assertEqual(str(sut.head), 'PlayerNode: Player: 456, Marry | None | None')
        self.assertEqual(str(sut.tail), 'PlayerNode: Player: 456, Marry | None | None')

    def test_player_list_append_not_empty(self):
        sut = PlayerList([Player('123', 'John')])
        sut.append(Player('456', 'Marry'))
        self.assertEqual(str(sut.head), 'PlayerNode: Player: 123, John | Player: 456, Marry | None')
        self.assertEqual(str(sut.tail), 'PlayerNode: Player: 456, Marry | None | Player: 123, John')

    def test_player_list_append_empty(self):
        sut = PlayerList()
        sut.append(Player('456', 'Marry'))
        self.assertEqual(str(sut.head), 'PlayerNode: Player: 456, Marry | None | None')
        self.assertEqual(str(sut.tail), 'PlayerNode: Player: 456, Marry | None | None')

    def test_player_list_delete(self):
        sut = PlayerList([Player('123', 'John'), Player('456', 'Marry')])
        sut.delete()
        self.assertEqual(str(sut.head), 'PlayerNode: Player: 456, Marry | None | None')
        self.assertEqual(str(sut.tail), 'PlayerNode: Player: 456, Marry | None | None')

    def test_player_list_pop(self):
        sut = PlayerList([Player('123', 'John'), Player('456', 'Marry')])
        sut.pop()
        self.assertEqual(str(sut.head), 'PlayerNode: Player: 123, John | None | None')
        self.assertEqual(str(sut.tail), 'PlayerNode: Player: 123, John | None | None')

    def test_player_list_delete_empty(self):
        sut = PlayerList()
        with self.assertRaises(LinkedListException) as err:
            sut.delete()
            self.assertEqual(type(err.exception), LinkedListException)
            self.assertEqual(err.exception.args[0], "The list is empty.")

    def test_player_list_pop_empty(self):
        sut = PlayerList()
        with self.assertRaises(LinkedListException) as err:
            sut.pop()
            self.assertEqual(type(err.exception), LinkedListException)
            self.assertEqual(err.exception.args[0], "The list is empty.")

    def test_player_list_remove(self):
        sut = PlayerList([Player('123', 'John'),
                          Player('873', 'Karen'),
                          Player('456', 'Marry')])
        removed = sut.remove('873')
        self.assertEqual(str(removed), 'PlayerNode: Player: 873, Karen | Player: 456, Marry | Player: 123, John')
        self.assertEqual(str(sut.head), 'PlayerNode: Player: 123, John | Player: 456, Marry | None')
        self.assertEqual(str(sut.tail), 'PlayerNode: Player: 456, Marry | None | Player: 123, John')

    def test_player_list_remove_invalid_key(self):
        sut = PlayerList([Player('123', 'John'),
                          Player('873', 'Karen'),
                          Player('456', 'Marry')])
        with self.assertRaises(LinkedListException) as err:
            sut.remove('543')
            self.assertEqual(type(err.exception), LinkedListException)
            self.assertEqual(err.exception.args[0], "Key does not exist.")

    def test_player_list_remove_empty(self):
        sut = PlayerList()
        with self.assertRaises(LinkedListException) as err:
            sut.remove('873')
            self.assertEqual(type(err.exception), LinkedListException)
            self.assertEqual(err.exception.args[0], "The list is empty.")

    def test_player_list_display(self):
        sut = PlayerList([Player('123', 'John'),
                          Player('873', 'Karen'),
                          Player('456', 'Marry')])
        sut.display()
        print("\n")
        sut.display(False)
