import random
import time
import os
## This program is going to be a game. PC will pick between 3 classes: Warrior, Ranger, and Mage.
class Enemy:
    def __init__(self, name):
        self.name = name
        self.description = "undef"
        self.health = -1
        self.damageRange = []
        self.percentChanceCritical = -1
    
class Goblin(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.description = "An ugly little goblin. His little head is ripe for blugeoning."
        self.damageDescriptions =["He swings his sword at you.", "He stabs his sword at you.", "He tries to bite you.", "He tries to bonk your head."]
        self.health = 5
        self.damageRange = [1, 2]
        self.percentChanceCritical = 0

class Troll(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.description = "An lanky, stanky troll. He's got a wide maw, and he looks hungry!"
        self.damageDescriptions = ["He swings his club at you.", "He goes for a big chomp", "He wafts his putrid scent at you.", "He throws a big rock at you."]
        self.health = 12
        self.damageRange = [3, 4]
        self.percentChanceCritical = 0

class Ogre(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.description = "An big old ogre. He might be nice, but there aren't any donkeys or onions to be seen..."
        self.damageDescriptions = ["He tries to smash you with his fist.", "He goes for a big kick.", "He hucks a bag of onions at you.", "He throws a donkey carcass at you."]
        self.health = 18
        self.damageRange = [4, 5]
        self.percentChanceCritical = 0

class Witch(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.description = "A cruel green witch. She cackles while picking her nose with her wand."
        self.damageDescriptions = ["She casts a cruel hex on you.", "She summons evil faries to attack you.", "She flies her broom into you at full speed.", "She casts a mean spell on you."]
        self.damageRange = [1, 3, 5]
        self.percentChanceCritical = 0

class PC:
    def __init__(self, name):
        self.name = name
        self.occupation = "undef"
        self.health = -1
        self.maxHealth = -1
        self.damageRange = []
        self.percentChanceCritical = -1

        self.strength = -1
        self.dexterity = -1
        self.intelligence = -1

        def examine(self : PC, enemy.description : str):

        def doDamage(self : PC, damageRange : list):
            random_index = random.randint(0, len(damageRange) - 1)
            damage = random.randint(self.damageRange[0], self.damageRange[damageRange.length - 1])
            if random.randint(1, 100) <= self.percentChanceCritical:
                damage = damage * 2
            
            return damage

class Warrior(PC):
    def __init__(self, name):
        super().__init__(name)
        self.occupation = "Warrior"
        self.health = 18
        self.maxHealth = 18
        self.damageRange = [1, 2, 3, 4, 5, 6, 7, 8]
        self.percentChanceCritical = 5

        self.strength = 15
        self.dexterity = 10
        self.intelligence = 5

        self.rallyCount = 5
        self.rallyCountMax = 5

        def RallyUp(self : Warrior):
            if self.health < self.maxHealth:
                self.health = (self.maxHealth / 2) + self.health
                if self.health > self.maxHealth:
                    self.health = self.maxHealth
        


class Mage(PC):
    def __init__(self, name):
        super().__init__(name)
        self.occupation = "Mage"
        self.health = 12
        self.maxHealth = 12
        self.damageRange = [0, 0, 3, 4, 5, 10]
        self.percentChanceCritical = 5
        
        self.strength = 5
        self.dexterity = 10
        self.intelligence = 15

        self.manaCount = 10
        self.manaMax = 10

        def castFireball(self : Mage, enemyWeakness : str)
            if enemyWeakness == "fire":
                damage = self.doDamage(self.damageRange) * 1.5
            else:
                damage = self.doDamage(self.damageRange)
            manaCount = self.manaCount - 1

            return damage
            

        
class Ranger(PC):
    def __init__(self, name):
        super().__init__(name)
        self.occupation = "Ranger"
        self.health = 15
        self.maxHealth = 15
        self.damageRange = [3, 4, 5]
        self.percentChanceCritical = 15

        self.strength = 10
        self.dexterity = 15
        self.intelligence = 5

        self.focusCount = 5
        self.focusCountMax = 5

        def FocusUp(self : Ranger):
            if self.health < self.maxHealth:
                self.health = (self.maxHealth / 2) + self.health
                if self.health > self.maxHealth:
                    self.health = self.maxHealth




## In this program, the user will create a character represented by class type PC and fight an NPC.

name = input("What is your name? ")
while True:
    occupation = input("What class would you like to be? Warrior, Mage, or Ranger? ")
    if occupation == "Warrior":
        print("You are a Warrior!")
        user = Warrior(name) 
        break
    elif occupation == "Mage":
        print("You are a Mage!")
        user = Mage(name) 
        break
    elif occupation == "Ranger":
        print("You are a Ranger!")
        user = Ranger(name) 
        break
    else:
        print("That is not a valid class.")
 

enemy1 = Goblin()

os.system('cls')

print(f"An evil creature blocks your path. It's a {enemy1.name}!")




        
    

