# This program deals out a hand of cards from a 52 card deck.

# INCOMPLETE CODE 

import os
import time
import random

# CONSTANTS

SUITS = ["D", "H", "C", "S"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "0", "J", "Q", "K", "A"]

def viewTable(aHand: list, comCards: list, round: int):
    # os.system('cls')
    for i in range(50):
        print("-", end='')
    print()
    for i in range(3):
        for i in range(50):
            if (i == 0) or (i == 49):
                print("|", end='')
            else:
                print(" ", end='')
        print()

        
    match round:
        case 1:
            print("|\t\t" + comCards[0] + " " + comCards[1] + " " + comCards[2] + " ?? ??                   |")
        case 2:
            print("|\t\t" + comCards[0] + " " + comCards[1] + " " + comCards[2] + " " + comCards[3] + " " + "??                   |")
        case 3:
            print("|\t\t" + comCards[0] + " " + comCards[1] + " " + comCards[2] + " " + comCards[3] + " " + comCards[4] + "                   |")

    for i in range(3):
        for i in range(50):
            if (i == 0) or (i == 49):
                print("|", end='')
            else:
                print(" ", end='')
        print()
    for i in range(50):
        print("-", end='')

    print("")
    print("YOUR HAND: ", end='')

    for card in aHand:
        print(card + " ", end='')

    print("\n")

def playRound(aDeck: list, aHand: list, communityCards: list, roundCount: int):

    match(roundCount):
        case 1:
            print(f"Welcome to Texas Hold'em Poker!\n\nPress anything to play!")
            print(f"Dealing", end='')
            
            print(f".", end ='')
            
            
            print(f" .", end='')
            
            
            print(f" .", end='')
            
            
            
            
            
            viewTable(aHand, communityCards, 1)
        case 2:
            viewTable(aHand, communityCards, 2)
        case 3:
            viewTable(aHand, communityCards, 3)

    
    

    




def main():

    # Create a deck
    theDeck= []
    for suit in SUITS: 
        for rank in RANKS:
            theDeck.append(rank + suit)

    # print(theDeck) # TEST

    # Shuffle the deck
    random.shuffle(theDeck)

    # print(theDeck) # TEST

    # Create a hand
    hand= []

    for i in range(2):
        card = theDeck[i]
        hand.append(card)
        theDeck.remove(card)

    # Create the community cards
    communityCards= []

    for i in range(5):
        card = theDeck[i]
        communityCards.append(card)
        theDeck.remove(card)

    # Start game

    os.system("cls")
    round = 1
    for i in range(3):
        playRound(theDeck, hand, communityCards, round)
        round = round + 1


    
    # print(hand) # TEST
    # print(len(theDeck)) # TEST
    # print (theDeck) #test



if __name__ == '__main__':
    main()