from app.player import Player
class PlayerBNode:
    def __init__(self, player: Player, left = None, right = None):
        self._player = player
        self._left = left
        self._right = right


    @property
    def player(self):
        return self._player

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value

    def __lt__(self, other):
        return self.player.name < other.player.name

    def __eq__(self, other):
        return self.player.name == other.player.name

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}(PlayerName={self.player!r}, left={self.left!r}, right={self.right!r}'

