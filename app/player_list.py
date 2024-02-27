from __future__ import annotations
from player_node import PlayerNode
from player import Player


class PlayerList:
    def __init__(self, values: list[Player] = None, head: PlayerNode = None, tail: PlayerNode = None) -> None:
        self._head: PlayerNode | None = head
        self._tail: PlayerNode | None = tail
        if values:
            for value in values:
                self.append(value)

    def is_empty(self) -> bool:
        return self._head is None

    def insert(self, value: Player):
        if self.is_empty():
            self.empty_insert(value)
        else:
            current_node = PlayerNode(value, self._head)
            self._head.prev = current_node
            self._head = current_node

    def append(self, value: Player):
        if self.is_empty():
            self.empty_insert(value)
        else:
            current_node = PlayerNode(value, None, self._tail)
            self._tail.next = current_node
            self._tail = current_node

    def empty_insert(self, value: Player):
        self._head = PlayerNode(value)
        self._tail = self._head

    def delete(self):
        if self.is_empty():
            raise LinkedListException("The list is empty.")
        removed_node = self._head.player
        self._head = self._head.next
        self._head.prev = None
        return removed_node

    def pop(self):
        if self.is_empty():
            raise LinkedListException("The list is empty.")
        removed_node = self._tail.player
        self._tail = self._tail.prev
        self._tail.next = None
        return removed_node

    def remove(self, key):
        if self.is_empty():
            raise LinkedListException("The list is empty.")
        current_node = self._head
        while current_node:
            if current_node.key == key:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self._head = self._head.next
                    self._head.prev = None
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                else:
                    self._tail = self._tail.prev
                    self._tail.next = None
                return current_node
            current_node = current_node.next
        raise LinkedListException("Key does not exist.")

    def display(self, forward: bool = True):
        if forward:
            current_node = self._head
            while current_node:
                print(current_node.player)
                current_node = current_node.next
        else:
            current_node = self._tail
            while current_node:
                print(current_node.player)
                current_node = current_node.prev

    @property
    def head(self) -> PlayerNode | None:
        return self._head

    @property
    def tail(self) -> PlayerNode | None:
        return self._tail


class LinkedListException(Exception):
    def __init__(self, message):
        self.message = message
