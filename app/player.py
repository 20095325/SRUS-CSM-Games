from __future__ import annotations


class Player:
    def __init__(self, unique_id: str = None, player_name: str = None) -> None:
        self._uid: str | None = unique_id
        self._name: str | None = player_name

    def __str__(self) -> str:
        return f'Player: {self._uid}, {self._name}'

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._name
