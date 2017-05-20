from Item import Item
from Constants import *

class Gold(Item):
    def __init__(self, x, y, value):
        super(Gold, self).__init__(x, y, GOLD, "Gold")
        self.value = value
