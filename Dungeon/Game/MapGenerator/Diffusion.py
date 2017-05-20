"""A map generator using diffusion-limited aggregation

Based on the design description here: http://roguebasin.roguelikedevelopment.org/index.php?title=Diffusion-limited_aggregation

For internal use only"""

from Game import Map
from Game import Util
from Game.Objects import *
import random

NUM_WALKERS = 600

def generate():
    """Returns a generated map"""
    wall_type = random.randint(0, 1)
    floor_type = random.randint(0, 1)

    area = Map.Map(wall_type, floor_type)
    tiles = area.map
    
    setSeed(area)

    for x in range(NUM_WALKERS):
        walker = Walker(getRandTile(area))
        walker.seekSpace(area)

    Util.addBorders(area.map)

    return area

def setSeed(area):
    seed_pos = getCentreTile(area)
        
    neighbours = Util.correctCoords(area.height, area.width, Util.getNeighbouringCoords(seed_pos, 2))
    
    for i in neighbours:
        x, y = i
        area.map[x][y].state = Map.Floor

def getCentreTile(area):
    return (area.height/2, area.width/2)

def getRandTile(area):
    """Gets a random floor tile from the area"""
    x = random.randint(0, area.height - 1)
    y = random.randint(0, area.width - 1)

    rand_tile = area.map[x][y]

    if rand_tile.state == Map.Wall:
        return (x, y)
    else:
        return getRandTile(area)
   
class Walker (Object.Object):
    def __init__(self, position):
        x, y  = position
        super(Walker, self).__init__(x, y)

    def seekSpace(self, area):
        frozen = False
        while not frozen:
            neighbours = Util.correctCoords(area.height, area.width, Util.getNeighbouringCoords((self.x, self.y), 1, Util.ORTHOGONAL))
            for i in neighbours:
                x, y = i
                if area.map[x][y].state == Map.Floor:
                    area.map[self.x][self.y].state = Map.Floor
                    frozen = True
                    break
            if not frozen: 
                self.walk(neighbours)

    def walk(self, neighbours):
        new_pos = random.randint(0, len(neighbours) - 1)
        x, y = neighbours[new_pos]
        self.x = x
        self.y = y
    
