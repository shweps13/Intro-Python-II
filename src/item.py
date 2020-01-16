class Item:
    def __init__(self, item_name = None, item_description = None):
        self.item_name = item_name
        self.item_description = item_description

    def __str__(self):
        return "{}".format(self.item_name)

    def __repr__(self):
        return "{}".format(self.item_name)

    def print_description(self):
        return "Item: {}, {}".format(self.item_name, self.item_description)
