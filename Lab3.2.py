class Item:
    pass

class ValueableItem(Item):
    pass

class TrashItem(Item):
    pass

class Room:
    def __init_(self, is_explorable):
        self.is_explorable = is_explorable
    if is_explorable is False:
        print('Pokój jest zamórowany')
    else:
        self.item =[]

class Map:
    def __init__(self):
        self.rooms = []