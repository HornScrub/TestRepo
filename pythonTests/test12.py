import random
import time
import os

# CONSTANTS

SUITS = ["D", "H", "C", "S"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "0", "J", "Q", "K", "A"]


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.purse = 100
        self.inGame = True
    
    def bet(self, amount):
        if self.purse >= amount:
            self.purse -= amount
            return True
        else:
            return False
    
    def win(self, amount):
        self.purse += amount
        return True
    

# Create a deck
theDeck= []
for suit in SUITS: 
    for rank in RANKS:
        theDeck.append(rank + suit)

# Shuffle the deck
random.shuffle(theDeck)

# Create player list

playerList= []

os.system("cls")

userName = str(input("Enter name: "))
user = Player(userName)

playerList.append(user)

while True:
    try:
        numOfOpponents = int(input("Number of opponents: "))
        if (numOfOpponents > 0) and (numOfOpponents) < 8:
            break
        else:
            print("Please enter a valid number between 1 and 7.")
    except ValueError:
        print("Please enter a valid number between 1 and 7.")

nameList = ["William", "Akissi", "Quinton", "Justin", "Ramone", "Twila", "Vikram", "Molly"]

for opponent in range(numOfOpponents):
    name = random.choice(nameList)
    opponent = Player(name)
    playerList.append(opponent)
    nameList.remove(name)

# Pick Dealer

random.shuffle(playerList)

# Deal hands

for i in range(2):
    for player in playerList:
        card = theDeck[i]
        player.hand.append(card)
        theDeck.remove(card)

# Create the community cards
communityCards= []

for i in range(5):
    card = theDeck[i]
    communityCards.append(card)
    theDeck.remove(card)


# for player in playerList:
#     print(player.name)
#     print(player.hand)
#     print(player.purse)

# Start Game (Round 1)

pot = 0

for i in range(4):
    os.system('cls')
    print(f"Round {i + 1}\n")
    print("Community cards: ",end='')
    time.sleep(1)
    for communityCard in range(2 + i):
        print(communityCards[communityCard], end=' ')
    print(f"\nPot: {pot}\n")
    
    for currentPlayer in playerList:
        if currentPlayer.inGame:
            print(f"{currentPlayer.name}'s turn.")
            time.sleep(1)
            
            if currentPlayer == user: # If its the players turn
                choice = 0
                while True:
                    try:
                        
                        print(f"Your cards: {user.hand}\nYour purse: {user.purse}\n")
                        choice = int(input("1) BET [5]\n2) BET [10]\n3) FOLD\n"))
                        if choice in [1, 2, 3]:
                            break
                        else:
                            print("Please enter a valid number (1, 2, or 3).")
                    except ValueError:
                        print("Please enter a valid number.")

                match(choice):
                    case 1:
                        if user.bet(5):
                            print(f"You bet [5]")
                            pot += 5
                            
                        else:
                            user.bet(user.purse)
                    case 2:
                        if user.bet(10):
                            print(f"You bet [10]")
                            pot += 10
                            
                        else:
                            user.bet(user.purse)
                    case 3:
                        print(f"You folded")
                        user.inGame = False
                        
                    
                    case _:
                        print("Something went wrong!")
                        break
                
                

            else: # If its the computers turn
                compChoice = random.randint(1, 3)
                match(compChoice):
                    case 1:
                        if currentPlayer.bet(5):
                            print(f"{currentPlayer.name} bet [5].")
                            pot += 5
                            
                        else:
                            currentPlayer.bet(currentPlayer.purse)
                    case 2:
                        if currentPlayer.bet(10):
                            print(f"{currentPlayer.name} bet [10].")
                            pot += 10
                            
                        else:
                            currentPlayer.bet(currentPlayer.purse)
                    case 3:
                        currentPlayer.inGame = False
                        print(f"{currentPlayer.name} folded.")
            
            time.sleep(1)
            print(f"Pot: {pot}")
            time.sleep(1)
    
    print(f"\nRound {i + 1} complete.")
    continuationInputoftheGods = input("Enter anything to continue. . .")
        
        
    

