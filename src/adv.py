from room import Room
from player import Player
from item import Item

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

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

def print_no_room(d):
    print(f"There is no room {d:s} of current room")

shouldexit = False
while not shouldexit:
    print("---------------------------------------------")
    print(f"The player is at room {player.room.name:s}")
    print(f"{player.room.description:s}")

    print("List of items in the room")
    for i in player.room.items:
        print(i.name)

    pinput = input("Please enter a command: ")
    if pinput == "q":
        print("Quitting")
        shouldexit = True
        break
    elif pinput == "n":
        if player.room.n_to != None:
            player.room = player.room.n_to
        else:
            print_no_room("n")
    elif pinput == "e":
        if player.room.e_to != None:
            player.room = player.room.e_to
        else:
            print_no_room("e")
    elif pinput == "w":
        if player.room.w_to != None:
            player.room = player.room.w_to
        else:
            print_no_room("w")
    elif pinput == "s":
        if player.room.s_to != None:
            player.room = player.room.s_to
        else:
            print_no_room("s")
    elif pinput == "pick":
        print("Which item would you like to pick")
        
    else:
        print("Invalid command")

    print("---------------------------------------------")

    

