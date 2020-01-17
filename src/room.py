# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room_name, room_description, room_items = []):
        self.room_name = room_name
        self.room_description = room_description
        self.room_items = room_items

    def show_items(self):
        if len(self.room_items) == 0:
            return "This room have no items"
        elif len(self.room_items) == 1:
            return "You can pick [{}] here".format(self.room_items[0])
        else:
            return "{} can be picked here".format(', '.join(str(v) for v in self.room_items))
    
    def __str__(self):
        return "{} \nRoom Description: {}".format(self.room_name, self.room_description)
