from Item import Item
from Constants import *
import random

POWER, NAME, DESC = range(3)
NUMBER_OF_TRIES = 5

class Food(Item):
    def __init__(self, food, power, x=0, y=0):
        super(Food, self).__init__(x, y, FOOD, food[NAME])
        self.power = power

def createFood(max_power):
    return Food(apple, random.randint(1, max_power))

apple = {NAME : 'Apple'}
