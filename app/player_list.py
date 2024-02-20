from __future__ import annotations
from player_node import PlayerNode
from player import Player


class PlayerList:
    def __init__(self, values: list[Player] = None, head: PlayerNode = None, tail: PlayerNode = None) -> None:
        self._head: PlayerNode | None = head
        self._tail: PlayerNode | None = tail
        if values:
            for value in values:
                self.insert(value)

    def is_empty(self) -> bool:
        return self._head is None

    def insert(self, value):
        if self.is_empty():
            self._head = PlayerNode(value)
            self._tail = self._head
        else:
            new_node = PlayerNode(value, self._head)
            self._head.prev = new_node
            self._head = new_node

    @property
    def head(self) -> PlayerNode | None:
        return self._head

    @property
    def tail(self) -> PlayerNode | None:
        return self._tail



