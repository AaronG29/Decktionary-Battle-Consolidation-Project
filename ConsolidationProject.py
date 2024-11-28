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


def play_game():
    #Script a shuffled deck and show both players their cards
    deck = create_deck()
    player1, player2, _ = deal_cards(deck)  #Ignore cards that aren't used
    scores = {"Player 1": 0, "Player 2": 0}  #Tracking scoring
    #Keep looping through all 8 rounds
    for round_number in range(1, 9):
        print("\nRound " + str(round_number) + ":")

        #Display hand to Player 1
        print("Player 1's Turn:")
        display_hand(player1)
        lead_index = int(input("Choose a card to play (1-8): ")) - 1
        the_leading_card = player1.pop(lead_index)  #The chosen card of Player 1 is removed from his hand
        the_leading_suit = the_leading_card[1]  #Suit of leading card

        #Display hand to Player 2
        print("Player 2's Turn:")
        display_hand(player2)
        follow_index = int(input("Choose a card to play (1-8): ")) - 1
        the_following_card = player2.pop(follow_index)  #The chosen card of Player 2 is removed from his hand

        #Determining winner of the round
        winner = determine_winner(the_leading_card, the_following_card, the_leading_suit)
        if winner == "lead":
            scores["Player 1"] += 1
            print("Player 1 wins this round!")
        else:
            scores["Player 2"] += 1
            print("Player 2 wins this round!")

        # Display the current scores
        print(f"The Scores so far: {scores}")


#Final score and winner of Decktionary battle
    print("\nFinal Scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")
    if scores["Player 1"] > scores["Player 2"]:
        print("Congrats, Player 1 you win the game!")
    else:
        print("Congrats, Player 2 you win the game!")

#Run game
play_game()