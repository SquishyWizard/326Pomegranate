def scoring(p1_cards, p2_cards):
    """Determines the victor based on the cards from both hands
    
    Args:
    p1_cards (list): the first player's hand
    p2_cards (list): the second player's hand
    
    Side Effects:
    multiple lists are created to hold the values and suites 
    of each player's cards
    boolean values are created to check what kind of a hand each player has
    """
    p1_num_list = list()
    p1_suite_list = list()
    p2_num_list = list()
    p2_suite_list = list()
    
    for card in p1_cards:
        number, suite = card.split()
        p1_num_list.append(number)
        p1_suite_list.append(suite)
    
    for card in p2_cards:
        number, suite = card.split()
        p2_num_list.append(number)
        p2_suite_list.append(suite)
    
    p1haspair = haspair(p1_num_list)
    p1hastwopair = hastwopair(p1_num_list)
    p1has3ofakind = has3ofakind(p1_num_list)
    p1hasstraight = hasstraight(p1_num_list)
    p1hasflush = hasflush(p1_suite_list)
    p1hasfullhouse = hasfullhouse(p1_num_list)
    
    p2haspair = haspair(p2_num_list)
    p2hastwopair = hastwopair(p2_num_list)
    p2has3ofakind = has3ofakind(p2_num_list)
    p2hasstraight = hasstraight(p2_num_list)
    p2hasflush = hasflush(p2_suite_list)
    p2hasfullhouse = hasfullhouse(p2_num_list)
        
def haspair(cards):
    """Checks for a pair"""
    for card in cards:
        currentcard = cards.pop(card)
        if currentcard in cards:
            return True

def hastwopair(cards):
    """Checks for a two pair"""

def has3ofakind(cards):
    """Checks for a 3 of a kind"""
    samecard = 1
    for card in cards:
        currentcard = cards.pop(card)
        
    
def hasstraight(cards):
    """Checks for a straight"""
    for card in cards:
        lowvalue = card
    
    
def hasflush(cards):
    """ Checks to see if this hand contains a flush
    
    Args:
        cards(list of str): the player's hand
    
    Returns:
        flush: boolean stating whether this player has flush
    """
    #counter variables for flush scenario
    p1_club_ctr = 0
    p1_heart_ctr = 0
    p1_spade_ctr = 0
    p1_diamond_ctr = 0
    
    for card in cards:
        number, suite = cards[card].split()

def hasfullhouse(cards):
    """Checks for a full house"""
    if haspair(cards) == True:
        if has3ofakind(cards) == True:
            return True
        else:
            return False
    else:
        return False