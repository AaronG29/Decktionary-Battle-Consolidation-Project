#Import random
import random
#First step, start setting up the decktionary battle deck (MAKE SURE TO EXCLUDE KINGS)
def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = list(range(1, 14))  #Range excluding the king
    values.remove(13)  #Removal of king, number 13
    deck = [(value, suit) for value in values for suit in suits]
    random.shuffle(deck)
    return deck

#Players must now get their hands
def deal_cards(deck):
    player1 = deck[:8] #Player 1 deck
    player2 = deck[8:16] #Player 2 deck
    return player1, player2, deck[16:]

#Show the players hand to them so they can play
def display_hand(player):
    print("Your hand:")
    index = 1  
    for card in player:
        rank = card[0]  #Rank of the card
        suit = card[1]  #Suit of the card
        print(str(index) + ": " + str(rank) + " of " + suit)  #Display to the players their card
        index += 1  #Index increminted

#Decide whether of not player one or player two won the hand
def determine_winner(the_leading_card, the_following_card, the_leading_suit):
    #Check if the next card matches up with the initial card
    if the_following_card[1] == the_leading_suit:
        #Comparison of cards in order to decide who the winner is
        if the_following_card[0] > the_leading_card[0]:
            return "follow"  #Player 2 wins that round
    #If card is weaker player 1 wins
    return "lead"

#Create the game loop
#Player one will start
#Player 2 will play after player 1
#Decide who won
#Final score and winner of Decktionary battle
#Run game