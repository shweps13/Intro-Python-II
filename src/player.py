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

    def pick_up(self, item): 
        self.inventory.append(item)
    
    def take_item(self, item, room):
        if len(room.room_items) == 0:
            print(f"This room has no items.")
            return
        e = False
        for i in room.room_items:
            if i[0].item_name == item:
                room.remove_item(i, self)
                print(f"{item} founded!")
                e = True
                break
        if not e:
            print(f"{item} is not here!")