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


    def inOrderTraversal(self, current_node, result= None):
        if result is None:
            result = []

        if current_node is not None:
            self.inOrderTraversal(current_node.left, result)
            result.append(current_node.player)
            self.inOrderTraversal(current_node.right, result)
        return result


    def create_balanced_bst(self, sorted_list):
        if sorted_list is None:
            return

        if len(sorted_list) == 0:
            return
        elif len(sorted_list) % 2 == 0:
            middle = len(sorted_list) // 2
        else:
            middle = (len(sorted_list) - 1) // 2

        print(f"middle index: {middle}")

        root_player = sorted_list[middle]
        print(f"root_player: {root_player}")
        root_node = PlayerBNode(root_player)

        root_node.left = self.create_balanced_bst(sorted_list[:middle])
        root_node.right = self.create_balanced_bst(sorted_list[middle + 1 :])

        return root_node

    def print_bst(self, node, level=0):
        if node is not None:
            self.print_bst(node.right, level + 1)
            print("    " * level + f"- {node.player.name}")
            self.print_bst(node.left, level + 1)







if __name__ == '__main__':
    pass

