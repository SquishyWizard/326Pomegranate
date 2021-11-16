def scoring(p1_cards, p2_cards):
    """Determines the victor based on the cards from both hands
    
    Args:
    p1_cards (list): the first player's hand
    p2_cards (list): the second player's hand
    
    Side Effects:
    multiple counter variables are created, set to zero,
    and adjusted in value based on several conditional statements
    """
    
    #counter variables for flush scenario
    p1_club_ctr = 0
    p1_heart_ctr = 0
    p1_spade_ctr = 0
    p1_diamond_ctr = 0
    p2_club_ctr = 0
    p2_heart_ctr = 0
    p2_spade_ctr = 0
    p2_diamond_ctr = 0
    
    for card in p1_cards:
        if (len(card) == 3):
            if (card[2] == "C"):
                p1_club_ctr += 1
            elif (card[2] == "H"):
                p1_heart_ctr += 1
            elif (card[2] == "S"):
                p1_spade_ctr += 1
            else:
                p1_diamond_ctr += 1
        else:
            if (card[1] == "C"):
                p1_club_ctr += 1
            elif (card[1] == "H"):
                p1_heart_ctr += 1
            elif (card[1] == "S"):
                p1_spade_ctr += 1
            else:
                p1_diamond_ctr += 1
    for card in p2_cards:
        if (len(card) == 3):
            if (card[2] == "C"):
                p2_club_ctr += 1
            elif (card[2] == "H"):
                p2_heart_ctr += 1
            elif (card[2] == "S"):
                p2_spade_ctr += 1
            else:
                p2_diamond_ctr += 1
        else:
            if (card[1] == "C"):
                p2_club_ctr += 1
            elif (card[1] == "H"):
                p2_heart_ctr += 1
            elif (card[1] == "S"):
                p2_spade_ctr += 1
            else:
                p2_diamond_ctr += 1
    
    #Checks if player or opponent won via flush
    if (p1_club_ctr == 5 or p1_diamond_ctr == 5
        or p1_heart_ctr == 5 or p1_spade_ctr == 5):
        if (p2_club_ctr == 5 or p2_diamond_ctr == 5
            or p2_heart_ctr == 5 or p2_spade_ctr == 5):
            print("The match is a draw")
        else:
            print("Player wins")
    else:
        if (p2_club_ctr == 5 or p2_diamond_ctr == 5
            or p2_heart_ctr == 5 or p2_spade_ctr == 5):
            print("Opponent wins")
    
    p1_num_aces = 0
    p1_num_2s = 0
    p1_num_3s = 0
    p1_num_4s = 0
    p1_num_5s = 0
    p1_num_6s = 0
    p1_num_7s = 0
    p1_num_8s = 0
    p1_num_9s = 0
    p1_num_10s = 0
    p1_num_jacks = 0
    p1_num_queens = 0
    p1_num_kings = 0
    p2_num_aces = 0
    p2_num_2s = 0
    p2_num_3s = 0
    p2_num_4s = 0
    p2_num_5s = 0
    p2_num_6s = 0
    p2_num_7s = 0
    p2_num_8s = 0
    p2_num_9s = 0
    p2_num_10s = 0
    p2_num_jacks = 0
    p2_num_queens = 0
    p2_num_kings = 0
    
    for card in p1_cards:
        if (card[0] == "A"):
            p1_num_aces += 1
        elif (card[0] == "2"):
            p1_num_2s += 1
        elif (card[0] == "3"):
            p1_num_3s += 1
        elif (card[0] == "4"):
            p1_num_4s += 1
        elif (card[0] == "5"):
            p1_num_5s += 1
        elif (card[0] == "6"):
            p1_num_6s += 1
        elif (card[0] == "7"):
            p1_num_7s += 1
        elif (card[0] == "8"):
            p1_num_8s += 1
        elif (card[0] == "9"):
            p1_num_9s += 1
        elif (card[0] == "1"):
            p1_num_10s += 1
        elif (card[0] == "J"):
            p1_num_jacks += 1
        elif (card[0] == "Q"):
            p1_num_queens += 1
        elif (card[0] == "K"):
            p1_num_kings += 1
        else:
            pass
    for card in p2_cards:
        if (card[0] == "A"):
            p2_num_aces += 1
        elif (card[0] == "2"):
            p2_num_2s += 1
        elif (card[0] == "3"):
            p2_num_3s += 1
        elif (card[0] == "4"):
            p2_num_4s += 1
        elif (card[0] == "5"):
            p2_num_5s += 1
        elif (card[0] == "6"):
            p2_num_6s += 1
        elif (card[0] == "7"):
            p2_num_7s += 1
        elif (card[0] == "8"):
            p2_num_8s += 1
        elif (card[0] == "9"):
            p2_num_9s += 1
        elif (card[0] == "1"):
            p2_num_10s += 1
        elif (card[0] == "J"):
            p2_num_jacks += 1
        elif (card[0] == "Q"):
            p2_num_queens += 1
        elif (card[0] == "K"):
            p2_num_kings += 1
        else:
            pass
    
    p1_has_pair = False
    p1_has_twopair = False
    p1_has_3ofakind = False
    p1_has_straight = False
    p1_has_fullhouse = False
    p1_has_4ofakind = False
    p1_has_5ofakind = False
    p2_has_pair = False
    p2_has_twopair = False
    p2_has_3ofakind = False
    p2_has_straight = False
    p2_has_fullhouse = False
    p2_has_4ofakind = False
    p2_has_5ofakind = False
            
    if (p1_num_aces == 2 or p1_num_2s == 2 or p1_num_3s
        or p1_num_4s == 2 or p1_num_5s == 2 or p1_num_6s == 2
        or p1_num_7s == 2 or p1_num_8s == 2 or p1_num_9s == 2
        or p1_num_10s == 2 or p1_num_jacks == 2 
        or p1_num_queens == 2 or p1_num_kings == 2):
            p1_has_pair = True
    if (p1_num_aces == 3 or p1_num_2s == 3 or p1_num_3s
        or p1_num_4s == 3 or p1_num_5s == 3 or p1_num_6s == 3
        or p1_num_7s == 3 or p1_num_8s == 3 or p1_num_9s == 3
        or p1_num_10s == 3 or p1_num_jacks == 3 
        or p1_num_queens == 3 or p1_num_kings == 3):
            p1_has_3ofakind = True
    if (p1_num_aces == 4 or p1_num_2s == 4 or p1_num_3s
        or p1_num_4s == 4 or p1_num_5s == 4 or p1_num_6s == 4
        or p1_num_7s == 4 or p1_num_8s == 4 or p1_num_9s == 4
        or p1_num_10s == 4 or p1_num_jacks == 4 
        or p1_num_queens == 4 or p1_num_kings == 4):
            p1_has_4ofakind = True
    if (p1_num_aces == 5 or p1_num_2s == 5 or p1_num_3s
        or p1_num_4s == 5 or p1_num_5s == 5 or p1_num_6s == 5
        or p1_num_7s == 5 or p1_num_8s == 5 or p1_num_9s == 5
        or p1_num_10s == 5 or p1_num_jacks == 5 
        or p1_num_queens == 5 or p1_num_kings == 5):
            p1_has_5ofakind = True
    if (p2_num_aces == 2 or p2_num_2s == 2 or p2_num_3s
        or p2_num_4s == 2 or p2_num_5s == 2 or p2_num_6s == 2
        or p2_num_7s == 2 or p2_num_8s == 2 or p2_num_9s == 2
        or p2_num_10s == 2 or p2_num_jacks == 2 
        or p2_num_queens == 2 or p2_num_kings == 2):
            p2_has_pair = True
    if (p2_num_aces == 3 or p2_num_2s == 3 or p2_num_3s
        or p2_num_4s == 3 or p2_num_5s == 3 or p2_num_6s == 3
        or p2_num_7s == 3 or p2_num_8s == 3 or p2_num_9s == 3
        or p2_num_10s == 3 or p2_num_jacks == 3 
        or p2_num_queens == 3 or p2_num_kings == 3):
            p2_has_3ofakind = True
    if (p2_num_aces == 4 or p2_num_2s == 4 or p2_num_3s
        or p2_num_4s == 4 or p2_num_5s == 4 or p2_num_6s == 4
        or p2_num_7s == 4 or p2_num_8s == 4 or p2_num_9s == 4
        or p2_num_10s == 4 or p2_num_jacks == 4 
        or p2_num_queens == 4 or p2_num_kings == 4):
            p2_has_4ofakind = True
    if (p2_num_aces == 5 or p2_num_2s == 5 or p2_num_3s
        or p2_num_4s == 5 or p2_num_5s == 5 or p2_num_6s == 5
        or p2_num_7s == 5 or p2_num_8s == 5 or p2_num_9s == 5
        or p2_num_10s == 5 or p2_num_jacks == 5 
        or p2_num_queens == 5 or p2_num_kings == 5):
            p2_has_5ofakind = True