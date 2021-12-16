import random

#Creates and shuffles deck
deck = ["AH","2H","3H","4H","5H","6H","7H","8H","9H","TH","JH","QH","KH",
        "AS","2S","3S","4S","5S","6S","7S","8S","9S","TS","JS","QS","KS",
        "AD","2D","3D","4D","5D","6D","7D","8D","9D","TD","JD","QD","KD",
        "AC","2C","3C","4C","5C","6C","7C","8C","9C","TC","JC","QC","KC"]
deckstate = deck.copy()


class Player():
    """Class describing the player
    
    Attributes:
        hand - the given player's hand of cards
    """
    def __init__(self, hand):
        self.hand = hand

    def draw(self, deck, cards):
        """Adds 1-5 cards to a player's hand
        
        Args:
            deck - the current deck of cards
            cards - player's hand of cards
        
        Side effects:
            Removes items from the list "deck"
            Adds new items to the hand attribute
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
    """Represents the player's turn in the game
    
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
    """Checks to see if player has a pair
    
    Args:
        cards - player's hand of cards
    
    Returns:
        boolean - true if the player has a pair,
            false if the player does not have a pair
    """
    cardnums = [i[0] for i in cards]
    for num in cardnums:
        if cardnums.count(num) == 2:
            return True
    return False     

def hastwopair(cards):
    """Checks to see if player has a two-pair
    
    Args:
        cards - player's hand of cards
    
    Returns:
        boolean - true if the player has a two-pair,
            false if the player does not have a two-pair
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
    """Checks to see if player has a 3 of a kind
    
    Args:
        cards - player's hand of cards
    
    Returns:
        boolean - true if the player has a 3 of a kind,
            false if the player does not have a 3 of a kind
    """
    cardnums = [i[0] for i in cards]
    for num in cardnums:
        if cardnums.count(num) == 3:
            return True
    return False
        
def hasstraight(cards):
    """Checks to see if player has a straight
    
    Args:
        cards - player's hand of cards
    
    Returns:
        boolean - true if the player has a straight,
            false if the player does not have a straight
    """
    inside = False
    count = 0
    cardvals = list()
    cardnums = [i[0] for i in cards]
    for num in cardnums:
        cardvals.append(int(faceconvert(num)))
    if 14 in cardvals and 2 in cardvals and 3 in cardvals and 4 in cardvals\
    and 5 in cardvals:
        return True
    high = max(cardvals)
    low = min(cardvals)
    for num in cardvals:
        if num >= low and num <= high:
            count += 1
        if count == 5:
            inside = True
            break
    if inside and (high - low == 4) and not haspair(cards):
        return True
    else:
        return False
    
def hasflush(cards):
    """Checks to see if player has a flush
    
    Args:
        cards - player's hand of cards
    
    Returns:
        boolean - true if the player has a flush,
            false if the player does not have a flush
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
    """Checks to see if player has a full house
    
    Args:
        cards - player's hand of cards
    
    Returns:
        boolean - true if the player has a full house,
            false if the player does not have a full house
    """
    has1 = False
    cardnums = [i[0] for i in cards]
    for num in cardnums:
        if cardnums.count(num) == 2 and has1 == False:
            has1 = True
            cardnums.remove(num)
    for num in cardnums:
        if cardnums.count(num) == 3 and has1 == True:
            return True
    return False    
    
def has4ofakind(cards):
    """Checks to see if player has a 4 of a kind
    
    Args:
        cards - player's hand of cards
    
    Returns:
        boolean - true if the player has a 4 of a kind,
            false if the player does not have a 4 of a kind
    """
    cardnums = [i[0] for i in cards]
    for num in cardnums:
        if cardnums.count(num) == 4:
            return True
    return False
    
def hasstraightflush(cards):
    """Checks to see if player has a straight-flush
    
    Args:
        cards - player's hand of cards
    
    Returns:
        boolean - true if the player has a straight-flush,
            false if the player does not have a straight-flush
    """
    if hasstraight(cards) and hasflush(cards):
        return True
    else:
        return False

def checkhand(hand):
    """Reviews the player's hand to see what kind of a hand
    they have
    
    Args:
        hand - player's hand of cards
    
    Returns:
        int - number representing the strength of their hand
            (will be 1-9)
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
    
def faceconvert(card):
    """Converts Face cards to values
    
    Args:
        card - a card in a player's hand
    
    Returns:
        val - the value of the face card as an int
    """
    if card == "A":
        val = 14
    elif card == "K":
        val = 13
    elif card == "Q":
        val = 12
    elif card == "J":
        val = 11
    elif card == "T":
        val = 10
    else:
        val = card
    return val
 
def tiebreaker(p1_hand, p2_hand):
    """Determines the winner if both players' hands are of the same strength
    
    Args:
        p1_hand - first player's hand of cards
        p1_hand - second player's hand of cards
    """
    if has4ofakind(p1_hand) or has3ofakind(p1_hand) or hasfullhouse(p1_hand)\
        or hastwopair(p1_hand) or haspair(p1_hand):
            # Hands involving pairs, trips, and quads have to be 
            # compared by highest groups downward. Two full houses
            # for example are compared by higher trip, then higher
            # pair.
            p1cardnums = [i[0] for i in p1_hand]
            compcardnums = [i[0] for i in p2_hand]
            high = max(set(p1cardnums), key = p1cardnums.count)
            comphigh = max(set(compcardnums), key = compcardnums.count)
            highp1 = int(faceconvert(high))
            highcomp = int(faceconvert(comphigh))
            if highp1 > highcomp:
                print("You win!")
                return
            elif highp1 < highcomp:
                print("You lose :(")
                return
    p1cardvals = list()
    p1cardnums = [i[0] for i in p1_hand]
    for num in p1cardnums:
        p1cardvals.append(int(faceconvert(num)))
    p1high = max(p1cardvals)
    p2cardvals = list()
    p2cardnums = [i[0] for i in p2_hand]
    for num in p2cardnums:
        p2cardvals.append(int(faceconvert(num)))
    p2high = max(p2cardvals)
    if p1high == p2high:
        while p1high == p2high and len(p1cardvals) > 1:
            # Goes down the line of cards until it finds a
            # non-match. If all card ranks match, a tie is
            # declared.
            p1cardvals.remove(max(p1cardvals))
            p2cardvals.remove(max(p2cardvals))
            p1high = max(p1cardvals)
            p2high = max(p2cardvals)
    if p1high > p2high:
        print("You win!")
    elif p2high > p1high:
        print("You lose :(")
    else:
        print("Tie!")

def removedealt(deckstate):
    """Removes cards from the deck as they are being dealt
    
    Args:
        deckstate - list of cards in the deck
    """
    i = 0
    while i < 5:
        deckstate.pop()
        i += 1

def main():
    """Main method that runs the poker game
    
    Side effects:
    Deals player hands
    Prompts user for input and prints to terminal
    """
    print("\nLet's Play\n")
    
    random.shuffle(deckstate)
    p1hand = deckstate[-5:]
    removedealt(deckstate)
    computerhand = deckstate[-5:]
    removedealt(deckstate)
    
    removedealt(deckstate)
    p1 = Player(p1hand)
    computer = Player(computerhand)
    
    print(f"Your Hand: {p1.hand}")
    turn(p1, computer, deckstate)
    
    print("Your Hand:")
    for card in p1.hand:
        print(card)
    print("The Computer's Hand:")
    for card in computer.hand:
        print(card)
    
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
