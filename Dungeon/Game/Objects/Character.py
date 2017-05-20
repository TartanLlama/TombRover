from Object import Object
import CharacterClass
from Constants import *
from Game import Util

THREAT, HIT, MISS = range(3)

class Character(Object):
    def __init__(self, x=0, y=0, type=CHARACTER, hp=0, ac=0, damage=(0, 0), weapon=None, str_mod=0, dex_mod=0, con_mod=0, armour=None, cClass=CharacterClass.monster):
        super(Character, self).__init__(x, y, type)
        self.max_hp = hp
        self.hp = hp
        self.base_ac = ac
        self.ac = ac
        self.weapon = weapon
        self.damage = damage
        self.armour = armour
        if armour != None:
            self.ac += armour.defence

        self.str_mod = str_mod
        self.dex_mod = dex_mod
        self.con_mod = con_mod

        self.cClass = cClass
    def getDamage(self):
        extra_damage = 0
        if self.weapon != None:
            if member(self.weapon, self.cClass.damage_bonus[1]):
                extra_damage = self.cClass.damage_bonus[0]
            extra_damage += self.weapon.damage_bonus
            number, sides = self.weapon.damage
        else:
            number, sides = self.damage

        return Util.roll(number, sides) + extra_damage

    def takeDamage(self, damage):
        self.hp -= damage
        

    def attack(self, other, attack_type):
        to_hit_modifier = 0

        if self.weapon != None:
            if attack_type == MELEE and member(self.weapon, RANGED):
                to_hit_modifier = -4
                
            to_hit_modifier += self.weapon.to_hit_bonus
    
        hit = self.calculateHit(other, to_hit_modifier, attack_type)

        if hit == HIT:
            damage = self.getDamage()

        elif hit == THREAT:
            new_hit = self.calculateHit(other, to_hit_modifier, attack_type)
            if new_hit == HIT or new_hit == THREAT:
                multiplier = self.cClass.crit_multiplier

                if self.weapon != None and member(self.weapon, self.cClass.crit_bonus[1]):
                    multiplier += self.cClass.crit_bonus[0]

                damage = [self.getDamage() for i in range(multiplier)] #so that you get a different result each time
                damage = sum(damage)
            else:
                damage = self.getDamage()
        else:
            damage = 0

        other.takeDamage(damage)
        return (hit, damage)

    def calculateHit(self, other, to_hit_modifier, attack_type):
        roll = Util.roll(1, 20)
        threat_bound = 20

        if self.weapon != None and member(self.weapon, self.cClass.threat_range_bonus[1]):
                threat_bound -= self.cClass.threat_range_bonus[0]

        if roll >= threat_bound:
            return THREAT

        roll += to_hit_modifier

        if self.weapon != None:
            if attack_type == MELEE:
                roll += self.str_mod
            elif attack_type == RANGED:
                roll += self.dex_mod - Util.distanceBetween(self.x, self.y, other.x, other.y) + 1
        else:
            roll += self.str_mod
            
        

        if roll == 1:
            return MISS

        if roll >= other.ac:
            return HIT

                
        return MISS


    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        

        
