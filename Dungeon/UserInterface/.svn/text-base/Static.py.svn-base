
import pygame
pygame.init()

from Game.Objects.Constants import *
from Game.Objects import CharacterClass

RED = (255, 0, 0, 255)
DARK_RED = (150, 0, 0, 255)
YELLOW = (255, 255, 0, 255)
DARK_YELLOW = (200, 200, 0, 255)
GOLD_COL = (255, 220, 50, 255)
ORANGE = (255, 165, 0, 255)
DARK_ORANGE = (128, 80, 0, 255)
GREEN = (0, 255, 0, 255)
DARK_GREEN = (0, 150, 0, 255)
BLUE = (0, 0, 255, 255)
LIGHT_BLUE = (90, 170, 170)
DARK_BLUE = (45, 85, 85, 255)
SOMETHING = (50, 150, 50, 255)
BEIGE = (210, 170, 100, 255)
BROWN = (139, 69, 19, 255)
DARK_BROWN = (70, 35, 10, 255)
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
GREY = (150, 150, 150, 255)
DARK_GREY = (80, 80, 80, 255)

COLOUR_KEY = (71, 108, 108)

GRID_SIZE = 32
SIDEBAR_WIDTH = 235
BORDER_SIZE = 8

MOVE_TIME = 0.15

FONT = pygame.font.SysFont("Courier New", 20, True)
TEXT_WIDTH, TEXT_HEIGHT = FONT.size("0")

SMALL_FONT = pygame.font.SysFont("Courier New", 16, True)
SMALL_TEXT_WIDTH, SMALL_TEXT_HEIGHT = SMALL_FONT.size("0")

BIG_FONT = pygame.font.SysFont("Courier New", 40, True)
BIG_TEXT_WIDTH, BIG_TEXT_HEIGHT = BIG_FONT.size("0")

ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

KEYCODE_DICT = {}
for i in xrange(26):
    KEYCODE_DICT[i + 97] = ALPHABET[i]




