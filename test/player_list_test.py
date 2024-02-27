import unittest
from player_list import PlayerList
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
