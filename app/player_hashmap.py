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
    SIZE =10

    def __init__(self):
        #Create a total of 10 PlayerList instances individually one at a time.
        self.hashmap = [ PlayerList() for _ in range(self.SIZE) ]
        self.count = 0

    def _get_index(self, key: Player) -> int:
        """
        key must be a Player object
        """
        if not isinstance(key, Player):
            raise TypeError("Key must be a Player object")
        key_value = hash(key)
        return key_value % self.SIZE


    def __setitem__(self, key: Player, name: str) -> None:
        """Add a new player to PlayerList in a corresponding index in the hash map."""
        # 1. Use the key to calculate an index into the hash map
        index = self._get_index(key)
        # 2. Get the PlayerList at that index
        player_info = self.hashmap[index]

        # 3. Check if the player is already on that player list.
        player_node = player_info.find_key(key)
        if player_node: # If it is, update the player's name.
            player_node.player.name = name
            player_node.player.uid = key.uid
        else: # If it isn't, create a player and add the player to the player list.
            new_player = Player(key.uid, name)
            player_info.update_player(new_player)
            self.count += 1



    def __getitem__(self, key: Player):
        """Retrieve a player from the PlayerList with the corresponding index in the hash map"""
        index = self._get_index(key)
        player_info = self.hashmap[index]
        player_node = player_info.find_key(key)
        if player_node:
            return player_node.player.name
        raise KeyError(f"Key {key} not found in PlayerHashMap")


    def __len__(self):
        """Return the number of players in the hash map"""
        return self.count


    def __delitem__(self, key: Player):
        """Remove a player from the PlayerList with the corresponding index in the hash map"""
        index = self._get_index(key)
        player_info = self.hashmap[index]
        player_node = player_info.find_key(key)
        if player_node and player_node.player.uid == key.uid:
            print(f"Delete player ID {key.uid}, Name {player_node.player.name}")
            del self.hashmap[index]
            #self.hashmap[index] = " "
            self.count -= 1
        else:
            raise KeyError(f"Key {key} not found in PlayerHashMap")

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
    hash_map[my_player1] = my_player1.name
    hash_map[my_player2] = my_player2.name


    #Retrieve a player from the PlayerList
    #print(f"Name of UID 1 : {hash_map[my_player]}")
    print(f"Name of UID 2 : {hash_map[my_player1]}")
    print(f"Name of UID 11 : {hash_map[my_player2]}")


    del hash_map[my_player2]
    hash_map.display()
    print(f"len: {len(hash_map)}")







if __name__ == "__main__":
    main()
