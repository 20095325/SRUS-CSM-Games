class Player:
    def __init__(self, uid: str = None, name: str = None) -> None:
        self._uid: str = uid
        self._name: str = name

    def __str__(self) -> str:
        return f'Player: {self._uid}, {self._name}'