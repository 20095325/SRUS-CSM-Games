from __future__ import annotations

import hashlib


class Player:
    """
    player class used to create a player
    """
    def __init__(self, unique_id: str = None, player_name: str = None, score: int = None) -> None:
        """
        Initialise a player
        Args:
            unique_id: Used to identify the player.
            player_name: The name of the player.
            score: The score of the player.
        """
        self._uid = unique_id
        self._name = player_name
        self._score = score

    def __str__(self) -> str:
        """
        The string dunder method
        Returns:
            A formatted string that is human-readable
        """
        return f'Player: {self._uid}, {self._name}'

    def __eq__(self, other) -> bool:
        """
        The equals dunder method
        Args:
            other: this is the other player that this player being compared to
        Returns:
            A boolean
        """
        return self.score == other.score

    def __ge__(self, other) -> bool:
        """
        The greater than or equals dunder method
        Args:
            other: this is the other player that this player being compared to
        Returns:
            A boolean
        """
        return self.score >= other.score

    def __gt__(self, other) -> bool:
        """
        The greater than dunder method
        Args:
            other: this is the other player that this player being compared to
        Returns:
            A boolean
        """
        return self.score > other.score

    def __le__(self, other) -> bool:
        """
        The less than or equals dunder method
        Args:
            other: this is the other player that this player being compared to
        Returns:
            A boolean
        """
        return self.score <= other.score

    def __lt__(self, other) -> bool:
        """
        The less than dunder method
        Args:
            other: this is the other player that this player being compared to
        Returns:
            A boolean
        """
        return self.score < other.score

    @staticmethod
    def quicksort(player_list: list) -> list:
        """
        The quick sort static method used to sort a list of players by the player score.
        Args:
            player_list: the list of player objects
        Returns:
            the list of players sorted by the player score
        """
        if len(player_list) <= 1:
            return player_list
        pivot = player_list[0]
        left = [i for i in player_list[1:] if i > pivot]
        right = [i for i in player_list[1:] if i <= pivot]
        return Player.quicksort(left) + [pivot] + Player.quicksort(right)


    @property
    def uid(self) -> str:
        """
        the player uid getter
        Returns:
            the uid of the current player
        """
        return self._uid

    @property
    def name(self) -> str:
        """
        the player name getter
        Returns:
             the name of the current player
        """
        return self._name

    @property
    def score(self) -> int | None:
        """
        the player score getter
        Returns:
             the score of the current player
        """
        return self._score

    def __hash__(self) -> int:
        """
        The hash dunder method
        Returns:
            an int of hash created by the make_hash function
        """
        return self.make_hash(self.uid)

    @classmethod
    def make_hash(cls, key):
        """
        the hash function which creates the hash
        Args:
            key: the key is normally the uid of the player
        Returns:
            an int of hash created by the make_hash function
        """
        return int(hashlib.sha256(key.encode()).hexdigest(), 16) & (2**16 - 1)
        # the last bit above keeps our hash under 32bit so that the __hash__ method does not truncate our hash.
