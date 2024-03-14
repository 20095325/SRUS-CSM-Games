import unittest
from player_list import PlayerList, LinkedListException
from player import Player
from player_hash_table import PlayerHashTable


class HashMapTest(unittest.TestCase):

    def test_hash_map_init(self):
        sut = PlayerHashTable()
        self.assertIsInstance(sut, PlayerHashTable)

    def test_hash_map_get_index(self):
        player = Player('7656', 'John')
        sut = PlayerHashTable()
        self.assertEqual(sut.get_index(player), sut.get_index(player.uid))

    def test_hash_map_set_item_get_item(self):
        sut = PlayerHashTable()
        sut['123'] = 'John'
        self.assertEqual(str(sut['123']), 'Player: 123, John')

    def test_hash_map_len(self):
        sut = PlayerHashTable()
        self.assertEqual(len(sut), 0)
        sut['123'] = 'John'
        self.assertEqual(len(sut), 1)

    def test_hash_map_delete_item(self):
        sut = PlayerHashTable()
        sut['123'] = 'John'
        sut['543'] = 'Marry'
        self.assertEqual(len(sut), 2)
        del sut['123']
        self.assertEqual(len(sut), 1)
        del sut['543']
        self.assertEqual(len(sut), 0)

    def test_hash_map_display(self):
        sut = PlayerHashTable()
        sut['123'] = 'John'
        sut['543'] = 'Marry'
        sut['765'] = 'Karen'  # this collides with Marry
        sut.display()

