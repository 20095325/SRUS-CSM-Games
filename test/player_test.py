import unittest
from player import Player


class PlayerTest(unittest.TestCase):

    def test_player_str(self):
        sut = Player('123', 'John')
        self.assertEqual(str(sut), 'Player: 123, John')

    def test_player_name_and_uid(self):
        sut = Player('123', 'John')
        self.assertEqual(sut.uid, '123')
        self.assertEqual(sut.name, 'John')

    def test_player_hash(self):
        player = Player('7656', 'John')
        self.assertEqual(hash(player), Player.make_hash('7656'))
