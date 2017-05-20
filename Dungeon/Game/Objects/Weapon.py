import random
from Item import Item
from Constants import *

NAME, TYPE, DAMAGE, HANDS = range(4)

class Weapon(Item):
    def __init__(self, weap, x=0, y=0, to_hit_bonus=0, damage_bonus=0):
        super(Weapon, self).__init__(x, y, type=weap[TYPE], name=weap[NAME])
        self.damage = weap[DAMAGE]
        self.hands = weap[HANDS]
        self.to_hit_bonus = to_hit_bonus
        self.damage_bonus = damage_bonus

        if self.damage_bonus > 0:
            self.name += '+' + str(self.to_hit_bonus) + '/+' + str(self.damage_bonus)
        elif self.to_hit_bonus > 0:
            self.name += '+' + str(self.to_hit_bonus)

def createWeapon(player_level):
    highest_level = player_level/2

    weapon_level = random.randint(0, min(highest_level, len(weapons)-1))

    to_hit_bonus = random.randint(0, player_level/4)
    damage_bonus = random.randint(0, player_level/4)

    poss_weapons = weapons[weapon_level]
    weap = poss_weapons[random.randint(0, len(poss_weapons)-1)]
    return Weapon(weap, to_hit_bonus=to_hit_bonus, damage_bonus=damage_bonus)

weapons = [[{NAME:'Dagger', TYPE:DAGGER, DAMAGE:(1, 4), HANDS:1}],

           [{NAME:'Short sword', TYPE:SHORT_SWORD, DAMAGE:(1, 6), HANDS:1},
            {NAME:'Club', TYPE:CLUB, DAMAGE:(1, 6), HANDS:1},
            {NAME:'Short bow', TYPE:SHORT_BOW, DAMAGE:(1, 6), HANDS:2}],

           [{NAME:'L. crossbow', TYPE:LIGHT_CROSSBOW, DAMAGE:(1, 8), HANDS:2},
            {NAME:'Mace', TYPE:MACE, DAMAGE:(1, 8), HANDS:1},
            {NAME:'Morning star', TYPE:MORNING_STAR, DAMAGE:(1, 8), HANDS:1},
            {NAME:'Battle axe', TYPE:BATTLE_AXE, DAMAGE:(1, 8), HANDS:1},
            {NAME:'Longsword', TYPE:LONG_SWORD, DAMAGE:(1, 8), HANDS:1},
            {NAME:'Longbow', TYPE:LONG_BOW, DAMAGE:(1, 8), HANDS:2},
            {NAME:'Scythe', TYPE:SCYTHE, DAMAGE:(2, 4), HANDS:2}],
           
           [{NAME:'Flail', TYPE:FLAIL, DAMAGE:(1, 10), HANDS:2},
            {NAME:'Bastard sword', TYPE:BASTARD_SWORD, DAMAGE:(1, 10), HANDS:1},
            {NAME:'H. crossbow', TYPE:HEAVY_CROSSBOW, DAMAGE:(1, 10), HANDS:2}],

           [{NAME:'Great axe', TYPE:GREAT_AXE, DAMAGE:(1, 12), HANDS:2}],
           
           [{NAME:'Great sword', TYPE:GREAT_SWORD, DAMAGE:(2, 12), HANDS:2}]]
           
           
           

           
