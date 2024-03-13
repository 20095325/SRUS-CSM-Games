from __future__ import annotations

from player_list import PlayerList, LinkedListException
from player import Player


class PlayerHashTable:
    """
    The hash table class for the player lists
    """
    SIZE = 10
    hash_map: list[PlayerList]

    def __init__(self):
        """
        initialise the player hash table
        """
        self.hash_map = [PlayerList() for _ in range(self.SIZE)]

    def get_index(self, key: str | Player) -> int:
        """
        used to find the index of the player list a player belongs to
        Args:
            key: the key/uid of a player
        Returns:
             an int representing an index of the table
        """
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.make_hash(key) % self.SIZE

    def __getitem__(self, key: str) -> Player:
        """
        the get item dunder method
        used to find the index of the player list using the hash of the player id
        we used that index to get the correct player list and search through that player list.
        Args:
            key: the key/uid of a player
        Returns:
             a Player with the given key/uid
        """
        index = self.get_index(key)
        player_list = self.hash_map[index]
        try:
            player_node = player_list.search(key)
            return player_node.player
        except LinkedListException as e:
            raise KeyError(str(e))

    def __setitem__(self, key, name):
        """
        the set item dunder method
        used to find the index of the player list using the hash of the player id
        this determines which player list in the table to store the player in
        Args:
            key: the key/uid of a player
            name: the name of the player
        """
        player = Player(key, name)
        index = self.get_index(player)
        player_list = self.hash_map[index]
        try:
            node = player_list.search(key)
            node.player = player
        except LinkedListException:
            player_list.append(player)

    def __len__(self):
        """
        the len dunder method
        Returns:
            an int representing the number of players in the hash table
        """
        length: int = 0
        for x in self.hash_map:
            length += PlayerList.count(x)
        return length

    def __delitem__(self, key):
        """
        the delete item dunder method
        used the find the index of the player list and the remove the player from that list
        Args:
            key: the key/uid of a player
        """
        index = self.get_index(key)
        player_list = self.hash_map[index]
        try:
            player_list.remove(key)
        except LinkedListException as e:
            raise KeyError(str(e))
