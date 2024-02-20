from __future__ import annotations
from player import Player


class PlayerNode:
    def __init__(self, player: Player = None, next_node: PlayerNode = None, prev_node: PlayerNode = None) -> None:
        self._player: Player = player
        self._next_node: PlayerNode | None = next_node
        self._prev_node: PlayerNode | None = prev_node

    def __str__(self) -> str:
        next_node = self.next.player if self.next else None
        prev_node = self.prev.player if self.prev else None
        return f'PlayerNode: {self.player} | {next_node} | {prev_node}'

    @property
    def next(self) -> PlayerNode | None:
        return self._next_node

    @next.setter
    def next(self, node) -> None:
        self._next_node = node

    @property
    def prev(self) -> PlayerNode | None:
        return self._prev_node

    @prev.setter
    def prev(self, node) -> None:
        self._prev_node = node

    @property
    def key(self) -> str:
        return self._player.uid

    @property
    def player(self):
        return self._player