def loadImages():
    images = {}
    
    images["floor_visible_1"] = pygame.image.load(
        "Textures/Dungeon/floor_visible_1.bmp")
    images["floor_1"] = pygame.image.load("Textures/Dungeon/floor_1.bmp")
    images["wall_visible_1"] = pygame.image.load(
        "Textures/Dungeon/wall_visible_1.bmp")
    images["wall_1"] = pygame.image.load("Textures/Dungeon/wall_1.bmp")
    images["floor_visible_2"] = pygame.image.load(
        "Textures/Dungeon/floor_visible_2.bmp")
    images["floor_2"] = pygame.image.load("Textures/Dungeon/floor_2.bmp")
    images["wall_visible_2"] = pygame.image.load(
        "Textures/Dungeon/wall_visible_2.bmp")
    images["wall_2"] = pygame.image.load("Textures/Dungeon/wall_2.bmp")
    images["stair_down_visible"] = pygame.image.load(
        "Textures/Dungeon/stair_down_visible.bmp")
    images["stair_down"] = pygame.image.load("Textures/Dungeon/stair_down.bmp")
    images["stair_up_visible"] = pygame.image.load(
        "Textures/Dungeon/stair_up_visible.bmp")
    images["stair_up"] = pygame.image.load("Textures/Dungeon/stair_up.bmp")
    images["potion_blue"] = pygame.image.load("Textures/Objects/potion_blue.bmp")
    images["potion_cyan"] = pygame.image.load("Textures/Objects/potion_cyan.bmp")
    images["potion_green"] = pygame.image.load("Textures/Objects/potion_green.bmp")
    images["potion_pink"] = pygame.image.load("Textures/Objects/potion_pink.bmp")
    images["potion_red"] = pygame.image.load("Textures/Objects/potion_red.bmp")
    images["potion_white"] = pygame.image.load("Textures/Objects/potion_white.bmp")
    images["potion_yellow"] = pygame.image.load("Textures/Objects/potion_yellow.bmp")
    images["food"] = pygame.image.load("Textures/Objects/food.bmp")
    images["gold"] = pygame.image.load("Textures/Objects/gold.bmp")
    images["sack"] = pygame.image.load("Textures/Objects/sack.bmp")
    images["axe"] = pygame.image.load("Textures/Objects/axe.bmp")
    images["bow"] = pygame.image.load("Textures/Objects/bow.bmp")
    images["club"] = pygame.image.load("Textures/Objects/club.bmp")
    images["crossbow"] = pygame.image.load("Textures/Objects/crossbow.bmp")
    images["dagger"] = pygame.image.load("Textures/Objects/dagger.bmp")
    images["morning_star"] = pygame.image.load("Textures/Objects/morning_star.bmp")
    images["mace"] = pygame.image.load("Textures/Objects/mace.bmp")
    images["scythe"] = pygame.image.load("Textures/Objects/scythe.bmp")
    images["flail"] = pygame.image.load("Textures/Objects/flail.bmp")
    images["sword"] = pygame.image.load("Textures/Objects/sword.bmp")
    images["goblin"] = pygame.image.load("Textures/Monsters/goblin.bmp")
    images["kobold"] = pygame.image.load("Textures/Monsters/kobold.bmp")
    images["ogre"] = pygame.image.load("Textures/Monsters/ogre.bmp")
    images["orc"] = pygame.image.load("Textures/Monsters/orc.bmp")
    images["snake"] = pygame.image.load("Textures/Monsters/snake.bmp")
    images["troll"] = pygame.image.load("Textures/Monsters/troll.bmp")
    images["beetle"] = pygame.image.load("Textures/Monsters/beetle.bmp")
    images["clay_golem"] = pygame.image.load("Textures/Monsters/clay_golem.bmp")
    images["drake"] = pygame.image.load("Textures/Monsters/drake.bmp")
    images["frog"] = pygame.image.load("Textures/Monsters/frog.bmp")
    images["gecko"] = pygame.image.load("Textures/Monsters/gecko.bmp")
    images["gnoll"] = pygame.image.load("Textures/Monsters/gnoll.bmp")
    images["hobgoblin"] = pygame.image.load("Textures/Monsters/hobgoblin.bmp")
    images["jackal"] = pygame.image.load("Textures/Monsters/jackal.bmp")
    images["jelly"] = pygame.image.load("Textures/Monsters/jelly.bmp")
    images["komodo_dragon"] = pygame.image.load("Textures/Monsters/komodo_dragon.bmp")
    images["naga"] = pygame.image.load("Textures/Monsters/naga.bmp")
    images["rat"] = pygame.image.load("Textures/Monsters/rat.bmp")
    images["skeleton"] = pygame.image.load("Textures/Monsters/skeleton.bmp")
    images["warg"] = pygame.image.load("Textures/Monsters/warg.bmp")
    images["wolf"] = pygame.image.load("Textures/Monsters/wolf.bmp")
    images["giant_zombie"] = pygame.image.load("Textures/Monsters/giant_zombie.bmp")
    images["griffon"] = pygame.image.load("Textures/Monsters/griffon.bmp")
    images["minotaur"] = pygame.image.load("Textures/Monsters/minotaur.bmp")
    images["manticore"] = pygame.image.load("Textures/Monsters/manticore.bmp")
    images["iron_golem"] = pygame.image.load("Textures/Monsters/iron_golem.bmp")
    images["soldier_ant"] = pygame.image.load("Textures/Monsters/soldier_ant.bmp")
    images["banded_mail"] = pygame.image.load("Textures/Objects/banded_mail.bmp")
    images["chain_mail"] = pygame.image.load("Textures/Objects/chain_mail.bmp")
    images["leather_armor"] = pygame.image.load("Textures/Objects/leather_armor.bmp")
    images["half_plate"] = pygame.image.load("Textures/Objects/half_plate.bmp")
    images["padded_armor"] = pygame.image.load("Textures/Objects/padded_armor.bmp")
    images["plate_mail"] = pygame.image.load("Textures/Objects/plate_mail.bmp")
    images["scale_mail"] = pygame.image.load("Textures/Objects/scale_mail.bmp")
    images["studded_leather"] = pygame.image.load("Textures/Objects/studded_leather.bmp")

    for key in images:
        if key != "floor_visible" and key != "floor" \
           and key != "wall_visible" and key != "wall":
            images[key].set_colorkey(COLOUR_KEY)
    
    return images


