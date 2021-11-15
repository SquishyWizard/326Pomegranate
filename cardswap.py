import random

class Player:
    def __init__(self, hand):
        self.hand = hand
        

def draw(player, deck, cards):
    need1 = False
    need2 = False
    need3 = False
    need4 = False
    need5 = False
    if 1 in cards:
        del player.hand[1]
        need1 = True
    if 2 in cards:
        del player.hand[2]
        need2 = True
    if 3 in cards:
        del player.hand[3]
        need3 = True
    if 4 in cards:
        del player.hand[4]
        need4 = True
    if 5 in cards:
        del player.hand[5]
        need5 = True
    if need1:
        player.hand[1] = random.choice(list(deck.values()))
    if need2:
        player.hand[2] = random.choice(list(deck.values()))
    if need3:
        player.hand[3] = random.choice(list(deck.values()))
    if need4:
        player.hand[4] = random.choice(list(deck.values()))
    if need5:
        player.hand[5] = random.choice(list(deck.values()))
 