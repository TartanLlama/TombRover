from Constants import *

class CharacterClass():
    def __init__(self, name = "monster", hit_dice = (0, 0), str_res = (0, 0), dex_res = (0, 0), con_res = (0, 0), hand_damage = (0, 0), threat_range = 20,  crit_multiplier = 2, hit_bonus = (0, WEAPON), damage_bonus = (0, WEAPON), threat_range_bonus = (0, WEAPON), crit_bonus = (0, WEAPON)):
        self.name = name
        self.hit_dice = hit_dice
        self.str_res = str_res
        self.dex_res = dex_res
        self.con_res = con_res
        self.threat_range = threat_range
        self.crit_multiplier = crit_multiplier
        self.hit_bonus = hit_bonus
        self.damage_bonus = damage_bonus
        self.threat_range_bonus = threat_range_bonus
        self.crit_bonus = crit_bonus
        self.hand_damage = hand_damage

fighter = CharacterClass(name = "fighter", hit_dice = (1, 10), str_res = (10, 18), dex_res = (6, 14), con_res = (6, 16), hand_damage = (1, 6), hit_bonus = (1, MELEE)) 

ranger = CharacterClass(name = "ranger", hit_dice = (1, 8), str_res = (6, 14), dex_res = (10, 18), con_res = (6, 16), hand_damage = (1, 6), hit_bonus = (1, RANGED), damage_bonus = (1, RANGED))

thief = CharacterClass(name = "thief", hit_dice = (1, 6), str_res = (6, 16), dex_res = (8, 18), con_res = (8, 16), hand_damage = (1, 4), threat_range_bonus = (2, SHORT_SWORD), crit_bonus = (2, SHORT_SWORD))

monster = CharacterClass()
