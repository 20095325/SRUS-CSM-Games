import unittest
from player_list import PlayerList
from player import Player


class PlayerListTest(unittest.TestCase):

    def test_player_list(self):
        sut = PlayerList([Player('123', 'John')])
        self.assertIsNotNone(sut._head)

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

    def test_player_list_insert_empty(self):
        sut = PlayerList()
        sut.insert(Player('456', 'Marry'))
        self.assertEqual(str(sut.head), 'PlayerNode: Player: 456, Marry | None | None')

