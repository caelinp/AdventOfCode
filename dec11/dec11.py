def get_empty_rows_and_cols(universe):
    empty_rows, empty_cols = [], []
    for i, row in enumerate(universe):
        if '#' not in row:
            empty_rows.append(i)

    for j in range(len(universe[0])):
        col_is_empty = True
        for i in range(len(universe)):
            if (universe[i][j] == '#'):
                col_is_empty = False
                break
        if col_is_empty:
            empty_cols.append(j)

    return empty_rows, empty_cols

def get_distance(g1, g2, empty_rows, empty_cols, multiplier):
    row_start, row_end = sorted([g1[0], g2[0]])
    col_start, col_end = sorted([g1[1], g2[1]])
    empty_rows_in_range = 0
    empty_cols_in_range = 0

    for row in empty_rows:
        if row_start < row < row_end:
            empty_rows_in_range += 1

    for col in empty_cols:
      if col_start < col < col_end:
         empty_cols_in_range += 1
    
    row_diff = row_end - row_start + (multiplier - 1) * empty_rows_in_range
    col_diff = col_end - col_start + (multiplier - 1) * empty_cols_in_range
    return row_diff + col_diff

def get_galaxies(universe):
    galaxies = []
    for row in range(len(universe)):
        for col in range(len(universe[0])):
            if universe[row][col] == '#':
                galaxies.append((row, col))
    return galaxies

def sum_distances(galaxies, empty_rows, empty_cols, multiplier):
    distances = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            distances += get_distance(galaxies[i], galaxies[j], empty_rows, empty_cols, multiplier)
    return distances

universe = [list(line) for line in open("input.txt").read().split("\n")]
empty_rows, empty_cols = get_empty_rows_and_cols(universe)

galaxies = get_galaxies(universe)

p1_mult = 2
p2_mult = 1000000

distances = (sum_distances(galaxies, empty_rows, empty_cols, p1_mult), sum_distances(galaxies, empty_rows, empty_cols, p2_mult))
print("part 1: {}\npart 2: {}".format(*distances))