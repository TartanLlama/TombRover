import random
from Item import Item
from Constants import *

NAME, TYPE, DEF = range(3)

class Armour(Item):
    def __init__(self, arm, defence, x=0, y=0):
        super(Armour, self).__init__(x, y, type=arm[TYPE], name=arm[NAME])
        self.defence = defence

def createArmour(player_level):
    defence_range = range((player_level+1)/2 - 1, (player_level+1)/2 + 1)
    defence_range = filter((lambda x : x >= 0), defence_range)

    defence = random.randint(defence_range[0], min(defence_range[-1], len(armour)-1))

    return Armour(armour[defence], defence + 1)

armour = [{NAME:'Padded armour', TYPE:PADDED},
          {NAME:'Leather armour', TYPE:LEATHER},
          {NAME:'Studded armour', TYPE:STUDDED_LEATHER},
          {NAME:'Scale mail', TYPE:SCALE},
          {NAME:'Chainmail', TYPE:CHAIN},
          {NAME:'Banded mail', TYPE:BANDED},
          {NAME:'Half-plate', TYPE:HALF_PLATE},
          {NAME:'Full-plate', TYPE:FULL_PLATE}]
