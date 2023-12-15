hand_values = {"R": 1, "P": 2, "S": 3}
hand_mapping_me = {"X": "R", "Y": "P", "Z": "S"}
symbol_mapping_me = {"R": "X", "P": "Y", "S": "Z"}
hand_mapping_opp = {"A": "R", "B": "P", "C": "S"}
win_to_lose = {"R": "S", "S": "P", "P": "R"}
lose_to_win = {"S": "R", "P": "S", "R": "P"}
p1, p2 = 0, 0
for game in open("input.txt").read().split("\n"):
    game = game.split()
    p1 += hand_values[hand_mapping_me[game[1]]]
    p1 += 3 * (hand_mapping_opp[game[0]] == hand_mapping_me[game[1]])
    p1 += 6 * (win_to_lose[hand_mapping_me[game[1]]] == hand_mapping_opp[game[0]])
    
    p2 += (game[1] == "X") * (hand_values[win_to_lose[hand_mapping_opp[game[0]]]])
    p2 += (game[1] == "Y") * (hand_values[hand_mapping_opp[game[0]]] + 3)
    p2 += (game[1] == "Z") * (hand_values[lose_to_win[hand_mapping_opp[game[0]]]] + 6)

print("part 1: {}\npart 2: {}".format(p1, p2))
