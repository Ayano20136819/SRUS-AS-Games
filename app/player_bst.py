from app.player import Player
from app.player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self, root = None):
        self._root = root

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self._root!r})'




    def insert(self, player, current_root=None):
        if not isinstance(player, PlayerBNode):
            new_node = PlayerBNode(player)
        else:
            new_node = player

        if self._root is None:
            self._root = new_node
            return

        if current_root is None:
            current_root = self._root

        if new_node.player < current_root.player:
            if current_root.left is None:
                current_root.left = new_node
            else:
                self.insert(new_node, current_root.left)

        elif new_node.player > current_root.player:
            if current_root.right is None:
                current_root.right = new_node
            else:
                self.insert(new_node, current_root.right)

        else:
            return


    def search(self, name, current_root=None):
        if current_root is None:
            current_root = self._root

        if current_root is None:
            return None

        print(f"Checking node: {current_root.player.name}")

        if name == current_root.player.name:
            return current_root.player.name
        elif name < current_root.player.name:
            if current_root.left is None:
                return None
            return self.search(name, current_root.left)
        else:
            if current_root.right is None:
                return None
            return self.search(name, current_root.right)







if __name__ == '__main__':
    pass

