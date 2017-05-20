from Constants import *
from Item import Item
import random

class Sack(Item):
    def __init__(self, size, x=0, y=0, type=SACK, name="Sack"):
        super(Sack, self).__init__(x, y, type, name)
        self.size = size

def createSack():
    size = random.randint(1, 4)
    
    return Sack(size)
    
