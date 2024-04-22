from __future__ import annotations
from player import Player


class PlayerBNode:
    """
    PlayerBNode class used to create a Node for our PlayerBST
    """
    def __init__(self, player: Player | None = None):
        """
        Initialise the PlayerBNode
        Args:
            player: The Player Object that belongs to this node.
        """
        self._player = player
        self._left = None
        self._right = None

    @property
    def player(self) -> Player | None:
        """
        the player of the current node
        Returns:
            the player object of the current node
        """
        return self._player

    @property
    def left(self):
        """
        the left node getter
        Returns:
            the left PlayerBST
        """
        return self._left

    @left.setter
    def left(self, node) -> None:
        """
        the left node setter
        Args
            node: the PlayerBST you want to set as the left node
        """
        self._left = node

    @property
    def right(self):
        """
        the right node getter
        Returns:
            the right PlayerBST
        """
        return self._right

    @right.setter
    def right(self, node) -> None:
        """
        the right node setter
        Args
            node: the PlayerBST you want to set as the right node
        """
        self._right = node
