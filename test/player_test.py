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

    def test_player_comparison_operator_dunder_methods(self):
        player = Player('7656', 'John', 25)
        other_player = Player('5432', 'Marry', 20)
        other_player2 = Player('6543', 'Karen', 25)
        self.assertEqual(player, other_player2)  # 25 = 25
        self.assertGreater(player, other_player)  # 25 > 20
        self.assertGreaterEqual(player, other_player)  # 25 >= 20
        self.assertGreaterEqual(player, other_player2)  # 25 >= 25
        self.assertLess(other_player, player)  # 20 < 25
        self.assertLessEqual(other_player, player)  # 20 <= 25
        self.assertLessEqual(other_player2, player)  # 25 <= 25

    def test_player_quick_sort_method(self):
        sut = [Player('7656', 'John', 13),
               Player('5432', 'Marry', 87),
               Player('6543', 'Karen', 43),
               Player('534', 'Josh', 654),
               Player('432', 'Brandon', 72),
               Player('765', 'Luna', 3)]

        expectedReturn = [Player('534', 'Josh', 654),
                          Player('5432', 'Marry', 87),
                          Player('432', 'Brandon', 72),
                          Player('6543', 'Karen', 43),
                          Player('7656', 'John', 13),
                          Player('765', 'Luna', 3)]

        self.assertEqual(Player.quicksort(sut), expectedReturn)
