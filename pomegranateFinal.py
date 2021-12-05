import random
import Scoring as sc
import cardswap as cs

#Creates and shuffles deck
deck = ["AH","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH",
        "AS","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS",
        "AD","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD",
        "AC","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC"]
graveyard = []
# pot = 0
# current_bet = 0
dealers_hand = deck


class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
  
        
#current_bet = int(input("Enter Starting Bet: "))
    #raise value errror if negative or not a number
# pot += int(current_bet)


# -- TO PRINT OTHER HAND --
# print("\nOpponenet's Hand:")
# opponent_hand = dealers_hand[:5]
# for card in opponent_hand:
#     print(card, end = " ")


# -- TO PRINT  REMAINING CARDS --
# dealers_hand = dealers_hand[5:]
# print("\nDealer's Hand:")
# for card in dealers_hand:
#     print(card, end = " ")
    
    
    
def callRaiseFold(self, pot, current_bet):
    action = input("\nCall (1), Raise (2), or Fold (3)? ")
    if action == "1":
        print("1")
        pot += current_bet

    if action == "2":
        raised = int(input("Enter Raised Bet: "))
        if raised < current_bet:
            print("New bet is not higher than previous bet.")
            callRaiseFold(pot,current_bet)
        else:
            current_bet = int(input("Enter Raised Bet: "))
            # raise value errror if
            #   bet is lower than before
            #   not a number
            pot += current_bet
        
    if action == "3":
        print("You Lose!")
        #discard player's hand into graveyard
        
    # -- TO PRINT GRAVEYARD --
    # for card in graveyard:
    #     print(card, end = " ")


print("\nLet's Play\n")

random.shuffle(deck)

#gives player 5 cards from the deck
your_hand = dealers_hand[:5]
#displays player's hand
print("Your Hand:")
for card in your_hand:
    print(card, end = " ")
print("\n")
#takes player's cards out of the dealer's hand
dealers_hand = dealers_hand[5:]

def turn():
    choice = (input("Swap Cards? (1 for yes, 2 for no)"))
    if choice == 1:
        pass
        #calls method to replace cards
        #cs.draw(player = 0, deck = 0, cards = 0))
        #callRaiseFold(pot = 0, current_bet = 0)
    else:
        pass
        #callRaiseFold(pot = 0, current_bet= 0)
 
    #call scoring to find the final score


#main function
#loop to stop the turns when game is over
# while gameState = True:
#     turn()