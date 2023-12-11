with open("input.txt", "r") as file:
    grid = [list(line) for line in file.read().split("\n")]

for row in range(len(grid)):
    for column in range(len(grid[row])):
        if grid[row][column] == 'S':
            starting_row = row
            starting_column = column
            break
    else:
        continue
    break

check_pipes = [(starting_row, starting_column)]
seen_pipes = {(starting_row, starting_column)}
potential_s = {'|', '-', 'L', 'J', '7', 'F'}

while len(check_pipes) > 0:
    row, column = check_pipes.pop(0)
    current_pipe = grid[row][column]

    if row > 0 and current_pipe in "S|LJ" and grid[row - 1][column] in "|7F" and (row - 1, column) not in seen_pipes:
        seen_pipes.add((row - 1, column))
        check_pipes.append((row - 1, column))
        if current_pipe == 'S':
            potential_s = potential_s.intersection({'|', 'L', 'J'})

    if row < len(grid) - 1 and current_pipe in "S|7F" and grid[row + 1][column] in "|LJ" and (row + 1, column) not in seen_pipes:
        seen_pipes.add((row + 1, column))
        check_pipes.append((row + 1, column))
        if current_pipe == 'S':
            potential_s = potential_s.intersection({'|', '7', 'F'})

    if column > 0 and current_pipe in "S-7J" and grid[row][column - 1] in "-LF" and (row, column - 1) not in seen_pipes:
        seen_pipes.add((row, column - 1))
        check_pipes.append((row, column - 1))
        if current_pipe == 'S':
            potential_s = potential_s.intersection({'-', '7', 'J'})

    if column < len(grid[row]) - 1 and current_pipe in "S-LF" and grid[row][column + 1] in "-J7" and (row, column + 1) not in seen_pipes:
        seen_pipes.add((row, column + 1))
        check_pipes.append((row, column + 1))
        if current_pipe == 'S':
            potential_s = potential_s.intersection({'-', 'L', 'F'})

s_pipe = potential_s.pop()
grid[starting_row][starting_column] = s_pipe

grid = [['.' if (row, column) not in seen_pipes else grid[row][column]
         for column in range(len(grid[row]))] for row in range(len(grid))]


interior = 0
for row in grid:
    for i, char in enumerate(row):
        if char != ".":
            continue

        intersect = 0
        corner_pipes = []
        for j in range(i + 1, len(row)):
            if row[j] in "|":
                intersect += 1
            if row[j] in "FL":
                corner_pipes.append(row[j])
            if len(corner_pipes) != 0 and row[j] == "J" and corner_pipes[-1] == "F" or row[j] == "7" and corner_pipes[-1] == "L":
                corner_pipes.pop(-1)
                intersect += 1

        if intersect % 2 == 1:
            interior += 1

print(interior)