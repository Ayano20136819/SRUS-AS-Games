from app.player import Player
class PlayerBNode:
    def __init__(self, player: Player, left = None, right = None):
        self._player = player
        self._left = left
        self._right = right


    @property
    def player(self):
        return self.player

    @property
    def left(self):
        return self.left

    @left.setter
    def left(self, value):
        self.left = value

    @property
    def right(self):
        return self.right

    @right.setter
    def right(self, value):
        self.right = value

