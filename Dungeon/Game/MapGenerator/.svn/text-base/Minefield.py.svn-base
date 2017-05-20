"""Generates a map based on a moles in a minefield approach

For internal use only"""

from Game import Map
from Game import Util
import random
from Game.Objects import Object

NUMBER_OF_MINES = 20
NUMBER_OF_MOLES = 4 #should be no more than 4
MIN_EXPLOSION_SIZE = 3
MAX_EXPLOSION_SIZE = 6
MAX_MOLE_LIFE = 400
MOLE_LIFE_DECAY = 3
area = 0

def generate():
    """Returns a generated map"""
    global area

    wall_type = random.randint(0, 1)
    floor_type = random.randint(0, 1)

    area = Map.Map(wall_type, floor_type)
    
    generateMines()

    centre_x = area.width/2
    centre_y = area.height/2
    
    explode(centre_x, centre_y, MAX_MOLE_LIFE)

    cleanup()

    return area
    
def cleanup():
    """Changes blocked tiles (mines) into wall"""
    global area

    for x in area.map:
        for y in x:
            if y.state == Map.Blocked:
                y.state = Map.Wall

def generateMines():
    """Sets down mines in random locations of the map"""
    global area

    for i in range(NUMBER_OF_MINES):
        x, y = getRandTile(area)
        area.map[x][y].state = Map.Blocked #blocked tiles symbolise mines

def sendMoles(x, y, sides, life):
    """Sends out moles from the sides of the explosion"""
    global area

    for i in range(NUMBER_OF_MOLES):
        Mole(sides[i][0], sides[i][1], life).walk()

        
def explode(x, y, life):
    """Explodes a mine, creating a room and sends out moles"""
    global area

    room_x = random.randint(MIN_EXPLOSION_SIZE, MAX_EXPLOSION_SIZE)
    room_y = random.randint(MIN_EXPLOSION_SIZE, MAX_EXPLOSION_SIZE)

    x_map = range(-room_x, room_x)
    y_map = range(-room_y, room_y)

    #co-ordinates to carve out
    coords = [[x + x_map[i], y + y_map[j]] for i in x_map for j in y_map]
    
    #makes sure that there is still some wall at the border
    coords = filter ((lambda x : x[0] >= 1 and x[1] >= 1 and x[0] < area.width - 1 and x[1] < area.height - 1), coords)

    #EXPLOSION!
    for i in coords:
        new_x, new_y = i
        area.map[new_x][new_y].state = Map.Floor
            
    #calculates the middle of each side of the room
    sides = [[x + x_map[0], y + y_map[len(y_map)/2]],
             [x + x_map[-1], y + y_map[len(y_map)/2]],
             [x + x_map[len(x_map)/2], y + y_map[0]],
             [x + x_map[len(x_map)/2], y + y_map[-1]]]
             

    sendMoles(x, y, sides, life/MOLE_LIFE_DECAY)

def carve(x, y):
    """Carves out a piece of wall"""
    area.map[x][y].state = Map.Floor
        

class Mole(Object.Object):
    """An object representing a mole"""
    def __init__(self, x, y, life):
        super(Mole, self).__init__(x, y)

        self.life = life

    def walk(self):
        """Digs around, away from existing floor if possible"""
        global area
        
        neighbours = Util.getNeighbouringCoords((self.x, self.y), 1, Util.ORTHOGONAL)

        #makes sure that there is still some wall at the border
        neighbours = filter ((lambda x : x[0] >= 1 and x[1] >= 1 and x[0] < area.width - 1 and x[1] < area.height - 1), neighbours)

        self.x, self.y = self.getNewTile(area, neighbours)

        #if there are possible moves
        if self.x != -1:
            if area.map[self.x][self.y].state == Map.Blocked:
                explode(self.x, self.y, self.life)
            else:
                carve(self.x, self.y)
                self.life -= 1
                if self.life > 0:
                    self.walk()

    def getNewTile(self, area, neighbours):
        """Picks a tile to move to"""
        if len(neighbours) == 1:
            return neighbours[0]
        elif len(neighbours) == 0:
            return (-1, -1)

        new_pos = random.randint(0, len(neighbours) - 1)
        x, y = neighbours[new_pos]

        if area.map[x][y].state == Map.Floor:
            neighbours.remove((x, y))
            return self.getNewTile(area, neighbours)
        else:
            return (x, y)
        
def getRandTile(area):
    """Gets a random tile from the area"""
    x = random.randint(0, area.width - 1)
    y = random.randint(0, area.height - 1)
    rand_tile = area.map[x][y]

    return(x, y)
    
