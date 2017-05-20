from Item import Item
from Player import Player
from Constants import *
import random

NAME, EFF, TYPE, TIME = range(4)

class Potion(Item):
    def __init__(self, pot, x=0, y=0):
        super(Potion, self).__init__(x, y, pot[TYPE], pot[NAME]) 
        self.time = pot[TIME]

def createPotion():
    return Potion(potions[random.randint(0, len(potions)-1)])

potions = [{NAME:'Strength Potion', TYPE:STR_POT, TIME:1},
           {NAME:'Dexterity Potion', TYPE:DEX_POT, TIME:1},
           {NAME:'Iron Skin Potion', TYPE:INVINCIBLE_POT, TIME:1},
           {NAME:'Health Potion', TYPE:HEALTH_POT, TIME:0},
           {NAME:'Knowledge Potion', TYPE:KNOWLEDGE_POT, TIME:0},
           {NAME:'Berserk Potion', TYPE:BERSERK_POT, TIME:1}]
