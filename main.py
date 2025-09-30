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


player1 = Player("2", "Test3")
player2 = Player("3", "Test2")
player3 = Player("6", "Test1")
player4 = Player("1", "Test0")
player5 = Player("8", "Test5")
bst = PlayerBST()
bst.insert(player1)
bst.insert(player2)
bst.insert(player3)
bst.insert(player4)
bst.insert(player5)

print(bst)
sorted_players = bst.inOrderTraversal(bst._root)
print(sorted_players)
balanced_root = bst.create_balanced_bst(sorted_players)
bst.print_bst(balanced_root)




# print(bst.search("Test1"))
# print(bst.search("Test2"))
# print(bst.search("Test4"))

