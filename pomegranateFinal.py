import random

#Creates and shuffles deck
deck = ["AH","2H","3H","4H","5H","6H","7H","8H","9H","TH","JH","QH","KH",
        "AS","2S","3S","4S","5S","6S","7S","8S","9S","TS","JS","QS","KS",
        "AD","2D","3D","4D","5D","6D","7D","8D","9D","TD","JD","QD","KD",
        "AC","2C","3C","4C","5C","6C","7C","8C","9C","TC","JC","QC","KC"]
deckstate = deck.copy()


class Player():
    """
    Attributes:
        hand - the given player's hand of cards
    """
    def __init__(self, hand):
        self.hand = hand

    def draw(self, deck, cards):
        """
        Args:
            deck - the current deck of cards
            cards - player's hand of cards
        """
        need1 = False
        need2 = False
        need3 = False
        need4 = False
        need5 = False
        if 5 in cards:
            need5 = True
        if 4 in cards:
            need4 = True
        if 3 in cards:
            need3 = True
        if 2 in cards:
            need2 = True
        if 1 in cards:
            need1 = True
        if need1:
            self.hand[0] = random.choice(list(deck))
            deck.remove(self.hand[0])
        if need2:
            self.hand[1] = random.choice(list(deck))
            deck.remove(self.hand[1])
        if need3:
            self.hand[2] = random.choice(list(deck))
            deck.remove(self.hand[2])
        if need4:
            self.hand[3] = random.choice(list(deck))
            deck.remove(self.hand[3])
        if need5:
            self.hand[4] = random.choice(list(deck))
            deck.remove(self.hand[4])


def turn(player1, computer, deck):
    """
    Args:
        player1 - the human player
        computer - the computer player
        deck - the currect deck
    """
    choice = int(input("Swap Cards? (1 for yes, 2 for no)"))
    if choice == 1:
        cards = input("Which Cards? (List card numbers separated by a comma)")
        cardlist = [int(i) for i in cards.split(',')]
        player1.draw(deck, cardlist)
    l = [1, 2, 3, 4, 5]
    compcards = random.sample(l, (random.choice(l)))
    compcardlist = [int(j) for j in compcards]
    return

        
def haspair(cards):
    """
    Args:
        cards - player's hand of cards
    """
    cardnums = [i[0] for i in cards]
    for num in cardnums:
        if cardnums.count(num) == 2:
            return True
    return False     

def hastwopair(cards):
    """
    Args:
        cards - player's hand of cards
    """
    has1 = False
    cardnums = [i[0] for i in cards]
    for num in cardnums:
        if cardnums.count(num) == 2 and has1 == False:
            has1 = True
            cardnums.remove(num)
        if cardnums.count(num) == 2 and has1 == True:
            return True
    return False

def has3ofakind(cards):
    """
    Args:
        cards - player's hand of cards
    """
    cardnums = [i[0] for i in cards]
    for num in cardnums:
        if cardnums.count(num) == 3:
            return True
    return False
        
def hasstraight(cards):
    """
    Args:
        cards - player's hand of cards
    """
    inside = False
    count = 0
    cardvals = list()
    cardnums = [i[0] for i in cards]
    for num in cardnums:
        if num == "K":
            cardvals.append(13)
            continue
        if num == "Q":
            cardvals.append(12)
            continue
        if num == "J":
            cardvals.append(11)
            continue
        if num == "T":
            cardvals.append(10)
            continue
        if num == "A":
            pass
        else:
            cardvals.append(int(num))
    high = max(cardvals)
    low = min(cardvals)
    for num in cardvals:
        if num >= low and num <= high:
            count += 1
        if count == 5:
            inside = True
            break
    if inside and (high - low == 4):
        return True
    else:
        return False
    
