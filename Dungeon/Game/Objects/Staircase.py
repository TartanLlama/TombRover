from Item import Item
from Constants import *

class Staircase(Item):
    def __init__(self, x, y, up):
        t = 0
        if up:
            t = UP
        else:
            t = DOWN
        super(Staircase, self).__init__(x, y, t, "Staircase",False)
        
        
