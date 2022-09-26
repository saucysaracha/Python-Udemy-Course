#Blackjack game
#If cards in your hand add up to > 21, it's called a bust and you lose immediately
#J, K, Q count as 10
#A can be 1 or 11
#if your score = dealers score, its a draw
#If they have 21 and we have 20, we lose
#If the dealer ends up with a hand <17, then they must take another card

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from re import M
from BlackjackArt import logo

def deal_card():
    """Deals one random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_chosen = random.choice(cards)
    return card_chosen

# def game_continue(my_deck, computer_deck):
#     if( (add_up_deck(my_deck)) > 21):
#         game_over(my_deck, computer_deck)
#         return False
#     elif( (add_up_deck(my_deck)) == 21 ):
#         game_over(my_deck, computer_deck)
#         return False
#     else:
#         return True
    

def game_over(my_deck, computer_deck):
    if((add_up_deck(my_deck) > 21) and (add_up_deck(computer_deck) <= 21)):
        print(f"\nYour final hand: {my_deck}, final score: {add_up_deck(my_deck)}")
        print(f"Computer's final hand: {computer_deck}, final score: {add_up_deck(computer_deck)}")
        print("You lose :(")
        return True
    elif((add_up_deck(my_deck) <= 21) and (add_up_deck(computer_deck) > 21)):
        print(f"\nYour final hand: {my_deck}, final score: {add_up_deck(my_deck)}")
        print(f"Computer's final hand: {computer_deck}, final score: {add_up_deck(computer_deck)}")
        print("You win :)")
        return True
    elif((add_up_deck(my_deck) > 21) and (add_up_deck(computer_deck) > 21)):
        print(f"\nYour final hand: {my_deck}, final score: {add_up_deck(my_deck)}")
        print(f"Computer's final hand: {computer_deck}, final score: {add_up_deck(computer_deck)}")
        print("It's a bust :/")
        return True
    elif( add_up_deck(my_deck) == add_up_deck(computer_deck) ):
        print(f"\nYour final hand: {my_deck}, final score: {add_up_deck(my_deck)}")
        print(f"Computer's final hand: {computer_deck}, final score: {add_up_deck(computer_deck)}")
        print("It is a draw :/")
        return True
    elif( add_up_deck(my_deck) < add_up_deck(computer_deck) ):
        print(f"\nYour final hand: {my_deck}, final score: {add_up_deck(my_deck)}")
        print(f"Computer's final hand: {computer_deck}, final score: {add_up_deck(computer_deck)}")
        print("You lose :(")
        return True
    elif( add_up_deck(my_deck) > add_up_deck(computer_deck) ):
        print(f"\nYour final hand: {my_deck}, final score: {add_up_deck(my_deck)}")
        print(f"Computer's final hand: {computer_deck}, final score: {add_up_deck(computer_deck)}")
        print("You win :)")
        return True
    else:
        return False

def add_up_deck(deck):
    sum_of_deck = 0
    for cards in deck:
        sum_of_deck += cards
    return sum_of_deck

def print_scores(my_deck, computer_deck):
    print(f"\nYour cards: {my_deck}, current score: {add_up_deck(my_deck)}")
    print(f"Computer's first card: {computer_deck[0]}")



#main
play_blackjack = (input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")).lower()
gameover = False
while(play_blackjack == "y"):
    while(gameover == False):
        #main code here
        print(logo)
        my_deck = [deal_card(), deal_card()]
        computer_deck = [deal_card(), deal_card()]
        while(add_up_deck(computer_deck) < 17):
            computer_deck.append(deal_card())
        
        print_scores(my_deck, computer_deck)
        
        continue_or_not = True
        if( (add_up_deck(my_deck)) > 21):
            game_over(my_deck, computer_deck)
            continue_or_not = False
        elif( (add_up_deck(my_deck)) == 21 ):
            game_over(my_deck, computer_deck)
            continue_or_not = False
        
        while (continue_or_not == True):
            wannacontinue = ((input("Type 'y' to get another card, type 'n' to pass: ")).lower())
            if(wannacontinue == "n"):
                continue_or_not = False
                game_over(my_deck, computer_deck)
            elif(wannacontinue == "y"):
                my_deck.append(deal_card())
                print_scores(my_deck, computer_deck)
            
            if( (add_up_deck(my_deck)) > 21):
                game_over(my_deck, computer_deck)
                continue_or_not = False
            elif( (add_up_deck(my_deck)) == 21 ):
                game_over(my_deck, computer_deck)
                continue_or_not = False

        play_blackjack = (input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")).lower()
        if(play_blackjack == "y"):
            gameover = False
        if(play_blackjack == "n"):
            gameover == True
            break