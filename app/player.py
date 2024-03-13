from __future__ import annotations

import hashlib


class Player:
    """
    player class used to create a player
    """
    def __init__(self, unique_id: str = None, player_name: str = None) -> None:
        """
        Initialise a player
        Args:
            unique_id: Used to identify the player.
            player_name: The name of the player.
        """
        self._uid: str | None = unique_id
        self._name: str | None = player_name

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
        return self.uid == other.uid

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
