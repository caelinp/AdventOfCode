res = 0
with open("game_input.txt", "r") as text:
    data = text.readlines()
    for line in data:
        gameInfo = line.split("Game")[1].split(":")
        gameNum = gameInfo[0]
        roundAmounts = gameInfo[1].split(";")

        valid = True
        '''print("Game number: " + gameNum)'''
        amounts = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for round in roundAmounts:
            colorAmounts = round.split(",")
            '''print("round: ")
            print(colorAmounts)'''
            for color in colorAmounts:
                amount, color = color.split(" ")[1:]
                color = color.replace("\n", "")
                #print("amounts: ")
                #print(amounts)
                amounts[color] = max(amounts[color], int(amount))
        power = 1
        for color in amounts:
            power *= amounts[color]
        res += power

print(res)
