#Import random
import random
#First step, start setting up the decktionary battle deck (MAKE SURE TO EXCLUDE KINGS)
def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = list(range(1, 14))  #Range excluding the king
    values.remove(13)  #Removal of king, number 13
    deck = [(value, suit) for value in values for suit in suits]
#Players must now get their hands
#Show the players hand to them so they can play
#Decide whether of not player one or player two won the hand
#Create the game loop
#Player one will start
#Player 2 will play after player 1
#Decide who won
#Final score and winner of Decktionary battle
#Run game