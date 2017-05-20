import random
import Map

ORTHOGONAL, DIAGONAL, DIORTHOGONAL = range(3)

def roll(number, sides):
    score = 0
    for x in range(number):
        score += random.randint(1, sides)
    return score

def filterDictionary(data, function = lambda k, v : True):
    new_dict = {}

    for k, v in d.items():
        if predicate(k, v):
            new_dict[k] = v

def getNeighbouringCoords(tile_pos, radius, directions = DIORTHOGONAL):
    x, y = tile_pos
    fast_map = range(-radius, radius + 1)
    
    if directions == ORTHOGONAL:
        condition = lambda x : abs(x[0]) != abs(x[1])
    elif directions == DIAGONAL:
        condition = lambda x : abs(x[0]) == abs(x[1])
    else:
        condition = lambda x : True
 
    neighbours = [(x + i, y + j) for i in fast_map for j in fast_map if condition((i, j))]
    
    return neighbours

def addBorders(tiles):
    for x in range(len(tiles)):
        tiles[x][0] = Map.Tile(Map.Wall)
        tiles[x][len(tiles)-1] = Map.Tile(Map.Wall)
    for y in range(len(tiles)):
        tiles[0][y] = Map.Tile(Map.Wall)
        tiles[len(tiles)-1][y] = Map.Tile(Map.Wall)
                       


def correctCoords(height, width, coords):
    return filter ((lambda x : x[0] >= 0 and x[1] >= 0 and x[0] < width and x[1] < height), coords)

def distanceBetween(x1, y1, x2, y2):
   return max(max(x1, x2) - min(x1, x2), max(y1, y2) - min(y1, y2))
