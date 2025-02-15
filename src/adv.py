from room import Room
from player import Player
from item import Item

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [
                         Item("Great-Sword", "A very large sword"),
                         Item("Great-Shield", "A very large shield"),
                         Item("Great-Armor", "A very large armor")
                     ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [
                         Item("Sword", "A normal sword"),
                         Item("Shield", "A normal shield")
                     ]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [
                         Item("Bow", "A normal bow, doesn't require arrow"),
                         Item("Boots", "A cheap footwear")
                     ]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [
                         Item("Red-Potion", "Heals your wounds"),
                         Item("Green-Potion", "Recovers your stamina")
                     ]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [
                         Item("Stone", "A piece of stone")
                     ]),
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
    print(f"List of items the player has: ")
    for i in player.items:
        print(f"-{i.name:s}")

    print(f"The player is at room {player.room.name:s}")
    print(f"{player.room.description:s}")

    print("List of items in the room: ")
    for i in player.room.items:
        print(f"-{i.name:s}")

    pinputs = input("Please enter a command: ").split(" ")
    if len(pinputs) == 1:
        if pinputs[0] == "q":
            print("Quitting")
            shouldexit = True
            break
        elif pinputs[0] == "n":
            if player.room.n_to != None:
                player.room = player.room.n_to
            else:
                print_no_room("n")
        elif pinputs[0] == "e":
            if player.room.e_to != None:
                player.room = player.room.e_to
            else:
                print_no_room("e")
        elif pinputs[0] == "w":
            if player.room.w_to != None:
                player.room = player.room.w_to
            else:
                print_no_room("w")
        elif pinputs[0] == "s":
            if player.room.s_to != None:
                player.room = player.room.s_to
            else:
                print_no_room("s")
        else:
            print("Invalid command")
    elif len(pinputs) == 2:
        if pinputs[0] == "pick":
            item_name = pinputs[1]
            item = player.room.pick_item(item_name)
            if item != None:
                player.add_item(item)
                item.on_pick()
            else:
                print(f"Item name {item_name:s} does not exist")
        elif pinputs[0] == "drop":
            item_name = pinputs[1]
            item = player.drop_item(item_name)
            if item != None:
                player.room.add_item(item)
                item.on_drop()
            else:
                print(f"Item name {item_name:s} does not exist")
        else:
            print("Invalid command")
    else:
        print("Invalid command")

    print("---------------------------------------------")

    

