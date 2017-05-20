from Objects.Constants import *

Blocked, Wall, Floor = range(3)
class Map:
    """A class representing one map level"""
    def __init__(self, wall_type, floor_type, rows = 50, colums = 50):
        self.height = rows
        self.width = colums
        self.wall_type = wall_type
        self.floor_type = floor_type
        self.stairs = []
        self.objects_generated = False
        self.map = [[Tile(Wall) for x in range(self.width)] for y in range(self.height)]

    def getFloorType(self):
        return self.floor_type

    def getWallType(self):
        return self.wall_type

    def getMap(self):
        """Returns the tile grid which represents the map"""
        return self.map

    def blocked(self, x, y):
        """Returns if a given tile is blocked or not. 

        Will handle put of bounds input nicely"""
        return self.opaque(x, y) or self.map[x][y].state == Blocked or (self.map[x][y].character != None and member(self.map[x][y].character, MONSTER))

    def opaque(self, x, y):
        """Returns if a given tile is opaque or not.

        Will handle out of bounds input nicely"""
        return (x < 0 or y < 0 or x >= self.width or y >= self.height
                or self.map[x][y].state == Wall)

class Tile:
    """A class representing one tile of the map grid"""
    def __init__(self, state):
        self.items = []
        self.stairs = None
        self.character = None
        self.state = state
        self.inFov = False
        self.visited = False
        self.smell_rating = 0
        self.checked = False #for use with dungeon generators

    def addItem(self, item):
        if not self.containsStairs():
            self.items.append(item)
            return True
        else:
            return False

    def removeItem(self, item):
        self.items.remove(item)

    def containsStairs(self):
        return self.stairs != None

    def getItems(self):
        """Returns a list of all of the items on the tile"""
        return self.items

    def getItemsDictionary(self):
        dic = [(chr(97 + x), self.items[x]) for x in range(len(self.items))]
        return dict(dic)

    def getCharacter(self):
        """Returns the character standing on the tile"""
        return self.character

    def getState(self):
        """Returns the state of the tile.

        This can be:
                    Blocked
                    Wall
                    Floor

        The idea is that Floor can be seen through and walked on, Blocked tiles can only be seen through and neither apply to wall tiles.""" 
        return self.state

    def isInFov(self):
        """Returns if the tile is in the player's field of view or not"""
        return self.inFov

    def isVisited(self):
        """Returns if the tile has been visited or not"""
        return self.visited
