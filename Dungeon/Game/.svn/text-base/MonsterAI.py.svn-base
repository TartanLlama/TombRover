from Map import *
import Generator
from Objects import *
import FOV
import Util
from Objects.Constants import *

def moveAI(monsterList, player, area):
    """ Main AI method that moves every monster in the monster list"""
    returnList = []
    for monster in monsterList:
        if monster.getHP() > 0:
            returnVal = attackIfPossible(monster, player)
            if returnVal == None: 
                moved = False
                if area.map[monster.x][monster.y].isInFov():
                    moved = moveAIFov(monster, player, area)
                if not moved:
                    findAlternative(monster, area)
            else:
                returnList.append((monster,returnVal))
    return returnList
                    
def moveAIFov(monster, player, area):
    """ Move a monster which is in the players FOV """
    if monster.hasMorale():
        dx, dy = calculateAIFovMove(player, monster, area, True)
    else:
        dx, dy = calculateAIFovMove(player, monster, area, False)
    
    if dx == 0 and dy == 0:
        return False
    else:
        moveMonster(monster, dx, dy, area)
        return True

def calculateAIFovMove(player, monster, area, toward_player):
    """ Calculate the direction to move """
    playerX = player.x
    playerY = player.y
    monsterX = monster.x
    monsterY = monster.y
    dx = 0
    dy = 0

    direction = 0
    if toward_player:
        direction = 1
    else:
        direction = -1

    moved = False
    if playerX > monsterX:
        if playerY > monsterY and not area.blocked(monsterX + 1*direction, monsterY + 1*direction):
            dy = 1 * direction
            dx = 1 * direction
            moved = True
        elif playerY < monsterY and not area.blocked(monsterX + 1*direction, monsterY - 1*direction):
            dy = -1 * direction
            dx = 1 * direction
            moved = True
        elif not area.blocked(monsterX + 1*direction , monsterY): 
            dx = 1 * direction
            moved = True

                
    if playerX < monsterX:
        if playerY > monsterY and not area.blocked(monsterX -1*direction, monsterY + 1*direction):
            dy = 1 * direction
            dx = -1 * direction
            moved = True
        elif playerY < monsterY and not area.blocked(monsterX - 1*direction, monsterY - 1*direction):
            dy = -1 * direction
            dx = -1 * direction
            moved = True
        elif not area.blocked(monsterX - 1*direction , monsterY): 
            dx = -1 * direction
            moved = True
                
    if not moved and playerY > monsterY and not area.blocked(monsterX, monsterY + 1*direction):
        dy = 1 * direction
    if not moved and playerY < monsterY and not area.blocked(monsterX, monsterY - 1*direction):
        dy = -1 * direction

    return (dx, dy)
 
def moveMonster(monster, dx, dy, area):
    """ Move a monster using delta x and y """
    moveMonsterAbs(monster,monster.x+dx,monster.y+dy,area)

def moveMonsterAbs(monster,x,y,area):
    """ Move a monster using absolute positions """
    area.map[monster.x][monster.y].character = None
    monster.x = x
    monster.y = y
    area.map[monster.x][monster.y].character = monster

""" Find alternative move method """
def findAlternative(monster, area):
    if smellMove(monster, area) == False:
        moveNextFreeSpace(monster,area)
  
def moveNextFreeSpace(monster,area):
    """ Move the monster into the next free space or protect an Item, if all fails the monster moves to a random square """
    surroundArea = Util.getNeighbouringCoords((monster.x,monster.y),1)
    counter = 0
    if findObject(monster,surroundArea,area) == False:
        rInt = Util.roll(1,len(surroundArea))
        while counter < len(surroundArea):
            for (x,y) in surroundArea:
                counter = counter + 1
                if counter >= rInt:
                    if not isBlocked(area,x,y):
                        moveMonsterAbs(monster,x,y,area)
                        return True
                
    return True
                
def findObject(monster,surroundList,area):
    """ helper method to find an item in the surround area of a monster """
    for (x,y) in surroundList:
        itemList = area.map[x][y].getItems()
        for item in itemList:
            if member(item,ITEM):
                return True
    return False
    
def smellMove(monster, area):
    """ Smell the player and move towards him """
    maxSmell = 0

    coords = Util.correctCoords(area.height, area.width, Util.getNeighbouringCoords((monster.x, monster.y), 1))
    
    smells = [(area.map[x][y], x - monster.x, y - monster.y) for (x, y) in coords if area.map[x][y].character == None]
    
    if len(smells) > 0:
        max_smell = max(smells, key=lambda x: x[0].smell_rating)
        
        if max_smell[0].smell_rating > 0:
            moveMonster(monster, max_smell[1], max_smell[2], area)
            return True
    return False

def isBlocked(area,x,y):
    """ Is a given coordinate blocked """
    return area.blocked(x,y)
  
def attackIfPossible(monster, player):
    """ check if a monster can perform an attack """
    dx = player.x - monster.x
    dy = player.y - monster.y
     
    correct = [-1, 0, 1]
    if dx in correct  and dy in correct:
        return monster.attack(player, MELEE)

    return None
