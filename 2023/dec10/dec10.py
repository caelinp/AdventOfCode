import math
def get_origin(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'S':
                return (row, col)

def is_in_bounds(matrix, row, col):
    return (0 <= row < len(matrix)) and (0 <= col < len(matrix[0]))

def calculate_area(loop):
    area = 0
    perimeter = 0
    for i in range(len(loop)):
        x0, y0 = loop[i]
        x1, y1 = loop[(i + 1) % len(loop)]  # Wrap around to the first point
        perimeter += abs(y1 - y0) + abs(x1 - x0)
        area += (x0 * y1) - (x1 * y0)
    return math.ceil(abs(area) / 2 - perimeter / 2 + 1)

def get_north_pipe(matrix, row, col, last):
    return (row - 1, col) if is_in_bounds(matrix, row - 1, col) and matrix[row - 1][col] in '|7FS' and (row - 1, col) != last else None

def get_south_pipe(matrix, row, col, last):
    return (row + 1, col) if is_in_bounds(matrix, row + 1 , col) and matrix[row + 1][col] in '|JLS' and (row + 1, col) != last else None

def get_east_pipe(matrix, row, col, last):
    return (row, col + 1) if is_in_bounds(matrix, row, col + 1) and matrix[row][col + 1] in '-7JS' and (row, col + 1) != last else None

def get_west_pipe(matrix, row, col, last):
    return (row, col - 1) if is_in_bounds(matrix, row, col - 1) and matrix[row][col - 1] in '-FLS' and (row, col - 1) != last else None

def build_loop(matrix, origin):
    row, col = get_next_pipe(matrix, *origin, origin)
    last = origin
    length = 1
    loop = []
    while matrix[row][col] != 'S':
        pos = get_next_pipe(matrix, row, col, last)
        last = (row, col)
        row, col = pos
        if matrix[row][col] not in '|-':
            loop.append((row, col))
        length += 1
    return loop, length

def get_next_pipe(matrix, row, col, last):
    pipe = matrix[row][col]
    if pipe == 'S':
        return get_north_pipe(matrix, row, col, last) or get_east_pipe(matrix, row, col, last) or get_south_pipe(matrix, row, col, last) or get_west_pipe(matrix, row, col, last)
    elif pipe == "|":
        return get_north_pipe(matrix, row, col, last) or get_south_pipe(matrix, row, col, last)
    elif pipe == "-":
        return get_east_pipe(matrix, row, col, last) or get_west_pipe(matrix, row, col, last)
    elif pipe == "L":
        return get_east_pipe(matrix, row, col, last) or get_north_pipe(matrix, row, col, last)
    elif pipe == "F":
        return get_east_pipe(matrix, row, col, last) or get_south_pipe(matrix, row, col, last)
    elif pipe == "7":
        return get_south_pipe(matrix, row, col, last) or get_west_pipe(matrix, row, col, last)
    elif pipe == "J":
        return get_north_pipe(matrix, row, col, last) or get_west_pipe(matrix, row, col, last)

matrix = [list(line) for line in open("input.txt").read().split("\n")]
origin = get_origin(matrix)

loop, length = build_loop(matrix, origin)
farthest = length // 2

area = calculate_area(loop)
print("part 1: {}\npart 2: {}".format(farthest, area))




