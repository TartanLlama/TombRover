from Character import Character
from Constants import *
from Game import Util
import random

MAX_OBJECTS = 2
MAX_INV_SIZE = 20
DEFAULT_SIGHT = 8
DEFAULT_SMELL = 1000
START_HP = 10
DEFAULT_HEALTH_RECOVERY = 20
next_level_calc = lambda level : 300*pow(level, 2)


class Player(Character):
    def __init__(self, cClass, x = 0, y = 0):
        super(Player, self).__init__(x, y, PLAYER, hp=START_HP, ac=0, damage=cClass.hand_damage, cClass = cClass)
        self.str, self.str_mod = self.getAttribute(self.cClass.str_res)
        self.dex, self.dex_mod = self.getAttribute(self.cClass.dex_res)
        self.con, self.con_mod = self.getAttribute(self.cClass.con_res)

        self.ac = 10 + self.dex_mod
        self.base_ac = self.ac

        self.level = 1
        
        self.xp = 0
        self.next_level = next_level_calc(self.level)
        self.previous_level = 0

        self.gold = 0
        self.inventory = {}
        self.free_symbols = [chr(i) for i in xrange(ord('a'), ord('a')+MAX_INV_SIZE)]
                
        self.max_inv = MAX_OBJECTS
        self.sight = DEFAULT_SIGHT
        self.smell = DEFAULT_SMELL

        self.health_recovery = DEFAULT_HEALTH_RECOVERY
        self.recovery_steps = 0
        
        self.effect_reverter = None
        self.effect_revert_steps = 0
        self.effect_time = None

    def step(self):
        """takes a step and calculates health recovery and potion effect reversing"""
        #recovery
        self.recovery_steps += 1
        if self.recovery_steps == self.health_recovery:
            self.recovery_steps = 0
            if self.hp < self.max_hp:
                self.hp += 1
        

        #potion effect reversing
        if self.effect_reverter != None:
            self.effect_revert_steps += 1
            
            if self.effect_revert_steps >= self.effect_time:
                self.revertEffect(self.effect_reverter)

                self.effect_reverter = None
                self.effect_time = None
                self.effect_revert_steps = 0


    def revertEffect(self, reverter):
        """reverts the effect of the last potion quaffed"""
        potion_type = reverter[0]

        if potion_type == STR_POT:
            self.strengthPotionRev(reverter[1])
        elif potion_type == DEX_POT:
            self.dexterityPotionRev(reverter[1])
        elif potion_type == INVINCIBLE_POT:
            self.ironSkinPotionRev(reverter[1])
        elif potion_type == BERSERK_POT:
            self.berserkPotionRev(reverter[1], reverter[2], reverter[3], reverter[4])
        

    def takeDamage(self, damage):
        """takes the amount of given damage and resets health regeneration"""
        super(Player, self).takeDamage(damage)
        self.recovery_steps = 0

    def wear(self, symbol):
        """puts on the armour corresponding to the given symbol"""
        new_arm = self.inventory[symbol]
        if member(new_arm, ARMOUR):
            self.takeOff()
            self.armour = new_arm
            self.ac = self.base_ac + new_arm.defence
            self.armour.equipped = True

            return new_arm.name
        
        return None

    def takeOff(self):
        """takes off all armour"""
        old_arm = self.armour
        if old_arm != None:
            self.armour = None
            self.ac = self.base_ac
            old_arm.equipped = False

            return old_arm.name

        return None

    def wield(self, symbol):
        """wields the weapon corresponding to the given symbol"""
        new_weap = self.inventory[symbol]
        if member(new_weap, WEAPON):
            self.unwield()
            self.weapon = new_weap
            self.weapon.equipped = True

            return new_weap.name
        
        return None

    def unwield(self):
        """unwields weapons"""
        old_weap = self.weapon
        if old_weap != None:
            self.weapon = None
            old_weap.equipped = False
            return old_weap.name

        return None
        
    def getInv(self):
        """returns the inventory"""
        return self.inventory

    def eat(self, symbol):
        """eats the food corresponding to the given symbol"""
        food = self.inventory[symbol]
        if member(food, FOOD):
            self.addHp(food.power)
            self.removeInv(symbol)
            return food.power

        return None

    def addHp(self, d):
        """adds the given amount of hp"""
        self.hp += d

        if self.hp > self.max_hp:
            self.hp = self.max_hp
        

    def levelUp(self):
        """advances to the next character level"""
        hit_dice_num, hit_dice_sides = self.cClass.hit_dice
        extra_points = Util.roll(hit_dice_num, hit_dice_sides) + self.con_mod * hit_dice_num
        self.hp += extra_points
        self.max_hp += extra_points
        self.previous_level = self.next_level
        self.level += 1
        self.next_level = next_level_calc(self.level)

    def getAttribute(self, restrictions):
        """randomly chooses scores for an attribute between the given restrictions"""
        a_from, a_to = restrictions

        att = random.randint(a_from, a_to)
        mod = self.getModifier(att)

        return (att, mod)

    def getModifier(self, att):
        """calculates the modifier of a given attribute"""
        return (att - 10) / 2

    def quaffPotion(self, symbol):
        """drinks the potion corresponding to the given symbol"""
        if self.effect_reverter == None:
            potion = self.inventory[symbol]
        
            if member(potion, POTION):
                reverter = self.doEffect(potion)
                if reverter != None:
                    self.effect_reverter = reverter
                    self.effect_time = potion.time * self.level


                self.removeInv(symbol)
                return True
            return False
        else:
            return None

    def doEffect(self, potion):
        """adds the effect of a given potion"""
        if member(potion, STR_POT):
            return self.strengthPotion()
        elif member(potion, DEX_POT):
            return self.dexterityPotion()
        elif member(potion, INVINCIBLE_POT):
            return self.ironSkinPotion()
        elif member(potion, KNOWLEDGE_POT):
            return self.knowledgePotion()
        elif member(potion, TELEPORT_POT):
            return self.teleportPotion()
        elif member(potion, HEALTH_POT):
            return self.healthPotion()
        elif member(potion, BERSERK_POT):
            return self.berserkPotion()

    def strengthPotion(self):
        """the effect given by drinking a strength potion"""
        str_increase = self.str/4
        self.str += str_increase
        self.str_mod = self.getModifier(self.str)
        return (STR_POT, str_increase)

    def strengthPotionRev(self, decrease):
        """the function to revert the effects of a strength potion"""
        self.str -= decrease
        self.str_mod = self.getModifier(self.str)

    def dexterityPotion(self):
        """the effect given by drinking a dexterity potion"""
        dex_increase = self.dex/4
        self.dex += dex_increase
        self.dex_mod = self.getModifier(self.dex)
        return (DEX_POT, dex_increase)

    def dexterityPotionRev(self, decrease):
        """the function to revert the effects of a strength potion"""
        self.dex -= decrease
        self.dex_mod = self.getModifier(self.dex)

    def ironSkinPotion(self):
        """the effect given by drinking an iron skin potion"""
        old_ac = self.base_ac
        self.base_ac = 50

        armour_bonus = 0
        if self.armour != None:
            armour_bonus =  self.armour.defence 
            
        self.ac = self.base_ac + armour_bonus

        return (INVINCIBLE_POT, old_ac)

    def ironSkinPotionRev(self, old_ac):
        """the function to revert the effects of an iron skin potion"""
        self.base = old_ac
        
        armour_bonus = 0
        if self.armour != None:
            armour_bonus =  self.armour.defence 

        self.ac = self.base_ac + armour_bonus

    def knowledgePotion(self):
        """the effect given by drinking a knowledge potion"""
        self.increaseXP((self.next_level - self.xp)/2)
        return (KNOWLEDGE_POT)

    def teleportPotion(self):
        pass

    def teleportPotionRev(self):
        pass

    def healthPotion(self):
        """the effect given by drinking a health potion"""
        self.hp += (self.max_hp - self.hp)/2
        return (HEALTH_POT)

    def berserkPotion(self):
        """the effect given by drinking an berserk potion"""
        old_ac = self.base_ac
        old_max_hp = self.max_hp
        old_hp = self.hp
        old_class_damage_bonus = self.cClass.damage_bonus
        self.base_ac = 0

        armour_bonus = 0
        if self.armour != None:
            armour_bonus =  self.armour.defence 
            
        self.ac = self.base_ac + armour_bonus

        self.max_hp = self.max_hp * 10
        self.hp = self.max_hp
        self.cClass.damage_bonus = (10, WEAPON)

        return (BERSERK_POT, old_ac, old_max_hp, old_hp, old_class_damage_bonus)

    def berserkPotionRev(self, old_ac, old_max_hp, old_hp, old_class_damage_bonus):
        """the function to revert the effects of a berserk potion"""
        self.base_ac = old_ac

        armour_bonus = 0
        if self.armour != None:
            armour_bonus =  self.armour.defence 
            
        self.ac = self.base_ac + armour_bonus

        self.max_hp = old_max_hp
        
        if self.hp > old_hp:
            self.hp = old_hp

        self.cClass.damage_bonus = old_class_damage_bonus
        
    def increaseXP(self, delta):
        """increases the player's xp by a given amount and checks for levelling up"""
        self.xp += delta
        if self.xp >= self.next_level:
            self.levelUp()
            return True

        return False

    def getLevel(self):
        """returns the character level"""
        return self.level
        
    def decreaseHP(self, delta):
        """decreses hp by the given amount"""
        self.hp -= delta
        
    def addInv(self, item):
        """adds the given item to the inventory"""
        if len(self.inventory) < self.max_inv:
            self.inventory[self.free_symbols.pop(0)] = item
                        
            return item.name
        else:
            return None
    
    def removeInv(self,symbol):
        
        item = self.inventory[symbol]
        self.free_symbols.insert(0, symbol)
        self.free_symbols.sort()
        del self.inventory[symbol]
        
        if item.equipped:
            item.equipped = False

            if member(item, WEAPON):
                self.weapon = None
            elif member(item, ARMOUR):
                self.armour = None

        return item
        
        
    def hasItem(self,item):
        for x in inventory:
            if x == item:
                return True
        return False

    def increaseGold(self, delta):
        self.gold += delta

    def increaseInv(self, size):
        self.max_inv += size;
        
        if self.max_inv > MAX_INV_SIZE:
            self.max_inv = MAX_INV_SIZE
