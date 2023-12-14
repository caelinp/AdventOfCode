
def get_north_load(rocks):
    load = 0
    for j in range(len(rocks[0])):
        weight = len(rocks)
        for i in range(len(rocks)):
            if rocks[i][j] == "O":
                load += weight
                weight -= 1
            elif rocks[i][j] == "#":
                weight = len(rocks) - i - 1

def tilt_north(rocks):
    for j in range(len(rocks[0])):
        new_row = 0
        for i in range(len(rocks)):
            if rocks[i][j] == "O":
                rocks[i][j] = "."
                rocks[new_row][j] = "O"
                new_row += 1
            elif rocks[i][j] == "#":
                new_row = i + 1

def tilt_south(rocks):
    for j in range(len(rocks[0])):
        new_row = len(rocks) - 1
        for i in range(len(rocks) - 1, -1, -1):
            if rocks[i][j] == "O":
                rocks[i][j] = "."
                rocks[new_row][j] = "O"
                new_row -= 1
            elif rocks[i][j] == "#":
                new_row = i - 1

def tilt_west(rocks):
    for i in range(len(rocks)):
        new_col = 0
        for j in range(len(rocks[0])):
            if rocks[i][j] == "O":
                rocks[i][j] = "."
                rocks[i][new_col] = "O"
                new_col += 1
            elif rocks[i][j] == "#":
                new_col = j + 1

def tilt_east(rocks):
    for i in range(len(rocks)):
        new_col = len(rocks[0]) - 1
        for j in range(len(rocks[0]) -1, -1, -1):
            if rocks[i][j] == "O":
                rocks[i][j] = "."
                rocks[i][new_col] = "O"
                new_col -= 1
            elif rocks[i][j] == "#":
                new_col = i - 1
def cycle(rocks):
    tilt_north(rocks)
    tilt_west(rocks)
    tilt_south(rocks)
    tilt_east(rocks)
rocks = [[rock for rock in row] for row in open("example_input.txt").read().split("\n")]

print(get_north_load(rocks))

cycle(rocks)
for row in rocks:
    print("".join(row))

