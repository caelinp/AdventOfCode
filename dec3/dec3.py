# helper function that takes in coorindates r, c and returns True if any neighbors, diagonal, up, down, left, or right, are symbols, and false otherwise
def has_symbol_neighbour(matrix, r, c):
    neighbour_directions = {(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)}
    return any([not matrix[r + dr][c + dc].isnumeric() and matrix[r + dr][c + dc] != "." for (dr, dc) in neighbour_directions if 0 <= (r + dr) < len(matrix) and 0 <= (c + dc) < len(matrix[0])])

# helper function that takes in coordinates r, c and returns a list of stars that are neighbours with (r, c), or an empty list if there are none
def get_star_neighbours(matrix, r, c):
    neighbour_directions = {(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)}
    return [(r + dr, c + dc) for (dr, dc) in neighbour_directions if 0 <= (r + dr) < len(matrix) and 0 <= (c + dc) < len(matrix[0]) and matrix[r + dr][c + dc] == "*"]

matrix = [list(line) for line in open("example_input.txt").read().split("\n")]
stars = {(r, c) : [] for c in range(len(matrix[0])) for r in range(len(matrix)) if matrix[r][c] == "*"}
p1, p2 = 0, 0
# now iterate through all characters
for r in range(len(matrix)):
    c = 0
    while c < len(matrix[0]):
        # skip if coord is a symbol
        char = matrix[r][c]
        if not char.isnumeric():
            c += 1
            continue
        number = int(char)
        # check if first digit has a symbol neighbour
        touching_symbol = has_symbol_neighbour(matrix, r, c)
        star_neighbours = get_star_neighbours(matrix, r, c)
        while c + 1 < len(matrix[0]) and matrix[r][c + 1].isnumeric():
            # here we extend the number until the end
            c += 1
            touching_symbol |= has_symbol_neighbour(matrix, r, c)
            star_neighbours = get_star_neighbours(matrix, r, c) if not star_neighbours else star_neighbours
            number = number * 10 + int(matrix[r][c])
        p1 += number * touching_symbol
        if star_neighbours:
            stars[star_neighbours[0]].append(number)
        c += 2
p2 = sum([stars[star][0] * stars[star][1] for star in stars if len(stars[star]) == 2])
print("part 1: {}\npart 2: {}".format(p1, p2))



