import random


deck = ["AH","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH",
        "AS","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS",
        "AD","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD",
        "AC","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC"]
graveyard = []
pot = 0
current_bet = 0

class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

dealers_hand = deck
bet = input("Enter bet: ")
#raise value errror if negative or not a number
#raise value error if lower than the previous bets
pot += int(bet)
print("Let's Play")
random.shuffle(deck)

your_hand = dealers_hand[:5]
print("Your Hand:")
for card in your_hand:
    print(card, end = " ")
dealers_hand = dealers_hand[5:]

print("\nOpponenet Hand:")
opponent_hand = dealers_hand[:5]
for card in opponent_hand:
    print(card, end = " ")
    
dealers_hand = dealers_hand[5:]
print("\nDealer's Hand:")
for card in dealers_hand:
    print(card, end = " ")
    
    
action = input("\nCall (1), Raise (2), or Fold (3)? ")
if action == "1":
    print("1")
    #add money to pot
    pass

if action == "2":
    print("2")
    pass
    #how much more money
    #raise current bet
    #add money to pot
    
if action == "3":
    print("3")
    pass
    #you lose
    #discard player's hand into graveyard
