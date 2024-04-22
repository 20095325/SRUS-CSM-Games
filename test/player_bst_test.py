import unittest
from player_bnode import PlayerBNode
from player_bst import PlayerBST
from player import Player


class PlayerBSTTest(unittest.TestCase):

    def test_player_bst_insert_method(self):
        sut = PlayerBST()
        player = Player('123', 'John', 543)
        player2 = Player('5432', 'Marry', 87)
        player3 = Player('543', 'Brian', 421)
        player_bnode = sut.insert(player)
        player2_bnode = sut.insert(player2)
        player3_bnode = sut.insert(player3)
        self.assertEqual(player_bnode.player, player)
        self.assertEqual(player_bnode.right, player2_bnode)
        self.assertEqual(player_bnode.left, player3_bnode)