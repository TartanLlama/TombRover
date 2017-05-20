from Character import Character
from Constants import *
from Game import Util
import random
import copy

HIT_DICE, DAMAGE, AC_BONUS, TYPE, NAME, MORALE = range(6)
class Monster(Character):
    def __init__(self, mons, power, x=0, y=0):
        super(Monster, self).__init__(x, y, mons[TYPE], damage=mons[DAMAGE])
        self.level = power
        hit_dice_num, hit_dice_sides = mons[HIT_DICE]
        self.hp = Util.roll(hit_dice_num, hit_dice_sides)
        self.max_hp = self.hp
        self.ac = 10 + mons[AC_BONUS]
        self.name = mons[NAME]
        self.moraleFailureHp = mons[MORALE]
        
    def getName(self):
        return self.name
    
    def getHP(self):
        return self.hp
     
    def hasMorale(self):
        if self.hp*1.0/self.max_hp*100 < self.moraleFailureHp:
	        return False
        return True

def createMonster(max_power, current_map):
    power = random.randint(0, min(max_power, len(monsters)-1, (current_map+1)/2))
    poss_monsters = monsters[power]
    return Monster(poss_monsters[random.randint(0, len(poss_monsters)-1)], power+1)

monsters = [[{NAME:'goblin', HIT_DICE:(1, 4), DAMAGE:(1, 4), AC_BONUS:0, TYPE:GOBLIN, MORALE:25},
             {NAME:'rat', HIT_DICE:(1, 2), DAMAGE:(1, 2), AC_BONUS:-2, TYPE:RAT, MORALE:0},
             {NAME:'gecko', HIT_DICE:(1, 4), DAMAGE:(1, 3), AC_BONUS:-2, TYPE:GECKO, MORALE:10},
             {NAME:'kobold', HIT_DICE:(1, 4), DAMAGE:(1, 3), AC_BONUS:-2, TYPE:KOBOLD, MORALE:50},
             {NAME:'jackal', HIT_DICE:(1, 4), DAMAGE:(1, 3), AC_BONUS:0, TYPE:JACKAL, MORALE:0}],


            [{NAME:'orc', HIT_DICE:(2, 4), DAMAGE:(1, 4), AC_BONUS:1, TYPE:ORC, MORALE:10},
             {NAME:'jelly', HIT_DICE:(3, 2), DAMAGE:(1, 3), AC_BONUS:0, TYPE:JELLY, MORALE:0},
             {NAME:'soldier ant', HIT_DICE:(3, 2), DAMAGE:(1, 4), AC_BONUS:0, TYPE:SOLDIER_ANT, MORALE:0},
             {NAME:'giant frog', HIT_DICE:(2, 8), DAMAGE:(1, 1), AC_BONUS:-1, TYPE:FROG, MORALE:0}],


            [{NAME:'giant snake', HIT_DICE:(3, 6), DAMAGE:(1, 4), AC_BONUS:-1, TYPE:SNAKE, MORALE:20},
             {NAME:'wolf', HIT_DICE:(3, 6), DAMAGE:(1, 4), AC_BONUS:-1, TYPE:WOLF, MORALE:20},
             {NAME:'skeleton', HIT_DICE:(5, 4), DAMAGE:(1, 4), AC_BONUS:1, TYPE:SKELETON, MORALE:30},
             {NAME:'hobgoblin', HIT_DICE:(3, 6), DAMAGE:(1, 4), AC_BONUS:1, TYPE:HOBGOBLIN, MORALE:20}],


            [{NAME:'warg', HIT_DICE:(2, 10), DAMAGE:(1, 6), AC_BONUS:2, TYPE:WARG, MORALE:20},
             {NAME:'giant beetle', HIT_DICE:(2, 6), DAMAGE:(1, 4), AC_BONUS:4, TYPE:BEETLE, MORALE:0},
             {NAME:'komodo dragon', HIT_DICE:(2, 8), DAMAGE:(1, 6), AC_BONUS:1, TYPE:KOMODO_DRAGON, MORALE:10},
             {NAME:'gnoll', HIT_DICE:(5, 4), DAMAGE:(2, 3), AC_BONUS:2, TYPE:GNOLL, MORALE:20}],

            
            [{NAME:'drake', HIT_DICE:(2, 6), DAMAGE:(1, 8), AC_BONUS:1, TYPE:DRAKE, MORALE:40},
             {NAME:'naga', HIT_DICE:(3, 6), DAMAGE:(2, 4), AC_BONUS:-1, TYPE:NAGA, MORALE:10},
             {NAME:'ogre', HIT_DICE:(4, 6), DAMAGE:(2, 6), AC_BONUS:0, TYPE:OGRE, MORALE:0},
             {NAME:'clay golem', HIT_DICE:(4, 5), DAMAGE:(2, 4), AC_BONUS:3, TYPE:CLAY_GOLEM, MORALE:0}],


            [{NAME:'giant zombie', HIT_DICE:(6, 6), DAMAGE:(2, 5), AC_BONUS:0, TYPE:GIANT_ZOMBIE, MORALE:0},
             {NAME:'griffon', HIT_DICE:(4, 8), DAMAGE:(4, 3), AC_BONUS:-1, TYPE:GRIFFON, MORALE:50},
             {NAME:'minotaur', HIT_DICE:(5, 12), DAMAGE:(2, 6), AC_BONUS:0, TYPE:MINOTAUR, MORALE:10}],
            
            
            [{NAME:'manticore', HIT_DICE:(5, 8), DAMAGE:(6, 3), AC_BONUS:0, TYPE:MANTICORE, MORALE:5},
             {NAME:'iron golem', HIT_DICE:(6, 5), DAMAGE:(2, 4), AC_BONUS:5, TYPE:IRON_GOLEM, MORALE:0},
             {NAME:'troll', HIT_DICE:(10, 4), DAMAGE:(2, 10), AC_BONUS:2, TYPE:TROLL, MORALE:0}]]
            

            
   
        
