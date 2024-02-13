import unittest
import player


class PlayerTest(unittest.TestCase):

    def test_player_str(self):
        sut = player.Player('123', 'John')
        self.assertEqual(str(sut), 'Player: 123, John')

    def test_player_name_and_uid(self):
        sut = player.Player('123', 'John')
        self.assertEqual(sut._uid, '123')
        self.assertEqual(sut._name, 'John')
