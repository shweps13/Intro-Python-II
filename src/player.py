# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def change_room(self, new_room):
        self.current_room = new_room

    def show_inventory(self):
        if len(self.inventory) == 0:
            return "Empty"
        else:
            return ', '.join(str(v) for v in self.inventory)