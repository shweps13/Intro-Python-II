from room import Room
from player import Player
from item import Item

# Declare all the rooms


item = {
    'key': Item("Key", """Miscarcand Key is the key to the kingdom beneath 
Ayleid Ruin of Miscarcand, and it allows for a quick exit without having to travel 
through the labyrinth of Morimath or Sel Vanua"""),

    'lockpick': Item("Lockpick", """A Lockpick is a tool used for picking the locks of 
doors and chests."""),

    'scroll': Item("Scroll", """The scroll deals Shock Damage in a 
large area and also grants Shock Resistance."""),

    'pickaxe': Item("Pickaxe", """The pickaxe is a small sharp 
bladed tool used to mine for ore and dig through rock."""),

    'dagger': Item("Dagger", """Simple and workable weapon"""),
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item["scroll"]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [[item["pickaxe"]], [item["dagger"]], [item["key"]]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item["lockpick"]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item["key"]]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# print(room['outside'].n_to.name)
# print(room['foyer'].name)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print("---<===================================>---")
print("     Welcome to the Lambda Trail game!")
print("---<===================================>---")



name = input("Enter your name, hero:")

nowlocation = room['outside']

player = Player(name, nowlocation)

print("\nWelcome to the lands of might and magic,", player.name)
print("Right now you at", player.current_room.room_name, "- looks like there is a lot of adventures, huh?")
print("===========================================")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

playmode = True
print("                -=loading=-                ")
print("===========================================")

print("You can move in different sides to explore \n")
print("                    [n]                      ")
print("                     ^                       ")
print("               [w] <   > [e]                 ")
print("                     v                       ")
print("                    [s]                      ")
print("\nUse letters to move to [n]orth, [s]outh, [e]ast, [w]est")
print("You can check rooms to find items by [c]hek command")
print("Also, you can check your [i]nventory")
print("\nType [q] fot quit")
print("===========================================")


while playmode is True:
    print(f"\n[{player.name}], you at -= {player.current_room.room_name} =-")
    action = input("Your move ==>")
    if action == "q" or action == "quit" or action == "exit":
        print("\n--= bye-bye =--")
        playmode = False
    elif action == "c" or action == "check":
        print(f"\nItems in room: {nowlocation.show_items()}")
    elif action == "i" or action == "inventory":
        print(f"\nInventory: {player.show_inventory()}")
    elif action == "n" or action == "north":
        if hasattr(nowlocation, "n_to"):
            nowlocation = nowlocation.n_to
            player.change_room(nowlocation)
        else:
            print("\n--= Movement isn't allowed =--")
    elif action == "s" or action == "south":
        if hasattr(nowlocation, "s_to"):
            nowlocation = nowlocation.s_to
            player.change_room(nowlocation)
        else:
            print("\n--= Movement isn't allowed =--")
    elif action == "e" or action == "east":
        if hasattr(nowlocation, "e_to"):
            nowlocation = nowlocation.e_to
            player.change_room(nowlocation)
        else:
            print("\n--= Movement isn't allowed =--")
    elif action == "w" or action == "west":
        if hasattr(nowlocation, "w_to"):
            nowlocation = nowlocation.w_to
            player.change_room(nowlocation)
        else:
            print("\n--= Movement isn't allowed =--")
    else:
        print("\n--= Movement isn't allowed =--")
