def get_north_load_after_north_tilt(rocks):
    rocks = rocks.split("\n")
    load = 0
    for j in range(len(rocks[0])):
        weight = len(rocks)
        for i in range(len(rocks)):
            if rocks[i][j] == "O":
                load += weight
                weight -= 1
            elif rocks[i][j] == "#":
                weight = len(rocks) - i - 1
    return load

def get_north_load(rocks):
    rocks = rocks.split("\n")
    load = 0
    for i in range(len(rocks)):
        for j in range(len(rocks)):
            if rocks[i][j] == "O":
                load += len(rocks) - i
    return load

def tilt_north(rocks):
    rocks = [list(row) for row in rocks.split("\n")]
    for j in range(len(rocks[0])):
        new_row = 0
        for i in range(len(rocks)):
            if rocks[i][j] == "O":
                if new_row != i:
                    rocks[i][j] = "."
                    rocks[new_row][j] = "O"
                new_row += 1
            elif rocks[i][j] == "#":
                new_row = i + 1
    return "\n".join(["".join(row) for row in rocks])

def tilt_south(rocks):
    rocks = [list(row) for row in rocks.split("\n")]
    for j in range(len(rocks[0])):
        new_row = len(rocks) - 1
        for i in range(len(rocks) -1, -1, -1):
            if rocks[i][j] == "O":
                if new_row != i:
                    rocks[i][j] = "."
                    rocks[new_row][j] = "O"
                new_row -= 1
            elif rocks[i][j] == "#":
                new_row = i - 1
    return "\n".join(["".join(row) for row in rocks])

def tilt_west(rocks):
    rocks = [list(row) for row in rocks.split("\n")]
    for i in range(len(rocks)):
        new_col = 0
        for j in range(len(rocks[0])):
            if rocks[i][j] == "O":
                if new_col != j:
                    rocks[i][j] = "."
                    rocks[i][new_col] = "O"
                new_col += 1
            elif rocks[i][j] == "#":
                new_col = j + 1
    return "\n".join(["".join(row) for row in rocks])

def tilt_east(rocks):
    rocks = [list(row) for row in rocks.split("\n")]
    for i in range(len(rocks)):
        new_col = len(rocks[0]) - 1
        for j in range(len(rocks[0]) -1, -1, -1):
            if rocks[i][j] == "O":
                if new_col != j:
                    rocks[i][j] = "."
                    rocks[i][new_col] = "O"
                new_col -= 1
            elif rocks[i][j] == "#":
                new_col = j - 1
    return "\n".join(["".join(row) for row in rocks])

def cycle(rocks):
    rocks = tilt_north(rocks)
    rocks = tilt_west(rocks)
    rocks = tilt_south(rocks)
    rocks = tilt_east(rocks)
    return rocks

rocks = open("input.txt").read()

p1 = get_north_load_after_north_tilt(rocks)
rock_patterns = {} # mapping of all rock patterns (as strings) to the idx at which they were reached
loads = [] # list of north load values at every idx

for i in range(1_000_000_000):
    rocks = cycle(rocks)
    if i % 10_000_000 == 0:
        print(i)

p2 = get_north_load(rocks)


cycle_idx = 0
while rocks not in rock_patterns:
    loads.append(get_north_load(rocks))
    rock_patterns[rocks] = cycle_idx
    rocks = cycle(rocks)
    cycle_idx += 1

loop_start = rock_patterns[rocks]
loop_length = len(rock_patterns) - loop_start
offset = (1_000_000_000 - loop_start) % loop_length

p2 = loads[loop_start + offset]

print("part 1: {}\npart 2: {}".format(p1, p2))



