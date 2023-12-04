res = 0
with open("dec4_input.txt", "r") as text:
    data = text.readlines()
    game = 1
    for card in data:
        card = card.replace("\n", "")
        score = 0
        cardInfo = card.split(":")[1].split("|")
        winning_dirty = cardInfo[0].split(" ")
        winning = set()
        for entry in winning_dirty:
            if entry.isnumeric():
                winning.add(entry)
        myNums_dirty = cardInfo[1].split(" ")
        myNums = []
        myWinning = []
        for entry in myNums_dirty:
            if entry.isnumeric():
                myNums.append(entry)
        for entry in myNums:
            if entry in winning:
                myWinning.append(entry)
                if score == 0:
                    score = 1
                else:
                    score *= 2
        print("winning numbers: ")
        print(winning)
        print("my numbers: ")
        print(myNums)
        print("my winning numbers: ")
        print(myWinning)
        print("card score: " + str(score))      
        game += 1  
        res += score
print(res)
        