def hasflush(cards):
    """
    Args:
        cards - player's hand of cards
    """
    clubs = 0
    hearts = 0
    diamonds = 0
    spades = 0
    for card in cards:
        if card[1] == "C":
            clubs += 1
        if card[1] == "H":
            hearts += 1
        if card[1] == "D":
            diamonds += 1
        if card[1] == "S":
            spades += 1
    if clubs == 5 or hearts == 5 or diamonds == 5 or spades == 5:
        return True
    else:
        return False        

def hasfullhouse(cards):
    """
    Args:
        cards - player's hand of cards
    """
    has1 = False
    cardnums = [i[0] for i in cards]
    for num in cardnums:
        if cardnums.count(num) >= 2 and has1 == False:
            has1 = True
            cardnums.remove(num)
        if cardnums.count(num) >= 2 and has1 == True:
            return True
    return False    
    
def has4ofakind(cards):
    """
    Args:
        cards - player's hand of cards
    """
    cardnums = [i[0] for i in cards]
    for num in cardnums:
        if cardnums.count(num) == 4:
            return True
    return False
    
def hasstraightflush(cards):
    """
    Args:
        cards - player's hand of cards
    """
    if hasstraight(cards) and hasflush(cards):
        return True
    else:
        return False

def checkhand(hand):
    """
    Args:
        hand - player's hand of cards
    """
    if hasstraightflush(hand):
        return 9
    elif has4ofakind(hand):
        return 8
    elif hasfullhouse(hand):
        return 7
    elif hasflush(hand):
        return 6
    elif hasstraight(hand):
        return 5
    elif has3ofakind(hand):
        return 4
    elif hastwopair(hand):
        return 3
    elif haspair(hand):
        return 2
    else:
        return 1

<<<<<<< HEAD
def tiebreaker(p1_hand, p2_hand):
    """
    Args:
        p1_hand - first player's hand of cards
        p1_hand - second player's hand of cards
    """
    p1_hand_count = 0
    p2_hand_count = 0
    
    for card in p1_hand:
        value = card[0]
        if value == "A":
            p1_hand_count = p1_hand_count + 14
        elif value == "T":
            p1_hand_count = p1_hand_count + 10
        elif value == "J":
            p1_hand_count = p1_hand_count + 11
        elif value == "Q":
            p1_hand_count = p1_hand_count + 12
        elif value == "K":
            p1_hand_count = p1_hand_count + 13
        else:
            p1_hand_count + p1_hand_count + int(value)
    for card in p2_hand:
        value = card[0]
        if value == "A":
            p2_hand_count = p2_hand_count + 14
        elif value == "T":
            p2_hand_count = p2_hand_count + 10
        elif value == "J":
            p2_hand_count = p2_hand_count + 11
        elif value == "Q":
            p2_hand_count = p2_hand_count + 12
        elif value == "K":
            p2_hand_count = p2_hand_count + 13
        else:
            p2_hand_count + p2_hand_count + int(value)
    if p1_hand_count > p2_hand_count:
        print("You win!")
    else:
        print("You lose :(")
    
     
=======
def removeShuffled(deckstate):
    i = 0
    while i < 5:
        deckstate.pop()
        i+=1
>>>>>>> a238db316dcff81639104b0247ba24ff32e188d1

def main():
    print("\nLet's Play\n")
    random.shuffle(deckstate)
    p1hand = deckstate[-5:]
    removeShuffled(deckstate)
    computerhand = deckstate[-5:]
    removeShuffled(deckstate)
    print(deckstate)
    p1 = Player(p1hand)
    computer = Player(computerhand)
    print(f"Your Hand: {p1.hand}")
    turn(p1, computer, deckstate)
    print("Your Hand:")
    for card in p1.hand:
        print(f"{card}")
    print("The Computer's Hand:")
    for card in computer.hand:
        print(f"{card}")
    p1_handstrength = checkhand(p1.hand)
    comp_handstrength = checkhand(computer.hand)
    if p1_handstrength > comp_handstrength:
        print("You win!")
    elif comp_handstrength > p1_handstrength:
        print("You lose :(")
    else:
        tiebreaker(p1.hand, computer.hand)


if __name__ == "__main__":
    main()