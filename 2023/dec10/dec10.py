def get_origin(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if is_origin(matrix, row, col):
                return (row, col)

def is_in_bounds(matrix, row, col):
    rows, cols = len(matrix), len(matrix[0])
    return (0 <= row < rows) and (0 <= col < cols)

def fill_area(matrix, loop, value, row, col, outside_inside):
    loop = set(loop)
    def fill(row, col):
        nonlocal value
        if not is_in_bounds(matrix, row, col):
            outside_inside[2] = value
        if not is_in_bounds(matrix, row, col) or (row, col) in loop or (row, col) in outside_inside[0] or (row, col) in outside_inside[1]:
            return
        else:
            outside_inside[value].add((row, col))
            north, east, south, west = (row - 1, col), (row, col + 1), (row + 1, col), (row, col + 1)
            if north and north not in loop:
                fill(*north)
            if east and east not in loop:
                fill(*east)
            if south and south not in loop:
                fill(*south)
            if west and west not in loop:
                fill(*west)
    fill(row, col)
            
def reset_origin_pipe(matrix, origin):
    row, col = origin
    north, east, south, west = get_north_pipe(matrix, row, col, origin), get_east_pipe(matrix, row, col, origin), get_south_pipe(matrix, row, col, origin), get_west_pipe(matrix, row, col, origin)
    if north and south:
        matrix[row][col] = "|"
    elif north and east:
        matrix[row][col] = "L"
    elif north and west:
        matrix[row][col] = "J"
    elif south and west:
        matrix[row][col] = "7"
    elif south and east:
        matrix[row][col] = "F"
    elif east and west:
        matrix[row][col] = "-"
        
def is_origin(matrix, row, col):
    return is_in_bounds(matrix, row, col) and matrix[row][col] == 'S'

def get_north_pipe(matrix, row, col, last):
    return (row - 1, col) if is_in_bounds(matrix, row - 1, col) and matrix[row - 1][col] in ['|','7','F', "S"] and (row - 1, col) != last else None

def get_south_pipe(matrix, row, col, last):
    return (row + 1, col) if is_in_bounds(matrix, row + 1 , col) and matrix[row + 1][col] in ['|','J','L', "S"] and (row + 1, col) != last else None

def get_east_pipe(matrix, row, col, last):
    return (row, col + 1) if is_in_bounds(matrix, row, col + 1) and matrix[row][col + 1] in ['-','7','J', "S"] and (row, col + 1) != last else None

def get_west_pipe(matrix, row, col, last):
    return (row, col - 1) if is_in_bounds(matrix, row, col - 1) and matrix[row][col - 1] in ['-','F','L', "S"] and (row, col - 1) != last else None

def build_loop(matrix, origin):
    row, col = get_next_pipe(matrix, *origin, origin)
    last = origin
    length = 0
    loop = [origin]
    while not is_origin(matrix, row, col):
        loop.append((row, col))
        pos = get_next_pipe(matrix, row, col, last)
        last = (row, col)
        row, col = pos
        length += 1
    return loop, length + 1

def get_directions(matrix, row, col, last):
    symbol = matrix[row][col]
    # came from north
    if last == (row - 1, col):
        if symbol == "|":
            return ["S"]
        elif symbol == "L":
            return ["S", "E"]
        elif symbol == "J":
            return ["S", "W"]
    # came from south
    elif last == (row + 1, col):
        if symbol == "|":
            return ["N"]
        elif symbol == "7":
            return ["N", "W"]
        elif symbol == "F":
            return ["N", "E"]
    # came from west
    elif last == (row, col - 1):
        if symbol == "-":
            return ["E"]
        elif symbol == "7":
            return ["E", "S"]
        elif symbol == "J":
            return ["E", "N"]
    # came from east
    elif last == (row, col + 1):
        if symbol == "-":
            return ["W"]
        elif symbol == "F":
            return ["W", "S"]
        elif symbol == "L":
            return ["W", "N"]
    return None

def get_loop_area(matrix, loop, outside_inside):
    last = loop[0]
    for (row, col) in loop[1:]:
        pipe = matrix[row][col]
        directions = get_directions(matrix, row, col, last)
        north = (row - 1, col)
        south = (row + 1, col)
        east = (row, col + 1)
        west = (row, col - 1)
        if pipe == "|":
            if directions == ["N"]:
                fill_area(matrix, loop, 0, *west, outside_inside)
                fill_area(matrix, loop, 1, *east, outside_inside)
            elif directions == ["S"]:
                fill_area(matrix, loop, 0, *east, outside_inside)
                fill_area(matrix, loop, 1, *west, outside_inside)
        elif pipe == "-":
            if directions == ["E"]:
                fill_area(matrix, loop, 1, *south, outside_inside)
                fill_area(matrix, loop, 0, *north, outside_inside)
            elif directions == ["W"]:
                fill_area(matrix, loop, 1, *north, outside_inside)
                fill_area(matrix, loop, 0, *south, outside_inside)
        elif pipe == "L":
            if directions == ["S", "W"]:
                fill_area(matrix, loop, 1, *south, outside_inside)
                fill_area(matrix, loop, 1, *west, outside_inside)
            elif directions == ["E", "N"]:
                fill_area(matrix, loop, 0, *south, outside_inside)
                fill_area(matrix, loop, 0, *west, outside_inside)
        elif pipe == "7":
            if directions == ["E", "S"]:
                fill_area(matrix, loop, 0, *north, outside_inside)
                fill_area(matrix, loop, 0, *east, outside_inside)
            elif directions == ["N", "W"]:
                fill_area(matrix, loop, 1, *north, outside_inside)
                fill_area(matrix, loop, 1, *east, outside_inside)
        elif pipe == "J":
            if directions == ["S", "W"]:
                fill_area(matrix, loop, 0, *south, outside_inside)
                fill_area(matrix, loop, 0, *east, outside_inside)
            elif directions == ["E", "N"]:
                fill_area(matrix, loop, 1, *south, outside_inside)
                fill_area(matrix, loop, 1, *east, outside_inside)
        elif pipe == "F":
            if directions == ["N", "E"]:
                fill_area(matrix, loop, 0, *north, outside_inside)
                fill_area(matrix, loop, 0, *west, outside_inside)
            elif directions == ["W", "S"]:
                fill_area(matrix, loop, 1, *north, outside_inside)
                fill_area(matrix, loop, 1, *west, outside_inside)
        if (len(outside_inside[0]) + len(outside_inside[1]) + len(loop)) == len(matrix) * len(matrix[0]):
            return                                     
        last = (row, col)



def get_next_pipe(matrix, row, col, last):
    if is_origin(matrix, row, col):
        if (north := get_north_pipe(matrix, row, col, last)):
            return north
        elif (east := get_east_pipe(matrix, row, col, last)):
            return east
        elif (south := get_south_pipe(matrix, row, col, last)):
            return south
        elif (west := get_west_pipe(matrix, row, col, last)):
            return west
    pipe = matrix[row][col]
    if pipe == "|":
        if (north := get_north_pipe(matrix, row, col, last)):
            return north
        elif (south := get_south_pipe(matrix, row, col, last)):
            return south 
    elif pipe == "-":
        get_west_pipe(matrix, row, col, last)
        if (east := get_east_pipe(matrix, row, col, last)):
            return east
        elif (west := get_west_pipe(matrix, row, col, last)):
            return west
    elif pipe == "L":
        if (north := get_north_pipe(matrix, row, col, last)):
            return north
        elif (east := get_east_pipe(matrix, row, col, last)):
            return east
    elif pipe == "F":
        if (east := get_east_pipe(matrix, row, col, last)):
            return east
        elif (south := get_south_pipe(matrix, row, col, last)):
            return south 
    elif pipe == "7":
        if (west := get_west_pipe(matrix, row, col, last)):
            return west
        elif (south := get_south_pipe(matrix, row, col, last)):
            return south 
    elif pipe == "J":
        if (north := get_north_pipe(matrix, row, col, last)):
            return north
        elif (west := get_west_pipe(matrix, row, col, last)):
            return west
    return None

matrix = [list(line) for line in open("example_input.txt").read().split("\n")]
origin = get_origin(matrix)

loop, length = build_loop(matrix, origin)
farthest = length // 2

reset_origin_pipe(matrix, origin)
outside_inside = [set(), set(), int]

get_loop_area(matrix, loop, outside_inside)
area = len(outside_inside[not outside_inside[2]])
print("part 1: {}\npart 2: {}".format(farthest, area))




