input_file = "dec7_input.txt"
hand_types = {"five_of_kind": [], "four_of_kind": [], "full_house": [], "three_of_kind": [], "two_pairs": [], "one_pair": [], "high_card": []}

def encode_hand(hand):
    hand = list(hand)
    hand_encoded = []
    for card in hand:
        if card == "A":
            hand_encoded.append(13)
        elif card == "K":
            hand_encoded.append(12)
        elif card == "Q":
            hand_encoded.append(11)
        elif card == "J":
            hand_encoded.append(1)
        elif card == "T":
            hand_encoded.append(10)
        else:
            hand_encoded.append(int(card))
    return hand_encoded

def get_value(hand):
    value = 0
    multiplier = 10000000000
    for card in hand:
        value += card * multiplier
        multiplier /= 100
    return int(value)

def get_hand_type(hand):
    # track the counts of each card other than jokers separately from the jokers
    cards = {}
    jokers = 0
    for card in hand:
        if card == "J":
            jokers += 1
        else:
            cards[card] = cards.get(card, 0) + 1

    # if we have four or five jokers, automatically five of a kind so we can return right away
    if jokers == 4 or jokers == 5:
        return "five_of_kind"
    
    threeCards = False
    onePair = False
    for card in cards:
        # check for five of kind
        if cards[card] + jokers == 5:
            return "five_of_kind"
        # check for four of kind
        elif cards[card] + jokers == 4:
            return "four_of_kind"
        elif cards[card] == 3:
            threeCards = True
        elif cards[card] == 2:
            # if onePair was already set, then we have detected two pairs, so we know the hand type
            if onePair:
                # one joker turns two pairs into a full house
                if jokers == 1:
                    return "full_house"
                else:
                    return "two_pairs"
            onePair = True
    
    # full house
    if threeCards and onePair:
        return "full_house"

    # three of kind
    elif threeCards:
        return "three_of_kind"
    
    # one pair
    elif onePair:
        # we can turn a pair into a triplet with one joker
        if jokers == 1:
            return "three_of_kind"
        return "one_pair"
    
    # with two jokers we can turn any high card into a three of kind
    elif jokers == 2:
        return "three_of_kind"
    
    # with one joker we can turn any high card into a one pair
    elif jokers == 1:
        return "one_pair"
    
    # else it's just a high card
    else:
        return "high_card"

def categorize_hand(hand_and_bid):
    hand, bid = hand_and_bid
    hand_encoded = encode_hand(hand)
    value = get_value(hand_encoded)
    hand_obj = [hand, hand_encoded, value, bid]
    hand_type = get_hand_type(hand)
    hand_types[hand_type].append(hand_obj)
    
with open(input_file, "r") as text:
    data = text.read().split("\n")
    for line in data:
        hand_and_bid = line.split()
        categorize_hand(hand_and_bid)
    

    # now sort by card rank within categories
    for hand_list in hand_types:
        hand_types[hand_list].sort(key = lambda x: x[2])

    score = 0
    rank = 1
    # lowest rank cards to highest
    for hand in hand_types["high_card"]:
        score += rank * int(hand[3])
        rank += 1

    for hand in hand_types["one_pair"]:
        score += rank * int(hand[3])
        rank += 1
    
    for hand in hand_types["two_pairs"]:
        score += rank * int(hand[3])
        rank += 1
    
    for hand in hand_types["three_of_kind"]:
        score += rank * int(hand[3])
        rank += 1

    for hand in hand_types["full_house"]:
        score += rank * int(hand[3])
        rank += 1
    
    for hand in hand_types["four_of_kind"]:
        score += rank * int(hand[3])
        rank += 1
    
    for hand in hand_types["five_of_kind"]:
        score += rank * int(hand[3])
        rank += 1
    
    print(score)


    