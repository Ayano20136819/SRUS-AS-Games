# -------------------------------
#
# Folder: app
# Filename: player_hashmap
# Author: Ayano SASAKIDO
# Version 0.0
# Created: 
#
# -------------------------------
# Imports
# -------------------------------
from app.player import Player
from app.player_list import PlayerList

class PlayerHashMap:
    def __init__(self, size=10):
        self.size = size
        #Create a total of 10 PlayerList instances individually one at a time.
        self.hashmap = [ PlayerList() for _ in range(self.size) ]
        self.count = 0

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            print("This is Player instance")
            key = int(key.uid)
            print(f"key: {key}")
            return key % self.size
        else:
            print("This is not Player instance")



    def __setitem__(self, key: Player, name: str) -> None:
        """Add a new player to PlayerList in a corresponding index in the hash map."""
        # 1. Use the key to calculate an index into the hash map
        index = self.get_index(key)
        print(f"Index: {index}")
        # 2. Get the PlayerList at that index
        player_info = self.hashmap[index]

        # 3. Check if the player is already on that player list.
        player_node = player_info.find_key(key)
        print(f"Existing Player: {player_node}")
        if player_node: # If it is, update the player's name.
            print(f"Update player ID {key.uid} Old name {player_node.player.name} - New {name} ")
            player_node.player.name = name
            player_node.player.uid = key.uid
        else: # If it isn't, create a player and add the player to the player list.
            print(f"Add new player ID: {key.uid}, Name: {name}")
            new_player = Player(key.uid, name)
            player_info.update_player(new_player)
            self.count += 1



    def __getitem__(self, key: Player):
        """Retrieve a player from the PlayerList with the corresponding index in the hash map"""
        print("Retrieve a player from the PlayerList")
        index = self.get_index(key)
        print(f"Index: {index}")
        player_info = self.hashmap[index]
        player_node = player_info.find_key(key)
        if player_node:
            return player_node.player.name
        else:
            return None


    def __len__(self):
        """Return the number of players in the hash map"""
        return self.count


    def __delitem__(self, key: Player):
        """Remove a player from the PlayerList with the corresponding index in the hash map"""
        index = self.get_index(key)
        print(f"Delete index {index}")
        player_info = self.hashmap[index]
        player_node = player_info.find_key(key)
        if player_node and player_node.player.uid == key.uid:
            print(f"Delete player ID {key.uid}, Name {player_node.player.name}")
            self.hashmap[index] = " "
            self.count -= 1
        else:
            print(f"Delete player ID {key.uid} not found in hash map")


    def display(self):
        print("--Current Players in HashMap ---")
        for i, player_list in enumerate(self.hashmap):
            print(f"Index {i}: {player_list}")





def main():
    # get the player's appropriate PlayerList:
    hash_map = PlayerHashMap()

    # add new player
    my_player = Player("1", "Alice")
    my_player1 = Player("2", "Bob")
    my_player2 = Player("11", "Charlie")


    # check if the player is in the list
    # If it is, update the player's name
    # If it isn't, create a player and add the player to the player list
    hash_map[my_player] = my_player.name
    print(f"Name: {hash_map[my_player]}")
    hash_map[my_player1] = my_player1.name
    hash_map.display()
    hash_map[my_player2] = my_player2.name
    hash_map.display()
    print(f"len: {len(hash_map)}")


    #Retrieve a player from the PlayerList
    #print(f"Name of UID 1 : {hash_map[my_player]}")
    print(f"Name of UID 2 : {hash_map[my_player1]}")
    print(f"Name of UID 11 : {hash_map[my_player2]}")


    del hash_map[my_player2]
    hash_map.display()
    print(f"len: {len(hash_map)}")







if __name__ == "__main__":
    main()