class PlayerGenerator():
    
    def __init__(self):
        images = {}
        images["shadow"] = pygame.image.load("Textures/Player/shadow.bmp")
        images["body"] = pygame.image.load("Textures/Player/body.bmp")
        images["cloak"] = pygame.image.load("Textures/Player/cloak.bmp")
        images["gloves"] = pygame.image.load("Textures/Player/gloves.bmp")
        images["trousers_green"] = pygame.image.load("Textures/Player/trousers_green.bmp")
        images["trousers_black"] = pygame.image.load("Textures/Player/trousers_black.bmp")
        
        images["fighter_top"] = pygame.image.load("Textures/Player/fighter_top.bmp")
        images["fighter_hair"] = pygame.image.load("Textures/Player/fighter_hair.bmp")
        images["fighter_shoes"] = pygame.image.load("Textures/Player/fighter_shoes.bmp")
        
        images["thief_top"] = pygame.image.load("Textures/Player/thief_top.bmp")
        images["thief_hair"] = pygame.image.load("Textures/Player/thief_hair.bmp")
        images["thief_shoes"] = pygame.image.load("Textures/Player/thief_shoes.bmp")
        
        images["ranger_top"] = pygame.image.load("Textures/Player/ranger_top.bmp")
        images["ranger_hair"] = pygame.image.load("Textures/Player/ranger_hair.bmp")
        images["ranger_shoes"] = pygame.image.load("Textures/Player/ranger_shoes.bmp")
        
        images["axe_great"] = pygame.image.load("Textures/Player/axe_great.bmp")
        images["axe_battle"] = pygame.image.load("Textures/Player/axe_battle.bmp")
        images["bow_short"] = pygame.image.load("Textures/Player/bow_short.bmp")
        images["bow_long"] = pygame.image.load("Textures/Player/bow_long.bmp")
        images["club"] = pygame.image.load("Textures/Player/club.bmp")
        images["crossbow_light"] = pygame.image.load("Textures/Player/crossbow_light.bmp")
        images["crossbow_heavy"] = pygame.image.load("Textures/Player/crossbow_heavy.bmp")
        images["dagger"] = pygame.image.load("Textures/Player/dagger.bmp")
        images["flail"] = pygame.image.load("Textures/Player/flail.bmp")
        images["mace"] = pygame.image.load("Textures/Player/mace.bmp")
        images["morning_star"] = pygame.image.load("Textures/Player/morning_star.bmp")
        images["scythe"] = pygame.image.load("Textures/Player/scythe.bmp")
        images["sword_short"] = pygame.image.load("Textures/Player/sword_short.bmp")
        images["sword_long"] = pygame.image.load("Textures/Player/sword_long.bmp")
        images["sword_bastard"] = pygame.image.load("Textures/Player/sword_bastard.bmp")
        images["sword_great"] = pygame.image.load("Textures/Player/sword_great.bmp")
        
        images["banded_top"] = pygame.image.load("Textures/Player/banded_top.bmp")
        images["chain_top"] = pygame.image.load("Textures/Player/chain_top.bmp")
        images["full_plate_top"] = pygame.image.load("Textures/Player/full_plate_top.bmp")
        images["half_plate_top"] = pygame.image.load("Textures/Player/half_plate_top.bmp")
        images["leather_top"] = pygame.image.load("Textures/Player/leather_top.bmp")
        images["padded_top"] = pygame.image.load("Textures/Player/padded_top.bmp")
        images["plate_bottom"] = pygame.image.load("Textures/Player/plate_bottom.bmp")
        images["scale_top"] = pygame.image.load("Textures/Player/scale_top.bmp")
        images["studded_bottom"] = pygame.image.load("Textures/Player/studded_bottom.bmp")
        images["studded_top"] = pygame.image.load("Textures/Player/studded_top.bmp")
        
        for key in images:
            images[key].set_colorkey(COLOUR_KEY)
        
        self.images = images
    
    def getPlayerImage(self, player, size):
        
        char_class = player.cClass
        weapon = player.weapon
        armour = player.armour
        
        if char_class.name == CharacterClass.fighter.name:
            cloak  = ""
            top    = "fighter_top"
            bottom = "trousers_green"
            hair   = "fighter_hair"
            shoes  = "fighter_shoes"
        elif char_class.name == CharacterClass.ranger.name:
            cloak  = ""
            top    = "ranger_top"
            bottom = "trousers_green"
            hair   = "ranger_hair"
            shoes  = "ranger_shoes"
        elif char_class.name == CharacterClass.thief.name:
            cloak  = "cloak"
            top    = "thief_top"
            bottom = "trousers_black"
            hair   = "thief_hair"
            shoes  = "thief_shoes"
        
        if weapon != None and member(weapon, MELEE):
            if member(weapon, AXE):
                if member(weapon, GREAT_AXE):
                    weapon = "axe_great"
                else:
                    weapon = "axe_battle"
            elif member(weapon, CLUB):
                weapon = "club"
            elif member(weapon, MACE):
                if member(weapon, MORNING_STAR):
                    weapon = "morning_star"
                else:
                    weapon = "mace"
            elif member(weapon, FLAIL):
                weapon = "flail"
            elif member(weapon, SCYTHE):
                weapon = "scythe"
            elif member(weapon, DAGGER):
                weapon = "dagger"
            elif member(weapon, SWORD):
                if member(weapon, SHORT_SWORD):
                    weapon = "sword_short"
                elif member(weapon, BASTARD_SWORD):
                    weapon = "sword_bastard"
                elif member(weapon, GREAT_SWORD):
                    weapon = "sword_great"
                else:
                    weapon = "sword_long"
        elif weapon != None and member(weapon, RANGED):
            if member(weapon, CROSSBOW):
                if member(weapon, HEAVY_CROSSBOW):
                    weapon = "crossbow_heavy"
                else:
                    weapon = "crossbow_light"
            elif member(weapon, BOW):
                if member(weapon, LONG_BOW):
                    weapon = "bow_long"
                else:
                    weapon = "bow_short"
        else:
            weapon = ""
        
        if armour != None and member(armour, PADDED):
            top = "padded_top"
        elif armour != None and member(armour, LEATHER):
            if member(armour, STUDDED_LEATHER):
                top = "studded_top"
                bottom = "studded_bottom"
            else:
                top = "leather_top"
        elif armour != None and member(armour, SCALE):
            top = "scale_top"
        elif armour != None and member(armour, CHAIN):
            top = "chain_top"
        elif armour != None and member(armour, BANDED):
            top = "banded_top"
            bottom = "plate_bottom"
        elif armour != None and member(armour, PLATE):
            if member(armour, FULL_PLATE):
                top = "full_plate_top"
                bottom = "plate_bottom"
            else:
                top = "half_plate_top"
                bottom = "plate_bottom"
        
        return self.compilePlayerImage(size, cloak, shoes, bottom, top, hair,
                                       weapon)
    
    def compilePlayerImage(self, size, cloak="", shoes="", trousers="", top="",
                           hair="", weapon=""):
        keys = ["shadow", cloak, "body", shoes, "gloves", trousers, top, hair,
                weapon]
        base = pygame.Surface(size)
        base.fill(COLOUR_KEY)
        for key in keys:
            if key in self.images:
                img = self.images[key]
                img = pygame.transform.scale(img, size)
                base.blit(img, (0, 0))
        base.set_colorkey(COLOUR_KEY)
        return base


