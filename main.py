from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList
from app.player_hashmap import PlayerHashMap

player = Player("20987","Test")
list = PlayerList()
list.insert_tail(1, "test1")
list.insert_tail(2, "test2")
list.insert_tail(3, "test3")

print("List forward:")
list.display(True)

# print("List backward:")
# list.display(False)

