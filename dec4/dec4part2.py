matchMap = {}
copies = {}
with open("dec4_input.txt", "r") as text:
    data = text.readlines()
    for card in data:
        card = card.replace("\n", "").split(":")
        cardNum = card[0].replace("Card ", "").replace(" ", "")
        cardInfo = card[1].split("|")
        winning_dirty = cardInfo[0].split(" ")
        winning = set()
        for entry in winning_dirty:
            if entry.isnumeric():
                winning.add(entry)
        myNums_dirty = cardInfo[1].split(" ")
        myNums = []
        matches = 0
        for entry in myNums_dirty:
            if entry.isnumeric():
                myNums.append(entry)
        for entry in myNums:
            if entry in winning:
                matches += 1
        matchMap[cardNum] = matches

    for game in matchMap:
        copies[int(game)] = 1
    cards = 0
    for game in matchMap:
        games_ahead = matchMap[game]
        for i in range(games_ahead):
            copies[int(game) + i + 1] += copies[int(game)]
        cards += copies[int(game)]
        
    
    print(cards)
        
        