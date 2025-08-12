from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList


player = Player("2","Test")
print(f"Player info: {player}")
node = PlayerNode(player)
print(f"Node info: {node}")

print(node.key())

list = PlayerList()
list.insert_tail(1, "test1")
list.insert_tail(2, "test2")
list.insert_tail(3, "test3")



list.find_tail()

print("List forward:")
list.display(True)

print("List backward:")
list.display(False)
