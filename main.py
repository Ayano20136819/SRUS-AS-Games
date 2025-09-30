from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList
from app.player_bst import PlayerBST


# player = Player("2","Test")
# print(f"Player info: {player}")
# node = PlayerNode(player)
# print(f"Node info: {node}")

# print(node.key())

#list = PlayerList()
# list.insert_tail(1, "test1")
# list.insert_tail(2, "test2")
# list.insert_tail(3, "test3")



# print("List forward:")
# list.display(True)
# print()
# print("List backward:")
# list.display(False)
# print()
# player = Player("101", "Test")
# print(player) # call __str__
# player.uid = "201" # setter uid
# print(player.uid) # getter uid
# player.name = "test"
# print(player.name)


player1 = Player("2", "Test1")
player2 = Player("3", "Test2")
player3 = Player("6", "Test3")
bst = PlayerBST()
bst.insert(player1)
bst.insert(player2)
bst.insert(player3)
print(bst)

