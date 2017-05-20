"""A map generator based on random room placement

Edited from the implementation found here: http://roguebasin.roguelikedevelopment.org/index.php?title=Complete_Roguelike_Tutorial,_using_python%2Blibtcod,_part_2#The_Map

For internal use only"""

from Game import Map
import random

MAX_ROOM_SIZE = 8
MIN_ROOM_SIZE = 4
MAX_ROOMS = 20
area = 0

def generate():
    """Returns a generated map"""
    global area

    wall_type = random.randint(0, 1)
    floor_type = random.randint(0, 1)

    area = Map.Map(wall_type, floor_type)
    rooms = []

    for i in range(MAX_ROOMS):
        rooms = generateRoom(rooms)

    for i in range(len(rooms)):
        createRoom(rooms[i])
        
        if i > 0:
            joinRooms(rooms[i-1], rooms[i])

    return area
        


def generateRoom(rooms):
    """Returns a rectangle representing a well-placed room"""
    w = random.randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)
    h = random.randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)

    x = random.randint(0, area.width - w - 1)
    y = random.randint(0, area.height - h - 1)

    room = Rect(x, y, w, h)

    failed = False

    if len(rooms) == 0:
        rooms.append(room)
    else:
        for i in rooms:
            if room.intersects(i):
               failed = True
    
        if not failed:
            rooms.append(room)

    return rooms
        
def joinRooms(r1, r2):
    """Joins two rooms together by tunnels"""

    x1, y1 = r1.centre()
    x2, y2 = r2.centre()
    
    if random.randint(0, 1) == 0:
        carveHorizTunnel(x1, x2, y1)
        carveVertTunnel(y1, y2, x2)
    else:
        carveVertTunnel(y1, y2, x1)
        carveHorizTunnel(x1, x2, y2)

def createRoom(room):
    """Hollows out a room in the map"""
    global area

    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            area.map[x][y].state = Map.Floor

def carveHorizTunnel(x1, x2, y):
    """Carves out a horizontal tunnel in the map"""
    global area
    
    for x in range(min(x1, x2), max(x1, x2) + 1):
        area.map[x][y].state = Map.Floor

def carveVertTunnel(y1, y2, x):
    """Carves out a vertical tunnel in the map"""
    global area
    
    for y in range(min(y1, y2), max(y1, y2) + 1):
        area.map[x][y].state = Map.Floor



class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def centre(self):
        """Returns the x and y values of the centre of the rectangle"""
        centre_x = (self.x1 + self.x2) / 2
        centre_y = (self.y1 + self.y2) / 2

        return (centre_x, centre_y)
 
    def intersects(self, other):
        """Returns whether the rectangle intersects with another"""
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)

    
