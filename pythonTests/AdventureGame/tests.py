import random, os, time

from game import User, Enemy, Room, Game

user = User()

user.name = "Test Man"
user.player_class = "Warrior"
user.health = 20
user.max_health = 20
user.defense = 3
user.attack_dice = "1d6"
user.dodge_chance = 5
user.strength = 15
user.dexterity = 10
user.intelligence = 5
user.critical_hit_chance = 10
user.mana = 5
user.max_mana = 5
user.special = "Shield Bash"
user.inventory = ["Health Potion"]

room1 = Room()

room1.name = "Test Room"

room1.description = "A dark and dusty room filled with ancient artifacts and strange creatures."

room1.enemy = Enemy("Giant Spider")

enemy_1a = Enemy("Goblin", 10, 1, "1d4", 15, "A small but dangerous creature, the goblin patrols the hallway armed with a small spear and ruined buckler. He stabs at rodents, looking for a snack...", [], -1, ["The goblin utters a high-pitched squeal.", f"The goblin says \"Zaza hungry! You look tasty!\"", f"The gobin bares his sharp, yellowed teeth."], ["The goblin stabs at you with his spear!", f"The goblin tries to bite your ankles!", "The goblin throws a rock at you!"])
room1.enemy = enemy_1a

Game.showRoom(room1)
Game.userTurn(room1, user)