def getImageString(obj_type, visible=True):
    if member(obj_type, MONSTER):
        if member(obj_type, BEETLE):
            return "beetle"
        elif member(obj_type, CLAY_GOLEM):
            return "clay_golem"
        elif member(obj_type, DRAKE):
            return "drake"
        elif member(obj_type, FROG):
            return "frog"
        elif member(obj_type, GECKO):
            return "gecko"
        elif member(obj_type, GNOLL):
            return "gnoll"
        elif member(obj_type, GOBLIN):
            return "goblin"
        elif member(obj_type, HOBGOBLIN):
            return "hobgoblin"
        elif member(obj_type, JACKAL):
            return "jackal"
        elif member(obj_type, JELLY):
            return "jelly"
        elif member(obj_type, KOBOLD):
            return "kobold"
        elif member(obj_type, KOMODO_DRAGON):
            return "komodo_dragon"
        elif member(obj_type, NAGA):
            return "naga"
        elif member(obj_type, OGRE):
            return "ogre"
        elif member(obj_type, ORC):
            return "orc"
        elif member(obj_type, RAT):
            return "rat"
        elif member(obj_type, SKELETON):
            return "skeleton"
        elif member(obj_type, SNAKE):
            return "snake"
        elif member(obj_type, SOLDIER_ANT):
            return "soldier_ant"
        elif member(obj_type, WARG):
            return "warg"
        elif member(obj_type, WOLF):
            return "wolf"
        elif member(obj_type, GIANT_ZOMBIE):
            return "giant_zombie"
        elif member(obj_type, GRIFFON):
            return "griffon"
        elif member(obj_type, MINOTAUR):
            return "minotaur"
        elif member(obj_type, MANTICORE):
            return "manticore"
        elif member(obj_type, IRON_GOLEM):
            return "iron_golem"
        elif member(obj_type, TROLL):
            return "troll"
    elif member(obj_type, STAIRS):
        if visible:
            if member(obj_type, UP):
                return "stair_up_visible"
            else:
                return "stair_down_visible"
        else:
            if member(obj_type, UP):
                return "stair_up"
            else:
                return "stair_down"
    elif member(obj_type, ITEM):
        if member(obj_type, POTION):
            if member(obj_type, STR_POT):
                return "potion_yellow"
            elif member(obj_type, INVINCIBLE_POT):
                return "potion_pink"
            elif member(obj_type, TELEPORT_POT):
                return "potion_white"
            elif member(obj_type, KNOWLEDGE_POT):
                return "potion_cyan"
            elif member(obj_type, HEALTH_POT):
                return "potion_green"
            elif member(obj_type, BERSERK_POT):
                return "potion_red"
            else:
                return "potion_blue"
        elif member(obj_type, ARMOUR):
            if member(obj_type, PADDED):
                return "padded_armor"
            elif member(obj_type, LEATHER):
                if member(obj_type, STUDDED_LEATHER):
                    return "studded_leather"
                else:
                    return "leather_armor"
            elif member(obj_type, SCALE):
                return "scale_mail"
            elif member(obj_type, CHAIN):
                return "chain_mail"
            elif member(obj_type, BANDED):
                return "banded_mail"
            elif member(obj_type, PLATE):
                if member(obj_type, HALF_PLATE):
                    return "half_plate"
                else:
                    return "plate_mail"
        elif member(obj_type, WEAPON):
            if member(obj_type, MELEE):
                if member(obj_type, SWORD):
                    return "sword"
                elif member(obj_type, AXE):
                    return "axe"
                elif member(obj_type, CLUB):
                    return "club"
                elif member(obj_type, DAGGER):
                    return "dagger"
                elif member(obj_type, MORNING_STAR):
                    return "morning_star"
                elif member(obj_type, MACE):
                    return "mace"
                elif member(obj_type, SCYTHE):
                    return "scythe"
                elif member(obj_type, FLAIL):
                    return "flail"
            elif member(obj_type, RANGED):
                if member(obj_type, BOW):
                    return "bow"
                elif member(obj_type, CROSSBOW):
                    return "crossbow"
        elif member(obj_type, SCROLL):
            return "scroll"
        elif member(obj_type, GOLD):
            return "gold"
        elif member(obj_type, FOOD):
            return "food"
        elif member(obj_type, SACK):
            return "sack"
    return None
