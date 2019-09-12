# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    room: object
    def __init__(self, room, items = []):
        self.room = room
        self.items = items

    def drop_item(self, name):
        for i in range(len(self.items)):
            item = self.items[i]
            if item.name == name:
                del self.items[i]
                return item
        return item
    
    def add_item(self, item):
        self.items.append(item)