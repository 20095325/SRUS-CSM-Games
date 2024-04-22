from __future__ import annotations
from player import Player


class PlayerBNode:

    def __init__(self, player: Player | None = None,
                 left: PlayerBNode | None = None,
                 right: PlayerBNode | None = None):

        self._player = player
        self._left = left
        self._right = right

    @property
    def player(self) -> Player | None:
        """
        the player of the current node
        Returns:
            the player object of the current node
        """
        return self._player

    @property
    def left(self) -> PlayerBNode | None:
        """
        the left node getter
        Returns:
            the left PlayerBNode
        """
        return self._left

    @left.setter
    def left(self, node) -> None:
        """
        the left node setter
        Args
            node: the PlayerBNode you want to set as the left node
        """
        self._left = node

    @property
    def right(self) -> PlayerBNode | None:
        """
        the left node getter
        Returns:
            the left PlayerBNode
        """
        return self._right

    @right.setter
    def right(self, node) -> None:
        """
        the left node setter
        Args
            node: the PlayerBNode you want to set as the left node
        """
        self._right = node
