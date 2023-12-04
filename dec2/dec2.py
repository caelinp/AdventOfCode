res = 0
amounts = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
with open("game_input.txt", "r") as text:
    data = text.readlines()
    for line in data:
        gameInfo = line.split("Game")[1].split(":")
        gameNum = gameInfo[0]
        roundAmounts = gameInfo[1].split(";")

        valid = True
        '''print("Game number: " + gameNum)'''
        for round in roundAmounts:
            colorAmounts = round.split(",")
            '''print("round: ")
            print(colorAmounts)'''
            for color in colorAmounts:
                amount, color = color.split(" ")[1:]
                color = color.replace("\n", "")
                #print("amounts: ")
                #print(amounts)
                if int(amount) > amounts[color]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            print(gameNum + "is valid")
            res += int(gameNum)
        else:
            print(gameNum + "invalid")
    print(res)
