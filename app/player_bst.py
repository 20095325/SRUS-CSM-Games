from __future__ import annotations
from player_bnode import PlayerBNode


class PlayerBST:

    def __init__(self, root: PlayerBNode | None = None):
        self._root = root

    @property
    def root(self) -> PlayerBNode | None:
        """
        the root node getter
        Returns:
            the root node of the player BST
        """
        return self._root
