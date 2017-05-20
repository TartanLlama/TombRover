from Map import *
import random
from MapGenerator import *
from Objects import *
import copy
import threading

MAX_NUM_WEAPONS = 2
MAX_NUM_ARMOUR = 2
MAX_NUM_POTIONS = 2
MAX_NUM_SACKS = 1

class Generator(threading.Thread):
    def __init__(self, player_level, maps, at_end, map_number):
        r_gen = [Rooms.generate for x in range(2)] 
        m_gen = [Minefield.generate for y in range(2)]
        c_gen = [Cellular.generate for z in range(2)]
        d_gen = [Diffusion.generate]

        self.generators = r_gen + m_gen + c_gen + d_gen
        self.player_level = player_level
        self.maps = maps
        self.at_end = at_end
        self.map_number = map_number
        threading.Thread.__init__(self)

    def run(self):
        m = self.generateMap()

        if self.at_end:
            index = len(self.maps) - 1
        else:
            index = 0
        
        self.maps[index] = m
                        
    def generateMap(self):
        choice = random.randint(0, len(self.generators) - 1)
    
        generator = self.generators[choice]
        
        m = generator()

        return m
    

    def printMap(self, tiles):
        file = open('out', 'w')
        printstring = ''
        for x in tiles:
            for y in x:
                if y.state == Floor:
                    printstring += '.'
                else:
                    printstring += '#'
            file.write(printstring + '\n')
            printstring = ''


def generateObjects(area, player_level, map_number):
        placeStairs(area)
        placeGold(area, player_level)
        placeFood(area, map_number)
        placeWeapons(area, player_level)
        placeArmour(area, player_level)
        placePotions(area)
        placeSacks(area)
        placeMonsters(area, map_number)
        return area

def placeSacks(area):
    num_sacks = random.randint(0, MAX_NUM_SACKS)
    
    sacks = []
    for i in range(num_sacks):
        sacks.append(Sack.createSack())
        
    for j in sacks:
        x, y = getNoStairsTile(area)
        j.x, j.y = x, y
        area.map[x][y].addItem(j)
    

def placeArmour(area, player_level):
    num_armour = random.randint(0, MAX_NUM_ARMOUR)
    
    armour = []
    for i in range(num_armour):
        armour.append(Armour.createArmour(player_level))
        
    for j in armour:
        x, y = getNoStairsTile(area)
        j.x, j.y = x, y
        area.map[x][y].addItem(j)

def placePotions(area):
    num_potions = random.randint(0, MAX_NUM_POTIONS)
    
    potions = []
    for i in range(num_potions):
        potions.append(Potion.createPotion())
        
    for j in potions:
        x, y = getNoStairsTile(area)
        j.x, j.y = x, y
        area.map[x][y].addItem(j)

def placeWeapons(area, player_level):
    num_weapons = random.randint(0, MAX_NUM_WEAPONS)
    
    weapons = []
    for i in range(num_weapons):
        weapons.append(Weapon.createWeapon(player_level))
        
    for j in weapons:
        x, y = getNoStairsTile(area)
        j.x, j.y = x, y
        area.map[x][y].addItem(j)

                        
def placeFood(area, map_number):
    max_power = map_number+1 * 2

    foods = []
    while max_power > 0:
        food = Food.createFood(max_power)
        foods.append(food)
        max_power -= food.power
            
    for i in foods:
        x, y = getNoStairsTile(area)
        i.x, i.y = x, y
        area.map[x][y].addItem(i)
                                   

def placeMonsters(area, map_number):
    monster_power = map_number+1 * 4
        
    monsters = []
    while monster_power > 0:
        monster = Monster.createMonster(monster_power, map_number)
        monsters.append(monster)
        monster_power -= monster.level
        
    for i in monsters:
        x, y = getNoStairsOrCharacterTile(area)
        i.x, i.y = x, y
        area.map[x][y].character = i
        
          
def placeGold(area, player_level):
    total_gold = pow(player_level, 2) * 100
    
    gold_deposits = []

    while total_gold > 0:
        gold_value = random.randint(1, total_gold)
        gold_deposits.append(gold_value)
        total_gold -= gold_value

    for i in gold_deposits:
        x, y = getNoStairsTile(area)
        
        area.map[x][y].addItem(Gold.Gold(x, y, i))
        

def placeStairs(area):
    x, y = getRandTile(area)

    area.map[x][y].stairs = Staircase.Staircase(x, y, True)
    area.stairs.append((x, y))
        
    valid = False

    while not valid:
        x, y = getRandTile(area)
        valid = area.map[x][y].stairs = Staircase.Staircase(x, y, False)
        
    area.stairs.append((x, y))

def getNoStairsOrCharacterTile(area):
        x, y = getNoStairsTile(area)
        
        if area.map[x][y].character != None:
            return getNoStairsTile(area)
        else:
            return (x, y)
    
def getNoStairsTile(area):
    """Gets a random floor tile which doesn't have any stairs on it"""
    x, y = getRandTile(area)

    if area.map[x][y].containsStairs():
        return getNoStairsTile(area)
    else:
        return (x, y)

def getRandTile(area):
    """Gets a random floor tile from the area"""
    x = random.randint(0, area.width - 1)
    y = random.randint(0, area.height - 1)
    rand_tile = area.map[x][y]

    if rand_tile.state == Floor:
        return (x, y)
    else:
        return getRandTile(area)
