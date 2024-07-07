## This program is a dungeon exploration game. The user wins by reaching the end of the dungeon.
#### The user will move through rooms and encounter enemies to fight.
#### The user will lose and the game will restart if the user runs out of health.

## IMPORTS ##

# Random is used to generate random numbers. These will be used to generate random damage values, critical hits, and random encounters.
import random

# OS is used to control the terminal. It is used to clear the terminal and print text.
import os

# Time is used to control the speed of the game. It is used to slow down the displayed output of the terminal.
import time

DAMAGE_DICT = {"1d4" : [1, 2, 3 , 4],
               "1d6" : [1, 2, 3, 4, 5, 6],
               "1d8" : [1, 2, 3, 4, 5, 6, 7, 8],
               "1d10" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
## CLASSES ##


     # User #
    ## Enemy ##
  #### Room ####
###### Game ######

##### CLASS DEFINITIONS #####

## User ##
class User:
# The User class represents the user in the dungeon.
    def __init__(self, name = "undef", player_class = "undef", health = -1, max_health = -1, defense = -1, attack_dice = "undef", dodge_chance = -1, strength = -1, dexterity = -1, intelligence = -1, critical_hit_chance = -1, mana = -1, max_mana = -1, special = "undef", inventory = []):
# An object of this class has the following attributes:
    # a name (name : string)
        self.name = name
    # a class name (class : string)
        self.player_class = player_class
    # a health stat(health : int)
        self.health = health
    # a max health stat(max_health : int)
        self.max_health = max_health
    # a defense stat (defense : int)
        self.defense = defense
    # an attack dice (attack_dice : str)
        self.attack_dice = attack_dice
    # a percent chance to dodge (dodge_chance : int)
        self.dodge_chance = dodge_chance
    # a strength stat (strength : int)
        self.strength = strength
    # a dexterity stat (dexterity : int)
        self.dexterity = dexterity
    # a intelligence stat (intelligence : int)
        self.intelligence = intelligence
    # a percent chance of critical hit (critical_hit_chance : int)
        self.critical_hit_chance = critical_hit_chance = -1
    # a mana stat (mana : int)
        self.mana = mana
    # a max mana stat (max_mana : int)
        self.max_mana = max_mana
    # a special attack (special : str)
        self.special = special
    # a list of items (inventory : list)
        self.inventory = inventory

    def getDamage(self) -> int:
        return random.choice(DAMAGE_DICT[self.attack_dice])

    def displayStats(self) -> None:
        print(f"{self.name} --- {self.player_class}\n\nHP: {self.health}/{self.max_health}\nSTR: {self.strength}  DEX: {self.dexterity}  INT: {self.intelligence}")
    def displayInventory(self) -> None:
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print(f"Inventory: - {', '.join(self.inventory)}")

    def useItem(self, item_name : str) -> None:
        if item_name == "health potion":
            self.health += 10
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"\nHealth potion restored you to {self.health}/{self.max_health}.")
        elif item_name == "mana potion":
            self.mana += 5
            if self.mana > self.max_mana:
                self.mana = self.max_mana
            print(f"\nMana potion restored you to {self.mana}/{self.max_mana}.")
        elif item_name == "health elixir":
            self.max_health += 5
            self.health = self.max_health
            print(f"\nHealth elixir increased your max health to {self.max_health}!")
        elif item_name == "lucky charm":
            self.dodge_chance += 10
            print(f"\nLucky charm increased your dodge chance by 10%!")
        elif item_name == "defense enchanted pendant":
            self.defense += 1
            print(f"\nDefense enchanted pendant increased your defense by 1!")

        time.sleep(2)
        

## Enemy ##
class Enemy:
# The Enemy class represents an enemy in the dungeon.
    def __init__(self, name = "undef", health = -1, defense = -1, attack_dice = "undef", dodge_chance = -1, description = "undef", vulnerabilities = [], damage = -1, barks = [], damageDescriptions = []):
