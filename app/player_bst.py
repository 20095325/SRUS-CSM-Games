from __future__ import annotations
from player_bnode import PlayerBNode
from player import Player


class PlayerBST:
    """
    PlayerBST class used to create a Binary Search Tree for Players
    """
    def __init__(self, root: PlayerBNode | None = None):
        """
        Initialise the PlayerBST
        Args:
            root: The player binary node.
        """
        self._root = root

    def insert(self, player: Player) -> PlayerBNode:
        """
        the binary insert method for our PlayerBST
        Args:
            player: The Player object that you want to insert
        Returns:
            the node of the inserted player
        """
        if self.root is None:
            self._root = PlayerBNode(player)
            return self.root

        current_node = self.root
        if player.name < current_node.player.name:
            if current_node.left is None:
                current_node.left = PlayerBST(PlayerBNode(player))
                return current_node.left.root
            return current_node.left.insert(player)
        elif player.name > current_node.player.name:
            if current_node.right is None:
                current_node.right = PlayerBST(PlayerBNode(player))
                return current_node.right.root
            return current_node.right.insert(player)
        else:
            current_node._player = player
            return current_node

    def search(self, name: str) -> PlayerBNode:
        """
        the binary search method for our PlayerBST
        Args:
            name: The name of the player that you want to find
        Returns:
            the node of the found player or None
        """
        if self.root is None:
            return self.root

        current_node = self.root
        if name < current_node.player.name:
            if current_node.left is None:
                return current_node.left
            return current_node.left.search(name)
        elif name > current_node.player.name:
            if current_node.right is None:
                return current_node.right
            return current_node.right.search(name)
        else:
            return current_node

    def sorted_list(self) -> list:
        """
        Get a sorted list from our BST
        Returns:
            A list of PlayerBNodes in alphabetical order
        """
        player_list = []
        if self.root.left:
            player_list += self.root.left.sorted_list()
        player_list.append(self.root)
        if self.root.right:
            player_list += self.root.right.sorted_list()
        return player_list

    @staticmethod
    def balanced_bst(sorted_list) -> PlayerBST | None:
        """
        Create a new BST from a sorted list
        Returns:
            A list of PlayerBNodes in alphabetical order
        """
        if not sorted_list:
            return None

        middle = len(sorted_list) // 2
        bst = PlayerBST(sorted_list[middle])
        bst.root.left = PlayerBST.balanced_bst(sorted_list[:middle])
        bst.root.right = PlayerBST.balanced_bst(sorted_list[middle + 1:])

        return bst

    @property
    def root(self) -> PlayerBNode | None:
        """
        the root node getter
        Returns:
            the root node of the player BST
        """
        return self._root
