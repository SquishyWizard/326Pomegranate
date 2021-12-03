def scoring(p1_cards, p2_cards):
    """Determines the victor based on the cards from both hands
    
    Args:
    p1_cards (list): the first player's hand
    p2_cards (list): the second player's hand
    
    Side Effects:
    multiple counter variables are created, set to zero,
    and adjusted in value based on several conditional statements
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
        
def haspair(cards):
    """Checks for a pair"""