# An object of this class has the following attributes:
# a name (name : string)
        self.name = name
    # a health stat(health : int)
        self.health = health
    # a defense stat (defense : int)
        self.defense = defense
    # an attack dice (attack_dice : str)
        self.attack_dice = attack_dice
    # a percent chance to dodge (dodge_chance : int)
        self.dodge_chance = dodge_chance
    # a description (description : string)
        self.description = description
    # a list of vulnerabilities (vulnerabilities : list)
        self.vulnerabilities = vulnerabilities
    # a damage value (damage : int)
        self.damage = damage
    # a list of barks (barks : list)
        self.barks = barks
    # a list of damage descriptions (damageDescriptions : list)
        self.damageDescriptions = damageDescriptions

    def getDamage(self) -> int:
        return random.choice(DAMAGE_DICT[self.attack_dice])

## Room ##
class Room:
# The Room class represents rooms in a dungeon.
# The class has the following attributes:
    # the number of rooms generated (number_of_rooms : int)
    number_of_rooms = 0
    # this number will incremented each time a Room object is created.

    
    enemy_1a = Enemy("Goblin", 10, 1, "1d4", 15, "A small but dangerous creature, the goblin patrols the hallway armed with a small spear and ruined buckler. He stabs at rodents, looking for a snack...", [], -1, ["The goblin utters a high-pitched squeal.", f"The goblin says \"Zaza hungry! You look tasty!\"", f"The gobin bares his sharp, yellowed teeth."], ["The goblin stabs at you with his spear!", f"The goblin tries to bite your ankles!", "The goblin throws a rock at you!"])
    enemy_1b = Enemy("Orc", 15, 2, "1d6", 10, "An orc defends the next room, equipped with a massive axe. He snarls, perpetually angry...", [], -1, [f"The orc growls angrily.", f"The orc says \"Pathetic human!\"", f"The orc spins his axe meaningly."], ["The orc swings his axe at you!", f"The orc tries to chomp you!", "The orc throws a haymaker at you!"])
    enemy_1c = Enemy("Giant Spider", 20, 3, "1d8", 10, "A giant spider has claimed the ceiling, blocking the way forward. It avoids the light, tending to the dark corners of the room...", ["Fire"], -1, [f"The spider clicks its jaw hungrily.", f"The spider cleans his feelers.", f"The spider scuttles around erratically."], ["The spider attempts a poisonous bite!", f"The spider tries to claw at you!", "The spider shoots a tough ball of web at you!"])

    enemy_1_list = [enemy_1a, enemy_1b, enemy_1c]

    enemy_2a = Enemy("Minotaur", 25, 3, "1d8", 10, "A massive, tall, and ancient minotaur stands guard over the next room, his eyes piercing the darkness. He blows a heavy gust of air through his wide nostrils...", [], -1, [f"The minotaur grunts.", f"The minotaur stamps the ground, preparing to charge.", f"The minotaur points his horns at you."], ["The minotaur attempts to gore you!", f"The minotaur tries to punch you!", "The minotaur tries to kick you with a heavy hoof!"])
    enemy_2b = Enemy("Ghost", 15, 4, "1d6", 25 , "A ghostly knight stands guard over the next room, her eyes shining like a thousand stars. She longs for release from her curse...", ["Fire"], -1, [f"The ghost moans in despair.", f"The ghost flicks the lights on and off", f"The ghost looks through you, woefully."], [f"The ghost tries to steal your life force!", f"The ghost imbues you with necrotic energy!", f"The ghost fills your conscious with melancholy!"])
    enemy_2c = Enemy("Golem", 30, 4, "1d6", 0, f"The rock-made golem stoicly guards the path ahead. He stares straight ahead, holding a heavy metal mourningstar...", ["Water"], -1, [f"The golem just stands there, menacingly.", f"Did he just wink?", f"The golem stares at you."], ["The golem swings his mourningstar at you!", f"The golem throws a stone at you!", f"The golem tries to clap you!"])

    enemy_2_list = [enemy_2a, enemy_2b, enemy_2c]

    enemy_3a = Enemy("Dragon", 30, 4, "1d10", 5, "A dangerous, majestic dragon guards the final chamber. His red scales glitter against the torchlight...", ["Water"], -1, [f"The dragon roars loudly and proudly.", f"The dragon says \"Your time is up, creature!\"", f"The dragon unfurls his massive wings and roars!"], ["The dragon unleashes his fire breath on you!", f"The dragon reaches out with a huge claw to swipe you!", f"The dragon goes for a chomp!"])
    enemy_3b = Enemy("Necromancer", 25, 1, "1d8", 15, "A powerful, ancient necromancer guards the final chamber. His cabal of undead protect him, ready to carry out his orders...", ["Fire"], -1, [f"The necomancer raises more undead from the ground.", f"The necromancer prepares offensive spells.", f"The necromancer begins an unholy chant."], ["The necromancer tries to curse you!", f"The necromancer commands his undead minions to attack you!", f"The necromancer imbues your mind with necrotic energy!"])
    enemy_3c = Enemy("Demon", 30, 3, "1d8", 5, "A massive and ancient evil guards the final chamber. Armed with a flame whip and a blade of shadow, the demon is prepared to destroy life.", ["Water"], -1, [f"The demon speaks an cruel language, cursing you and your bloodline.", f"The demon paces back and forth, ready to strike.", f"The demon unleashes an unreal roar."], ["The demon strikes you with his whip!", f"The demon swings his blade at you!", f"The demon casts a spell of fire, engulfing you!"])

    enemy_3_list = [enemy_3a, enemy_3b, enemy_3c]

