from __future__ import annotations
from player_bnode import PlayerBNode
from player import Player


class PlayerBST:

    def __init__(self, root: PlayerBNode | None = None):
        self._root = root

    def insert(self, player: Player, node: PlayerBNode | None = None) -> PlayerBNode:
        if self.root is None:
            self._root = PlayerBNode(player)
            return self.root

        current_node = node or self.root
        if player.name < current_node.player.name:
            if current_node.left is None:
                current_node.left = PlayerBNode(player)
                return current_node.left
            self.insert(player, current_node.left)
        elif player.name > current_node.player.name:
            if current_node.right is None:
                current_node.right = PlayerBNode(player)
                return current_node.right
            self.insert(player, current_node.right)
        else:
            current_node.player = player

        return current_node

    @property
    def root(self) -> PlayerBNode | None:
        """
        the root node getter
        Returns:
            the root node of the player BST
        """
        return self._root
