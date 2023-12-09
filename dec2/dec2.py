res = [0, 0]
amounts = {"red": 12, "green": 13, "blue": 14}
for line in open("input.txt").read().split("\n"):
    # part 1: summing IDs of valid games
    game_num, round_amounts = line.split("Game")[1].split(":")
    valid = True
    for round in round_amounts.split(";"):
        for color in round.split(","):
            amount, color = color.split(" ")[1:]
            if not (valid := not int(amount) > amounts[color]):
                break
        if not valid:
            break
    res[0] += valid * int(game_num)

    # part 2: summing powers of minimum amounts of colors per game:
    min_amounts = {"red": 0, "green": 0, "blue": 0}
    for round in round_amounts.split(";"):
        for color in round.split(","):
            amount, color = color.split(" ")[1:]
            min_amounts[color] = max(min_amounts[color], int(amount))
    power = 1
    for color in min_amounts:
        power *= min_amounts[color]
    res[1] += power
print("part 1: {}, part 2: {}".format(*res))