# An object of this class represents a single room in the dungeon.
    def __init__(self, name = "undef", description = "undef", lightLevel = 0, list_of_items = [], enemy = None, enemy1list = enemy_1_list, enemy2list = enemy_2_list, enemy3list = enemy_3_list) -> None:
        # When a Room object is created, the number of totals rooms is incremeted, and that value is assigned to the new objects positional number.
        Room.number_of_rooms += 1
        self.roomNumber = Room.number_of_rooms
# An object of the class has the following attributes manually assigned at creation time:
    # a room name (name : string)
        self.name = name
    # a description (description : string)
        self.description = description
    # a level of light (lightLevel : int)
        self.light_level = lightLevel
    # a list of items it contains (list_of_items : list)
        self.list_of_items = list_of_items
    # an enemy it may contain (enemy : Enemy)

        self.enemy = enemy

        self.room1_desc_dict = {"Haunted Hallway": "A dimly lit hallway with strange symbols etched into the walls. A wooden door leads to the next room.",
                           "Courtyard": "A well-lit courtyard filled with flowers and greenery. A hatch leads to the next room.",
                           "Foyer": "A well-lit foyer with a grand fireplace. A hallway leads to the next room.",
                           "Weathered Watchtower": "Light pierces through the gaps of the stone tower, lighting the interior. Stone stairs lead beneath the tower.",
                           "Sad Cottage" : "A small, dimly lit cottage with a cracked door and missing windows. A trap door leads to the next room." }
        
        self.room2_desc_dict = {"Labratory" : "A dimly lit room filled with dusty equipment and ancient books. Powered bulbs light the area well. A mechanical door leads to the next room.",
                           "Forbidden Library" : "A library filled with ancient texts and tomes, illegible to mortal eyes. Candles lightly illuminate the area. A trap door leads to the next room.",
                           "Torture Chamber" : "A room containing various torture devices. Candles lightly illuminate the area. Old blood paints the walls and floor. A stone door leads to the next room.",
                           "Guard Room" : "A room filled with empty bunk beds and broken furniture, lit by wall sconces. A stone door leads to the next room."}
        
        self.room3_desc_dict = {"Throne Room" : "A magestic and massive room, lit well by wall sconces. Royal tapestries and a red carpet lead to a golden throne. A gem adorned door leads to the final room.",
                           "Ritual Chamber" : "Energy eminates from this dimly-lit room, owing to the active ritual being performed. A stone door leads to the final room.",
                           "Treasure Hoard" : "A huge chamber filled with mountains of gold and jewels. A golden door leads to the final room."}
        
        self.item_desc_dict = {"health potion" : "Restores 10 HP",
                          "mana potion" : "Restores 5 MP",
                          "health elixir" : "Fully heals and increases your max HP by 5",
                          "lucky charm" : "Increases your chance to dodge by 10%",
                          "defense enchanted pendant" : "Increases your defense permenatly by 1",
                          "torch" : "Can be used to light up the room.",
                          "lantern" : "Can be used to light up the room."}
        
        self.room_light_dict = {"Haunted Hallway" : 1,
                           "Courtyard" : 2,
                           "Foyer" : 2,
                           "Weathered Watchtower" : 1,
                           "Sad Cottage" : 1,
                           "Labratory" : 2,
                           "Forbidden Library" : 1,
                           "Torture Chamber" : 1,
                           "Guard Room" : 2,
                           "Throne Room" : 2,
                           "Ritual Chamber" : 1,
                           "Treasure Hoard" : 2}
    
    def createRoom1(aRoom : 'Room'):
        random_room1_name = random.choice(list(aRoom.room1_desc_dict.keys()))
        aRoom.name = random_room1_name
        aRoom.description = aRoom.room1_desc_dict[room1.name]
        aRoom.light_level = aRoom.room_light_dict[room1.name]
        aRoom.list_of_items = [random.choice(list(aRoom.item_desc_dict.keys()))]
        aRoom.item_desc_dict.pop(room1.list_of_items[0])
        aRoom.enemy = Room.enemy_1a
        ## aRoom.enemy = random.choice(Room.enemy_1_list)

    def createRoom2(aRoom : 'Room'):
        random_room2_name = random.choice(list(aRoom.room2_desc_dict.keys()))
        aRoom.name = random_room2_name
        aRoom.description = aRoom.room2_desc_dict[room2.name]
        aRoom.light_level = aRoom.room_light_dict[room2.name]
        aRoom.list_of_items = [random.choice(list(aRoom.item_desc_dict.keys()))]
        aRoom.item_desc_dict.pop(room2.list_of_items[0])
        aRoom.enemy = random.choice(Room.enemy_2_list)

    def createRoom3(aRoom : 'Room'):
        random_room3_name = random.choice(list(aRoom.room3_desc_dict.keys()))
        aRoom.name = random_room3_name
        aRoom.description = aRoom.room3_desc_dict[room3.name]
        aRoom.light_level = aRoom.room_light_dict[room3.name]
        aRoom.list_of_items = [random.choice(list(aRoom.item_desc_dict.keys()))]
        aRoom.item_desc_dict.pop(room3.list_of_items[0])
        aRoom.enemy = random.choice(Room.enemy_3_list)


        

    
        
    
    # Methods:
    # __str__(self) -> str:
    ## Returns a string representation of the object. This will be used to display relevant information about the room object to the terminal.
    def __str__(self) -> str:
        return self.name
    
