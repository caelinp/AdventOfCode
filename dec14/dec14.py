from functools import cache

@cache
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

@cache 
def get_north_load(rocks):
    rocks = rocks.split("\n")
    load = 0
    for i in range(len(rocks)):
        for j in range(len(rocks)):
            if rocks[i][j] == "O":
                load += len(rocks) - i
    return load

@cache
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

@cache
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

@cache
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

@cache
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

@cache
def cycle(rocks):
    rocks = tilt_north(rocks)
    rocks = tilt_west(rocks)
    rocks = tilt_south(rocks)
    rocks = tilt_east(rocks)
    return rocks

rocks = open("input.txt").read()

p1 = get_north_load_after_north_tilt(rocks)
p2 = 0
loads = []
history = {}
for i in range(300):
    rocks = cycle(rocks)
    loads.append(get_north_load(rocks))

    # check for repetition cycle
    if i > 20:
        state_hash = str(loads[-20:])
        if state_hash in history:
            rep_cycle_start = history[state_hash]
            rep_cycle_length = i - rep_cycle_start
            break
        history[state_hash] = i

target = 1_000_000_000
offset = (target - rep_cycle_start) % rep_cycle_length - 1  # -1 because initial load was not recorded 
p2 = loads[rep_cycle_start + offset]

print("part 1: {}\npart 2: {}".format(p1, p2))



