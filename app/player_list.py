from __future__ import annotations
from player_node import PlayerNode
from player import Player


class PlayerList:
    """
    The player list class used to store the head and tail of the list
    """
    def __init__(self, values: list[Player] = None, head: PlayerNode = None, tail: PlayerNode = None) -> None:
        """
        Initialise a player list
        Args:
            values: this will be the initial list of players to start with
            head: this is the start node of the player list
            tail: this is the end node of the player list
        """
        self._head: PlayerNode | None = head
        self._tail: PlayerNode | None = tail
        if values:
            for value in values:
                self.append(value)

    def __len__(self):
        """
        used to count the amount of players in the list
        Returns:
             an int representing the amount of players
        """
        length = 0
        if self.is_empty():
            return length
        current_node = self._head
        while current_node:
            current_node = current_node.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        used to check if the list has no nodes in it
        Returns:
            a boolean
        """
        return self._head is None

    def insert(self, value: Player):
        """
        Used to insert a player at the start of the list
        Args:
            value: a player
        """
        if self.is_empty():
            self.empty_insert(value)  # if empty use helper function to insert a new head and tail into the list
        else:
            current_node = PlayerNode(value, self._head)
            self._head.prev = current_node
            self._head = current_node

    def append(self, value: Player):
        """
        Used to insert a player at the end of the list
        Args:
            value: a player
        """
        if self.is_empty():
            self.empty_insert(value)  # if empty use helper function to insert a new head and tail into the list
        else:
            current_node = PlayerNode(value, None, self._tail)
            self._tail.next = current_node
            self._tail = current_node

    def empty_insert(self, value: Player):
        """
        helper function for inserting a player into an empty list
        Args:
            value: a player
        """
        self._head = PlayerNode(value)
        self._tail = self._head

    def delete(self):
        """
        Used to delete a player at the start of the list also known as the head
        Returns:
            the deleted node
        """
        if self.is_empty():
            raise LinkedListException("The list is empty.")
        removed_node = self._head.player
        self._head = self._head.next
        self._head.prev = None
        return removed_node

    def pop(self):
        """
        Used to delete a player at the end of the list also known as the tail
        Returns:
            the deleted node
        """
        if self.is_empty():
            raise LinkedListException("The list is empty.")
        removed_node = self._tail.player
        self._tail = self._tail.prev
        self._tail.next = None
        return removed_node

    def remove(self, key):
        """
        used to remove a node anywhere in the list using the key/player uid
        Args:
            key: the player uid
        Returns:
             the removed node
        Raises:
            LinkedListException: raises and exception
        """
        if self.is_empty():
            raise LinkedListException("The list is empty.")
        current_node = self._head
        while current_node:
            if current_node.key == key:
                if len(self) == 1:
                    self._head = None
                    self._tail = None
                    return current_node
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

    def search(self, key):
        """
        used to search through the list using the key/player uid
        Args:
            key: the player uid
        Returns:
             a player node if the key exists
        Raises:
            LinkedListException: raises and exception
        """
        if self.is_empty():
            raise LinkedListException("The list is empty.")
        current_node = self._head
        while current_node:
            if current_node.key == key:
                return current_node
            current_node = current_node.next
        raise LinkedListException("Key does not exist.")

    def display(self, forward: bool = True):
        """
        Used to display the list in a human-readable formatted string
        Args:
            forward: a boolean used to reverse the list
        """
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
        """
        the player list head getter
        Returns:
            the head of the player list
        """
        return self._head

    @property
    def tail(self) -> PlayerNode | None:
        """
        the player list tail getter
        Returns:
            the tail of the player list
        """
        return self._tail


class LinkedListException(Exception):
    """
    the exception class
    """
    def __init__(self, message):
        """
        Initialise the exception
        Args:
            message: the message to display when an exception is raised
        """
        self.message = message