## Game ##
class Game:
# The Game class represents the user interface for the game.
# The class is responsible for taking in Room, User, and Enemy objects and handling user input.
    def showRoom(room : Room) -> None:
        ''' Prints the description of the room. '''
        os.system('cls')
        print("ROOM: " + room.name + '\n')
        print(room.description)
        if room.enemy:
            print(f"You hear a monster about...\n")
        else:
            print(f"There seems to be no more monsters here. The path ahead is clear.\n")
        print("\n\n\n\n\n")
    def userTurn(room : Room, user : User) -> None:
        os.system('cls')
        ''' The user will take their turn in the room. '''
        action = ""
        while action != "fight" or action != "move" or action != "examine" or action!= "search" or action!= "use" or action != "quit":
            user.displayStats()
            user.displayInventory()
            print()
            print(f"\nWhat do you want to do? (", end='', flush=True)
            if room.enemy:
                print(f"fight, ", end='', flush=True)
            else:
                print(f"move, ", end='', flush=True)
            print("examine, search, use, quit): ", end='', flush=True)
            action = input().lower()

            if action == "fight":
                Game.fight(room, user)
            elif action == "move":
                print("You enter the next room", end='', flush = True)
                i = 1
                while i <= 3:
                    time.sleep(.75)
                    print(".", end='', flush=True)
                    i += 1
                break
            elif action == "examine":
                Game.examine(room, user)
            elif action == "search":
                Game.search(room, user)
            elif action == "use":
                Game.use(room, user)
            elif action == "quit":
                print("Goodbye!")
                exit()
            else:
                print("Invalid action. Please try again.")
        
    def fight(room : Room, user : User) -> None:
        ''' The user will engage in a fight with the enemy. '''
        os.system('cls')
        time.sleep(1)
        enemy = room.enemy
        print(f"You engage in a battle with {enemy.name}!")
        while user.health > 0 and enemy.health > 0:
            print(f"\nYour health: {user.health}/{user.max_health}\n{room.enemy.name}: {enemy.health}")
            print(random.choice(room.enemy.barks))
            print("What do you want to do? (attack, use item, flee): ", end='', flush=True)
            action = input().lower()
            if action == "attack":
                print(f"You attack {room.enemy.name}!", flush = True)
                time.sleep(2)
                chance_to_hit = 100 - room.enemy.dodge_chance
                if random.randint(1, 100) <= chance_to_hit:
                    damage = user.getDamage()
                    crit_roll = random.randint(1, 100)
                    if crit_roll >= user.critical_hit_chance:
                        damage = int(damage * 1.5)
                        print(f"\nCRITICAL HIT!")
                    damage -= enemy.defense
                    if damage >= 0:
                        enemy.health -= damage
                        print(f"\nYou hit {room.enemy.name} for {damage} damage!")
                    else:
                        print(f"\nYou hit {room.enemy.name}, but it had no effect!")
                else:
                    print(f"\nYou miss {enemy.name}!")
                time.sleep(2)
            elif action == "use item" and len(user.inventory) > 0:
                user.displayInventory()
                print("Which item do you want to use? ", end='', flush=True)
                item_name = input()
                found = False
                for item in user.inventory:
                    if item_name.lower() == item.lower():
                        found = True
                        print(f"\nYou use {item}!")
                        user.useItem(item)
                    if not found:
                        print(f"\nYou don't have that item!")
                        break
                time.sleep(1)

            elif action == "flee":
                print("You flee the battle and retire in disgrace!")
                time.sleep(2)
                exit()
            if enemy.health <= 0:
                print(f"\n{enemy.name} is defeated!")
                room.enemy = None
                time.sleep(3)
                break
            else:
                print(f"\n{enemy.name} attacks!")
                time.sleep(2)
                chance_to_hit = 100 - user.dodge_chance
                if random.randint(1, 100) <= chance_to_hit:
                    damage = enemy.getDamage()
                    damage -= user.defense
                    if damage >= 1:
                        user.health -= damage
                        print(f"\n{enemy.name} hits you for {damage} damage!")
                    else:
                        print(f"\n{enemy.name} hits you, but it had no effect!")
                else:
                    print(f"\nYou dodge {enemy.name}'s attack!")
                time.sleep(1)
                if user.health <= 0:
                    print(f"\nYou have been defeated!")
                    time.sleep(3)
                    exit()


    def examine(room : Room, user : User) -> None:
        ''' The user will examine the current room and enemy. '''
        print(room.description, flush=True)
        time.sleep(1)
        if room.enemy:
            print(room.enemy.description, flush=True)
        else:
            print("The room is quiet...", end='\n', flush=True)
        time.sleep(1)

        input("Press anything to continue...")
        os.system('cls')

    def search(room : Room, user : User) -> None:
        ''' The user will search the current room for items. '''
        print("\nYou search the room", end='', flush=True)
        i = 1
        while i <= 5:
            time.sleep(.75)
            print(".", end='', flush=True)
            i += 1
        if len(room.list_of_items) > 0:
            print()
            print("You find:", end='', flush=True)
            for item in room.list_of_items:
                print(f" {item}", end='', flush=True)
                user.inventory.append(item)
            print(".")
        else:
            print("You find nothing...")
        
        input("\nPress anything to continue...")
        os.system('cls')

    def use(room : Room, user : User):
        ''' The user will use an item in their inventory. '''
        user.useItem(input("\nWhich item do you want to use? ").lower())

    def quit():
        ''' The game will end. '''
        want_to_quit = input("\nAre you sure you want to quit? (yes/no): ").lower()
        if want_to_quit == "yes".lower():
            print("Goodbye!", end='', flush=True)
            time.sleep(2)
            exit()

    

    
            

                        
                

            

