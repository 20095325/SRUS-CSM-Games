from __future__ import annotations
from player import Player


class PlayerNode:
    """
    The player node class used to store a player
    along with that players next and prev nodes
    """
    def __init__(self, player: Player = None, next_node: PlayerNode = None, prev_node: PlayerNode = None) -> None:
        """
        Initialise a player node
        Args:
            player: This is the player object
            next_node: This is the reference to the next player object
            prev_node: This is the reference to the prev player object
        """
        self._player: Player = player
        self._next_node: PlayerNode | None = next_node
        self._prev_node: PlayerNode | None = prev_node

    def __str__(self) -> str:
        """
        The string dunder method
        Returns:
            A formatted string of the current player | next player | prev player
        """
        next_node = self.next.player if self.next else None
        prev_node = self.prev.player if self.prev else None
        return f'PlayerNode: {self.player} | {next_node} | {prev_node}'

    @property
    def next(self) -> PlayerNode | None:
        """
        The next node getter
        Returns:
             the node of the next player
        """
        return self._next_node

    @next.setter
    def next(self, node) -> None:
        """
        The next node setter
        Args:
            node: the node of the next player
        """
        self._next_node = node

    @property
    def prev(self) -> PlayerNode | None:
        """
        the prev node getter
        Returns:
            the node of the prev player
        """
        return self._prev_node

    @prev.setter
    def prev(self, node) -> None:
        """
        the prev node setter
        Args
            node: the node of the prev player
        """
        self._prev_node = node

    @property
    def key(self) -> str:
        """
        the key getter
        Returns:
            the uid of the player of the current node
        """
        return self._player.uid

    @property
    def player(self):
        """
        the player getter
        Returns:
            the player of the current node
        """
        return self._player
