hand_types = {"five_of_kind": [], "four_of_kind": [], "full_house": [], "three_of_kind": [], "two_pairs": [], "one_pair": [], "high_card": []}

def encode_hand(hand, jokers=False):
    face_encoding = {"A": 13, "K": 12, "Q": 11, "J": 1, "T": 10} if jokers else {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    return [int(card) if card.isnumeric() else face_encoding[card] for card in list(hand)]

def get_value_jokers(hand):
    value = 0
    multiplier = 14*14*14*14
    for card in hand:
        value += card * multiplier
        multiplier /= 14
    return int(value)

def get_hand_type(hand, jokers=False):
    if jokers:
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
        
        cards[max(cards, key=cards.get)] += jokers

    three_cards = one_pair= False
    for card in cards:
        # check for five of kind
        if cards[card] == 5:
            return "five_of_kind"
        # check for four of kind
        if cards[card] == 4:
            return "four_of_kind"
        if cards[card] == 3:
            three_cards = True
        if cards[card] == 2:
            if one_pair:
                return "two_pairs"
            one_pair = True

    if three_cards and one_pair:
        return "full_house"
    elif three_cards:
        return "three_of_kind"
    elif one_pair:
        return "one_pair"
    else:
        return "high_card"

def categorize_hand(hand_and_bid, jokers=False):
    hand, bid = hand_and_bid
    hand_encoded = encode_hand(hand, True)
    value = get_value_jokers(hand_encoded)
    hand_obj = [hand, hand_encoded, value, bid]
    hand_type = get_hand_type(hand, jokers)
    hand_types[hand_type].append(hand_obj)
    

for line in open("input.txt").read().split("\n"):
    hand_and_bid = line.split()
    categorize_hand(hand_and_bid, True)

# now sort by card rank within categories
for hand_list in hand_types:
    hand_types[hand_list].sort(key = lambda x: x[2])

score = 0
rank = 1
# lowest rank cards to highest
for hand_type in reversed(hand_types.values()):
    for hand in hand_type:
        score += rank * int(hand[3])
        rank += 1
print(score)


    