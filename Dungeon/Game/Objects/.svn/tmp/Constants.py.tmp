ITEM = [0]
CHARACTER = [1]
STAIRS = [3]


#Item{
POTION = [ITEM, 0]
WEAPON = [ITEM, 1]
SCROLL = [ITEM, 2]
GOLD = [ITEM, 3]
FOOD = [ITEM, 4]
ARMOUR = [ITEM, 5]
SACK = [ITEM, 6]

#Potion{
STR_POT = [POTION, 0]
DEX_POT = [POTION, 1]
INVINCIBLE_POT = [POTION, 2]
KNOWLEDGE_POT = [POTION, 3]
TELEPORT_POT = [POTION, 4]
HEALTH_POT = [POTION, 5]
BERSERK_POT = [POTION, 6]

#Weapon{
MELEE = [WEAPON, 0]
RANGED = [WEAPON, 1]

#Melee{
SWORD = [MELEE, 0]
AXE = [MELEE, 1]
CLUB = [MELEE, 2]
MACE = [MELEE, 3]
FLAIL = [MELEE, 4]
SCYTHE = [MELEE, 5]
DAGGER = [MELEE, 7]

#Sword{
SHORT_SWORD = [SWORD, 0]
LONG_SWORD = [SWORD, 1]
BASTARD_SWORD = [SWORD, 2]
GREAT_SWORD = [SWORD, 3]
#}Sword

#Axe{
BATTLE_AXE = [AXE, 0]
GREAT_AXE = [AXE, 1]
#}Axe

#Mace{
MORNING_STAR = [MACE, 0]
#}Mace
#}Melee

#Ranged{
BOW = [RANGED, 0]
CROSSBOW = [RANGED, 1]

#Bow{
SHORT_BOW = [BOW, 0]
LONG_BOW = [BOW, 1]
#}

#Crossbow{
LIGHT_CROSSBOW = [CROSSBOW, 0]
HEAVY_CROSSBOW = [CROSSBOW, 1]
#}Ranged
#}Weapons

#Armour{
PADDED = [ARMOUR, 0]
LEATHER = [ARMOUR, 1]
SCALE = [ARMOUR, 2]
CHAIN = [ARMOUR, 3]
BANDED = [ARMOUR, 4]
PLATE = [ARMOUR, 5]
#}Armour

#Leather{
STUDDED_LEATHER = [LEATHER, 0]
#}Leather

#Plate{
HALF_PLATE = [PLATE, 0]
FULL_PLATE = [PLATE, 1]
#}Plate
#}Item

#Character{
MONSTER = [CHARACTER, 0]
PLAYER = [CHARACTER, 1]

#Monster{
GOBLIN = [MONSTER, 0]
RAT = [MONSTER, 1]
GECKO = [MONSTER, 2]
KOBOLD = [MONSTER, 3]
JACKAL = [MONSTER, 4]
ORC = [MONSTER, 5]
JELLY = [MONSTER, 6]
SOLDIER_ANT = [MONSTER, 7]
FROG = [MONSTER, 8]
SNAKE = [MONSTER, 9]
WOLF = [MONSTER, 10]
SKELETON = [MONSTER, 11]
HOBGOBLIN = [MONSTER, 12]
WARG = [MONSTER, 13]
BEETLE = [MONSTER, 14]
KOMODO_DRAGON = [MONSTER, 15]
GNOLL = [MONSTER, 16]
DRAKE = [MONSTER, 17]
NAGA = [MONSTER, 18]
OGRE = [MONSTER, 19]
CLAY_GOLEM = [MONSTER, 20]
GIANT_ZOMBIE = [MONSTER, 21]
GRIFFON = [MONSTER, 22]
MINOTAUR = [MONSTER, 23]
MANTICORE = [MONSTER, 24]
IRON_GOLEM = [MONSTER, 25]
TROLL = [MONSTER, 26]

#}Monster
#}Character

#Stairs{
UP = [STAIRS, 0]
DOWN = [STAIRS, 1]
#}Stairs


def member(item, ty):
    """returns True if the given object is a member or submember of a given type"""
    return checkMember(item.type, ty)

def checkMember(ty1, ty2):
    if ty2 in ty1 or ty2 == ty1:
        return True
    elif len(ty1) == 1:
        return False
    else:
        return checkMember(ty1[0], ty2)
    
