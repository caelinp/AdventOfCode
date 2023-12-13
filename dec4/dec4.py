p1 = 0
match_map = {}
for i, card in enumerate(open("input.txt").read().split("\n")):
    winning, my_nums = [nums.split() for nums in card.split(":")[1].split("|")]
    score = 0
    matches = 0
    for entry in my_nums:
        score, matches = ((1 if score == 0 else score * 2), matches + 1) if entry in winning else (score, matches)
    match_map[i + 1] = matches
    p1 += score
p2 = 0
copies = {i : 1 for i in match_map}
for game in match_map:
    for i in range(match_map[game]):
        copies[game + i + 1] += copies[game]
    p2 += copies[game]
print("part 1: {}\npart 2: {}".format(p1, p2))