"""A class representing the game state

Simply call the constructor with no parameters to create a world with one map"""
from Map import *
import Generator
from Objects import *
import FOV
import Util
from Objects.CharacterClass import *
import time
import copy
import MonsterAI

MAX_NUMBER_OF_MAPS = 10
xp_form = lambda mlvl, plvl : min(mlvl, plvl)*100+(mlvl-plvl)*10*pow(min(mlvl, plvl), 2)
score_form = lambda maplvl, plvl, gold : int((((maplvl+1)*1.0)/2) * (((plvl+1)*1.0)/2) * gold)

class World:
    def __init__(self, player_class=fighter):
        self.maps = []
        self.player = Player.Player(player_class)
        self.current_map = 0
        self.base_level = 0
        self.addMap()
        
        self.checkMapGenerated()
        self.maps[self.current_map - self.base_level] = Generator.generateObjects(self.getCurrentMap(), self.player.level, self.current_map)
        self.getCurrentMap().objects_generated = True
        self.putPlayerOnStairs(True)
        self.processFov()
        self.turn_messages = []
        
        self.addMap()
        
    def checkMapGenerated(self):
        """checks if map generation is complete for the currently generating map"""
        while self.getCurrentMap() == None:
            time.sleep(0.1)
            
    def getPlayerLevel(self):
        """returns the player's character level"""
        return self.player.getLevel()

    def getPlayerHp(self):
        """returns the player's current hp and max hp"""
        return (self.player.hp, self.player.max_hp)

    def getInventory(self):
        """returns the player's inventory"""
        return self.player.getInv()

    def pickUpItem(self, item):
        """given an item, make the player pick it up"""
        self.turn_messages = []

        success = self.player.addInv(item)
        if success != None:
            self.getPlayerTile().removeItem(item)
            self.turn_messages.append('Picked up ' + success + '.')
        else:
            self.turn_messages.append('Inventory full')

        self.updateGame()
  
    def getPlayerExperience(self):
        """returns the experience cap for the previous player level, the player's current experience and the experience needed to reach the next character level"""
        return (self.player.previous_level, self.player.xp, self.player.next_level)

    def checkInInv(self, symbol):
        """returns true is a certain item symbol is in the player's inventory"""
        inv = self.getInventory()
        
        if symbol in inv:
            return True
        else:
            self.turn_messages.append('Not in inventory')
            return False

    def getMonsterFov(self):
        """returns the monsters which are in the field of with a symbol to correspond ot them"""
        current_letter = 97
        mons_dict = {}
        for i in self.getCurrentMap().map:
            for j in i:
                if j.inFov and j.character != None and member(j.character, MONSTER):
                    mons_dict[chr(current_letter)] = j.character 
                    current_letter += 1

        return mons_dict

    def fireAtMonster(self, monster):
        """fires with a ranged weapon at a given monster"""
        self.turn_messages = []
        if Util.distanceBetween(self.player.x, self.player.y, monster.x, monster.y) == 1:
            self.playerAttack(monster, MELEE)
        else:
            self.playerAttack(monster, RANGED)


    def playerWieldingRanged(self):
        """returns true if the player is wielding a ranged weapon"""
        return self.player.weapon != None and member(self.player.weapon, RANGED)

    def playerWear(self, symbol):
        """given an item symbol, make the player wear the corresponding piece of armour if there is one"""
        self.turn_messages = []

        if self.checkInInv(symbol):
            success = self.player.wear(symbol)

            if success != None:
                self.turn_messages.append('Put on ' + success + '.')
                self.updateGame()
            else:
                self.turn_messages.append('Can\'t put that on.')

            
    def playerTakeOff(self):
        """makes the player take off any item of armour which they are wearing"""
        self.turn_messages = []

        success = self.player.takeOff()
        
        if success != None:
            self.turn_messages.append('Took off ' + success + '.')
            self.updateGame()
        else:
            self.turn_messages.append(message = 'Nothing to take off.')

    def playerWielding(self):
        """returns true if the player is wielding a weapon"""
        return self.player.weapon != None

    def playerWield(self, symbol):
        """given an item symbol makes the player wield the corresponding weapon if there is one"""
        self.turn_messages = []
        
        if self.checkInInv(symbol):
            success = self.player.wield(symbol)

            if success != None:
                self.turn_messages.append('Equipped ' + success + '.')
                self.updateGame()
            else:
                self.turn_messages.append('Can\'t wield that.')

            
    def playerEat(self, symbol):
        """given an item symbol makes the player eat the corresponding item of food if there is one"""
        self.turn_messages = []
        
        if self.checkInInv(symbol):
            success = self.player.eat(symbol)

            if success != None:
                self.turn_messages.append('Ate some food and gained ' + str(success) + ' hp.')
                self.updateGame()
            else:
                self.turn_messages.append('Can\'t eat that')

    def playerQuaff(self, symbol):
        """given an item symbol makes the player drink the corresponding potion if there is one"""
        self.turn_messages = []

        if self.checkInInv(symbol):
            success = self.player.quaffPotion(symbol)

            if success:
                self.turn_messages.append('Quaffed potion')
                self.updateGame()
            elif success == False:
                self.turn_messages.append('Can\'t quaff that')
            else:
                self.turn_messages.append('Already under potion effects. Don\'t overdose!')
            

    def playerDrop(self, symbol):
        """given an item symbol makes the player drop the corresponding item if there is one"""
        self.turn_messages = []
        
        if self.checkInInv(symbol):
            item = self.player.removeInv(symbol)

            item.x, item.y = self.player.x, self.player.y
            self.getCurrentMap().map[item.x][item.y].items.append(item)
            self.turn_messages.append('Dropped ' + item.name + '.')
            self.updateGame()

    def playerUnwield(self):
        """makes the player unequip any weapons which they are wielding"""
        self.turn_messages = []

        success = self.player.unwield()

        if success != None:
            self.turn_messages.append('Unequipped ' + success + '.')
            self.updateGame()
        else:
            self.turn_messages.append('Nothing to unequip.')

            
    def getPlayerGold(self):
        """returns the amount of gold which the player has"""
        return self.player.gold

    def getPlayerInv(self):
        """returns the player's inventory"""
        return self.player.getInv()

    def getMaxInv(self):
        """returns the max number of items which the player can hold in their inventory"""
        return self.player.max_inv

    def addMap(self):
        """Helper method to generate a new map and add it to the current list"""
        self.maps.append(None)
        gen = Generator.Generator(self.player.getLevel(), self.maps, True, self.current_map)
        gen.start()
        

    def getCurrentMap(self):
        """Returns a Map object representing the current level"""
        return self.maps[self.current_map - self.base_level]

    def getPlayer(self):
        """Returns the current Player object"""
        return self.player

    def getMaps(self):
        """Returns the maps currently held"""
        return self.maps

    def goDown(self):
        """Moves the player down a level"""
        
        if self.getPlayerTile().containsStairs() and member(self.getPlayerTile().stairs, DOWN):
            self.removeFromTile(self.player)
            self.current_map += 1

            self.checkMapGenerated()
            #generates map objects if they haven't already been
            if not self.getCurrentMap().objects_generated:
                self.getCurrentMap().objects_generated = True 
                self.maps[self.current_map - self.base_level] = Generator.generateObjects(self.getCurrentMap(), self.player.level, self.current_map)

            #starts generating a new level if one is needed one map below
            if len(self.maps) - 1 == self.current_map - self.base_level:
                self.addMap()
                                
                if len(self.maps) > MAX_NUMBER_OF_MAPS:
                    self.base_level += 1
                    self.maps.pop(0)

            self.putPlayerOnStairs(True)
            self.processFov()
            

    def goUp(self):
        """Moves the player up a level"""
        if self.getPlayerTile().containsStairs() and member(self.getPlayerTile().stairs, UP) and self.current_map > 0:
            self.removeFromTile(self.player)
            self.current_map -= 1
            
            self.checkMapGenerated()
            #generates map objects if they haven't already been
            if not self.getCurrentMap().objects_generated:
                self.getCurrentMap().objects_generated = True 
                self.maps[self.current_map - self.base_level] = Generator.generateObjects(self.getCurrentMap(), self.player.level, self.current_map)

            #starts generating a new level if one is needed one map above
            if self.base_level > 0 and self.current_map - self.base_level == 0 and len(self.maps) == MAX_NUMBER_OF_MAPS:
                self.base_level -= 1
                self.maps.insert(0, None)
                self.maps.pop()
                
                gen.start()
                                
            self.putPlayerOnStairs(False)
            self.processFov()

    def putPlayerOnStairs(self, stairs_up):
        """Puts the player in the right position of the map to start"""
        self.player.x, self.player.y = self.getCurrentMap().stairs[not stairs_up]
        self.addToTile(self.player)
        
    def processFov(self):
        """Checks FOV in the current map"""
        self.getCurrentMap().map = FOV.FOV(self.getCurrentMap().map).do_fov(self.player.x, self.player.y, self.player.sight)

    def playerHere(self, tile):
        """Returns if the player is on a given tile"""
        return tile.character == self.player

    def movePlayer(self, dx, dy):
        """Move the player by the specified amounts"""
        self.turn_messages = []
        new_x = self.player.x + dx
        new_y = self.player.y + dy

        if not self.getCurrentMap().blocked(new_x, new_y):
            self.removeFromTile(self.player)
            self.player.x = new_x
            self.player.y = new_y
            self.addToTile(self.player)
            self.autoGet()
            self.updateGame()

        char = self.getCurrentMap().map[new_x][new_y].character
        if char != None and member(char, MONSTER):
            self.playerAttack(char, MELEE)


    def playerAttack(self, monster, attack_type):
        """attacks a given monster with a melee or ranged attack"""
        outcome = self.player.attack(monster, attack_type)
        self.turn_messages.append(self.parseAttackMessage(outcome, self.player, monster))

        if monster.hp <= 0:
            xp_gain = xp_form(monster.level, self.player.level)
            self.turn_messages.append(self.parseKillMessage(monster, xp_gain))
            self.removeFromTile(monster)
            levelled_up = self.player.increaseXP(xp_gain)
            monster = None

            if levelled_up:
                self.turn_messages.append('Welcome to experience level ' + str(self.player.level) + '!')
        self.updateGame()
                

    def autoGet(self):
        "automatically picks up any gold or sacks in the tile which the player is on"""
        for i in self.getPlayerTile().items:
            if member(i, GOLD):
                self.player.increaseGold(i.value)
                self.getPlayerTile().removeItem(i)
            elif member(i, SACK):
                self.player.increaseInv(i.size)
                self.getPlayerTile().removeItem(i)

    def playerDead(self):
        return self.player.hp <= 0

    def getScore(self):
        """calulates annd returns the player's score"""
        return score_form(self.current_map, self.player.level, self.player.gold)

    def parseKillMessage(self, monster, xp_gain):
        """parses and returns an output message for when a kill occurs"""
        return 'You kill the ' + monster.name + ', gaining ' + str(xp_gain) + ' experience.'
    
    def parseAttackMessage(self, outcome, attacker, defender):
        """parses and returns an output message for when an attack occurs"""
        hit, damage = outcome
        if hit < 2: #hit or crit
            hit = 'hits, dealing ' + str(damage) + ' damage.'
        else:
            hit = 'misses.'
        message = ''
        if member(attacker, PLAYER):
            message += 'Your attack on the ' + defender.name + ' ' 
        else:
            message += 'The ' + attacker.name + ' attacks you and '

        message += hit 

        return message
            
    def getPlayerTile(self):
        """returns the tile which the player is on"""
        return self.getCurrentMap().map[self.player.x][self.player.y]

    def updateGame(self):
        """Updates the rest of the game"""
        monster_list = [j.character for i in self.getCurrentMap().map for j in i if j.character != None and member(j.character, MONSTER)]
                
        monster_attacks = MonsterAI.moveAI(monster_list, self.player, self.getCurrentMap())

        for i in monster_attacks:
            self.turn_messages.append(self.parseAttackMessage(i[1], i[0], self.player))

        self.processFov()
        self.generateSmell()
        self.player.step()

    def generateSmellOlder(self):
        #DEPRECATED
        self.getCurrentMap().map[self.player.x][self.player.y].smell_rating += 1000000

        buffer = [[x.smell_rating for x in y] for y in self.getCurrentMap().map]
        
        for x in range(len(self.getCurrentMap().map)):
            for y in range(x):
                if not self.getCurrentMap().opaque(x, y):
                    surrounding_tiles = Util.correctCoords(self.maps[0].height, self.maps[0].width, Util.getNeighbouringCoords((x, y), 1)) + [(x, y)]
                    
                    surrounding_tiles = filter((lambda x: self.getCurrentMap().map[x[0]][x[1]].state != Wall), surrounding_tiles)
                    surrounding_smells = [self.getCurrentMap().map[x][y].smell_rating for (x, y) in surrounding_tiles if self.getCurrentMap().map[x][y].smell_rating > 0]
                    if len(surrounding_smells) > 0:
                        avg = sum(surrounding_smells)/len(surrounding_smells)/2
                        buffer[x][y] = avg

        for x in range(len(self.getCurrentMap().map)):
            for y in range(x):
                self.getCurrentMap().map[x][y].smell_rating = buffer[x][y]
        
    def generateSmellOldest(self):
        #DEPRECATED
        for x in range(len(self.getCurrentMap().map)):
            for y in range(x):             
                if self.getCurrentMap().blocked(x, y):
                    self.getCurrentMap().map[x][y].smell_rating = 0
                else:
                    self.getCurrentMap().map[x][y].smell_rating = self.player.smell / (Util.distanceBetween(x, y, self.player.x, self.player.y) + 1)

    def generateSmellOld(self):
        #DEPRECATED
        for x in range(len(self.getCurrentMap().map)):
            for y in range(x):
                self.getCurrentMap().map[x][y].checked = False
        self.permeate((self.player.x, self.player.y), 1)
        
    def permeate(self, pos, dist):
        #DEPRECATED
        x, y = pos
        curr_map = self.getCurrentMap()
        if not curr_map.map[x][y].checked and curr_map.map[x][y].state == Floor:
            self.getCurrentMap().map[x][y].checked = True
            self.getCurrentMap().map[x][y].smell_rating = self.player.smell / dist
            neighbours = Util.correctCoords(self.maps[0].height, self.maps[0].width, Util.getNeighbouringCoords(pos, 1))

            for i in neighbours:
                self.permeate(i, dist + 1)

    def generateSmell(self):
        """makes the player generate smell so that monsters can track them"""
        for x in range(len(self.getCurrentMap().map)):
            for y in range(x):
                self.getCurrentMap().map[x][y].smell_rating /= 2
                if self.getCurrentMap().map[x][y].inFov and not self.getCurrentMap().opaque(x, y):
                    self.getCurrentMap().map[x][y].smell_rating = self.player.smell / (abs(Util.distanceBetween(x, y, self.player.x, self.player.y))+1)



    def removeFromTile(self, char):
        """removes a given character from the tile they are on"""
        self.getCurrentMap().map[char.x][char.y].character = None

    def addToTile(self, char):
        """adds a given character to the tile which they are on"""
        self.getCurrentMap().map[char.x][char.y].character = char
  
