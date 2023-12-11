def get_empty_rows_and_cols(universe):
    empty_rows = [i for i in range(len(universe)) if '#' not in universe[i]]
    empty_cols = [j for j in range(len(universe[0])) if not any(universe[i][j] == '#' for i in range(len(universe)))]
    return empty_rows, empty_cols

def get_distance(g1, g2, empty_rows, empty_cols, multiplier):
    row_start, row_end = sorted([g1[0], g2[0]])
    col_start, col_end = sorted([g1[1], g2[1]])

    empty_rows_in_range = sum(row_start < row < row_end for row in empty_rows)
    empty_cols_in_range = sum(col_start < col < col_end for col in empty_cols)

    row_diff = row_end - row_start + (multiplier - 1) * empty_rows_in_range
    col_diff = col_end - col_start + (multiplier - 1) * empty_cols_in_range
    return row_diff + col_diff

def get_galaxies(universe):
    return [(row, col) for row in range(len(universe)) for col in range(len(universe[0])) if universe[row][col] == '#']

def sum_distances(galaxies, empty_rows, empty_cols, multiplier):
    return sum(get_distance(galaxies[i], galaxies[j], empty_rows, empty_cols, multiplier) for i in range(len(galaxies) - 1) for j in range(i + 1, len(galaxies)))


universe = [list(line) for line in open("input.txt").read().split("\n")]
empty_rows, empty_cols = get_empty_rows_and_cols(universe)
galaxies = get_galaxies(universe)
print("part 1: {}\npart 2: {}".format(sum_distances(galaxies, empty_rows, empty_cols, 2), sum_distances(galaxies, empty_rows, empty_cols, 1000000)))