## MAIN ##

## FUNCTION DEFINITIONS ##

def fakeLoad():
    ''' Simulates loading by printing a loading animation. '''
    i = 1
    k = 1
    while i <= 3:
        print("Loading", end='', flush=True)
        i += 1
        while k <= 3:
            print(".", end='', flush=True)
            time.sleep(0.5)
            k += 1
        os.system('cls')
        k = 1


if __name__ == "__main__":
    ''' The program will begin with a welcome message. 
    The user will then enter a character creation screen. 
    The user will be prompted to enter a name for the character. 
    The user will then select a class for their character.'''

    print(f"Welcome to the Dungeon Game! If you dare enter the dungeon ahead, press enter to continue...")
    input()
    print(f"Let's get started!")
    time.sleep(2)
    os.system('cls')
    name = input("Enter your character's name: ")
    print(f"Welcome, {name}!")
    time.sleep(2)
    os.system('cls')
    print(f"You are about to embark on an epic quest! Perils await you!")
    time.sleep(2)

    user = User()

    while True:
        try:
            classChoice = int(input("Choose your class:\n1) Warrior\n2) Mage\n3) Ranger\n"))
            if classChoice in [1, 2, 3]:
                break
        except ValueError:
            print("Please enter a valid number (1, 2, or 3).", end='', flush=True)
            time.sleep(2)
            os.system('cls')
    
    os.system('cls')
    if classChoice == 1:
        print(f"You have chosen the Warrior class!")

        user.name = name
        user.player_class = "Warrior"
        user.health = 20
        user.max_health = 20
        user.defense = 3
        user.attack_dice = "1d10"
        user.dodge_chance = 5
        user.strength = 15
        user.dexterity = 10
        user.intelligence = 5
        user.critical_hit_chance = 10
        user.mana = 5
        user.max_mana = 5
        user.special = "Shield Bash"

    elif classChoice == 2:
        print(f"You have chosen the Mage class!")
        user.name = name
        user.player_class = "Mage"
        user.health = 12
        user.max_health = 12
        user.defense = 1
        user.attack_dice = "1d8"
        user.dodge_chance = 10
        user.strength = 5
        user.dexterity = 10
        user.intelligence = 15
        user.critical_hit_chance = 15
        user.mana = 20
        user.max_mana = 20
        user.special = "Fireball"

    elif classChoice == 3:
        print(f"You have chosen the Ranger class!")
        user.name = name
        user.player_class = "Ranger"
        user.health = 15
        user.max_health = 15
        user.defense = 2
        user.attack_dice = "1d8"
        user.dodge_chance = 15
        user.strength = 8
        user.dexterity = 15
        user.intelligence = 8
        user.critical_hit_chance = 20
        user.mana = 10
        user.max_mana = 10
        user.special = "Focus"

    time.sleep(2)

    print(f"Your character has been created! The dungeon awaits. Press enter to proceed...")
    input()
    os.system('cls')

    room1 = Room("Entryway")
    fakeLoad()

    print(f"{user.name} the {user.player_class} approaches the entrance of the dungeon. A dark and foreboding energy fills the air as the maw of the ornate but sinister doors beckon our intrepid adventurer forward.")

    time.sleep(2)
    print("The doors creak open, revealing...", flush = True)
    time.sleep(2)

    room1 = Room()
    room2 = Room()
    room3 = Room()

    Room.createRoom1(room1)

    Game.showRoom(room1)
    Game.userTurn(room1, user)

    Room.createRoom2(room2)

    Game.showRoom(room2)
    Game.userTurn(room2, user)

    Room.createRoom3(room3)

    Game.showRoom(room3)
    Game.userTurn(room3, user)

    os.system('cls')
    print("You have successfully defeated the final boss!", flush = True)
    time.sleep(2)
    print(f"{user.name} the {user.player_class}, you have earned legendary renown and the title of Hero!", flush = True)
    time.sleep(2)   
    print("Thank you for playing the Dungeon Game! Goodbye!")
    exit()



