"""A random map generator based on Cellular Automata

Based on the design description here: http://roguebasin.roguelikedevelopment.org/index.php?title=Cellular_Automata_Method_for_Generating_Random_Cave-Like_Levels

For internal use only"""
import random
from Game import Map
from Game import Util
import copy
import sys

WALL_PROB = 40 #the percentage chance of a wall being placed on initialisation

def generate():
    """Returns a generated map"""
    sys.setrecursionlimit(5000)
    
    wall_type = random.randint(0, 1)
    floor_type = random.randint(0, 1)

    start_map = Map.Map(wall_type, floor_type)

    tiles = initWalls(start_map)
    start_map.map = tiles

    tiles = automate(start_map)

    start_map.map = tiles

    if checkAccessible(start_map):
        return start_map
    else:
        return generate()

def initWalls(start_map):
    """Places walls with 40% probability, otherwise floors

    Also places borders"""

    tiles = start_map.map

    #randomise walls
    for x in range(len(tiles)):
        tiles[x] = map (stateMap, tiles[x])

    Util.addBorders(tiles)

    return tiles

def stateMap(tile):
    """Picks a wall or floor tile to return"""

    if random.randint(1, 100) < WALL_PROB:
        return Map.Tile(Map.Wall)
    else:
        return Map.Tile(Map.Floor)


def automate(area):
    """Uses cellular automata to generate a vaugely sensible map"""

    tiles = area.map
    new_tiles = copy.deepcopy(tiles)
    
    for x in range(3):
        for y in range(len(tiles)):
            for z in range(len(tiles[0])):
                if getNeighbouringWalls(tiles, area.width, area.height, (y, z), 1) >= 5 or getNeighbouringWalls(tiles, area.width, area.height, (y, z), 2) <= 2:
                    new_tiles[y][z].state = Map.Wall
                else:
                    new_tiles[y][z].state = Map.Floor

        tiles = copy.deepcopy(new_tiles)
            
    for x in range(1):
        for y in range(len(tiles)):
            for z in range(len(tiles[0])):
                if getNeighbouringWalls(tiles, area.width, area.height, (y, z), 1) >= 4:
                    new_tiles[y][z].state = Map.Wall
                else:
                    new_tiles[y][z].state = Map.Floor
        tiles = copy.deepcopy(new_tiles)
    

    return tiles
        
def getNeighbouringWalls(tiles, width, height, tile_pos, radius):
    """Returns the number of walls in a certain radius from a co-ordinate"""
    coords = Util.getNeighbouringCoords(tile_pos, radius)
    coords = Util.correctCoords(height, width, coords)

    num_walls = pow((1 + radius*2), 2) - len(coords)

    coords.remove(tile_pos)
    
    area = [tiles[x[0]][x[1]] for x in coords]

    num_walls += reduce ((lambda x, y : x + (y.state == Map.Wall)), area, 0)
    return num_walls

def checkAccessible(area):
    """Returns if all the floor is accessible"""
    tiles = area.map
    tile_pos  = getRandTile(area)

    sendAreaPulse(tile_pos, area)
    return allAccessible(tiles)

def allAccessible(tiles):
    """Checks whether the processed tiles are accessible"""
    not_accessible = [y for x in tiles for y in x if not y.checked and y.state == Map.Floor]
   
    return len(not_accessible) == 0
    
def sendAreaPulse(tile_pos, area):
    """Sends out a pulse from a random floor tile and marks all floor accessible from that tile"""
    tiles = area.map
    x, y = tile_pos
    
    if not tiles[x][y].checked and tiles[x][y].state == Map.Floor:
        tiles[x][y].checked = True

        neighbours = Util.correctCoords(area.height, area.width, Util.getNeighbouringCoords(tile_pos, 1))

        for x in neighbours:
            sendAreaPulse(x, area)
    
def getRandTile(area):
    """Gets a random floor tile from the area"""
    x = random.randint(0, area.width - 1)
    y = random.randint(0, area.height - 1)
    rand_tile = area.map[x][y]

    if rand_tile.state == Map.Floor:
        return (x, y)
    else:
        return getRandTile(area)
    



