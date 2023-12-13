def encode_hand(hand, jokers=False):
    face_encoding = {"A": 13, "K": 12, "Q": 11, "J": 1, "T": 10} if jokers else {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    return [int(card) if card.isnumeric() else face_encoding[card] for card in list(hand)]

def get_value(hand, jokers=False):
    value = 0
    base = 14 if jokers else 15
    multiplier = base ** 4
    for card in hand:
        value += card * multiplier
        multiplier /= base
    return int(value)

def get_hand_type(hand, j_is_joker=False):
    # track the counts of each card other than jokers separately from the jokers
    cards = {}
    jokers = 0
    for card in hand:
        if card == "J" and j_is_joker:
            jokers += 1
        else:
            cards[card] = cards.get(card, 0) + 1
    # if we have four or five jokers, automatically five of a kind so we can return right away
    if j_is_joker:
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

def categorize_hand(hand_and_bid, hand_types, jokers=False):
    hand, bid = hand_and_bid
    hand_encoded = encode_hand(hand, jokers)
    value = get_value(hand_encoded, jokers)
    hand_obj = [hand, hand_encoded, value, bid]
    hand_type = get_hand_type(hand, jokers)
    hand_types[hand_type].append(hand_obj)
    
hand_types_p1 = {"five_of_kind": [], "four_of_kind": [], "full_house": [], "three_of_kind": [], "two_pairs": [], "one_pair": [], "high_card": []}
hand_types_p2 = {"five_of_kind": [], "four_of_kind": [], "full_house": [], "three_of_kind": [], "two_pairs": [], "one_pair": [], "high_card": []}

for line in open("input.txt").read().split("\n"):
    hand_and_bid = line.split()
    categorize_hand(hand_and_bid, hand_types_p1)
    categorize_hand(hand_and_bid, hand_types_p2, True)

# now sort by card rank within categories
for hand_list in hand_types_p1:
    hand_types_p1[hand_list].sort(key = lambda x: x[2])

for hand_list in hand_types_p2:
    hand_types_p2[hand_list].sort(key = lambda x: x[2])

p1 = 0
rank = 1
# lowest rank cards to highest
for hand_type in reversed(hand_types_p1.values()):
    for hand in hand_type:
        p1 += rank * int(hand[3])
        rank += 1
p2 = 0
rank = 1
# lowest rank cards to highest
for hand_type in reversed(hand_types_p2.values()):
    for hand in hand_type:
        p2 += rank * int(hand[3])
        rank += 1

print("part 1: {}\npart 2: {}".format(p1, p2))



    