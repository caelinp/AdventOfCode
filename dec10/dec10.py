
def get_origin(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if is_origin(matrix, row, col):
                return (row, col)

def is_in_bounds(matrix, row, col):
    rows, cols = len(matrix), len(matrix[0])
    return (0 <= row < rows) and (0 <= col < cols)

def reset_origin_pipe(matrix, origin):
    row, col = origin
    north, east, south, west = get_north(matrix, row, col, origin), get_east(matrix, row, col, origin), get_south(matrix, row, col, origin), get_west(matrix, row, col, origin)
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

def get_north(matrix, row, col, last):
    return (row - 1, col) if is_in_bounds(matrix, row - 1, col) and matrix[row - 1][col] in ['|','7','F', "S"] and (row - 1, col) != last else None

def get_south(matrix, row, col, last):
    return (row + 1, col) if is_in_bounds(matrix, row + 1 , col) and matrix[row + 1][col] in ['|','J','L', "S"] and (row + 1, col) != last else None

def get_east(matrix, row, col, last):
    return (row, col + 1) if is_in_bounds(matrix, row, col + 1) and matrix[row][col + 1] in ['-','7','J', "S"] and (row, col + 1) != last else None

def get_west(matrix, row, col, last):
    return (row, col - 1) if is_in_bounds(matrix, row, col - 1) and matrix[row][col - 1] in ['-','F','L', "S"] and (row, col - 1) != last else None

def build_loop(matrix, origin):
    row, col = get_next_pipe(matrix, *origin, origin)
    last = origin
    length = 0
    loop = [origin]
    while not is_origin(matrix, row, col):
        #print("current:"+ str(row) + " " + str(col))
        loop.append((row, col))
        pos = get_next_pipe(matrix, row, col, last)
        last = (row, col)
        row, col = pos
        length += 1
    return loop, length + 1

def get_loop_area(matrix, loop):
    direction = None
    for i in range(len(loop)):
        loop


# this will go clockwise
def get_next_pipe(matrix, row, col, last):
    pipe = matrix[row][col]
    if is_origin(matrix, row, col):
        if (north := get_north(matrix, row, col, last)):
            return north
        elif (east := get_east(matrix, row, col, last)):
            return east
        elif (south := get_south(matrix, row, col, last)):
            return south
        elif (west := get_west(matrix, row, col, last)):
            return west
    if pipe == "|":
        if (north := get_north(matrix, row, col, last)):
            return north
        elif (south := get_south(matrix, row, col, last)):
            return south 
    elif pipe == "-":
        get_west(matrix, row, col, last)
        if (east := get_east(matrix, row, col, last)):

            return east
        elif (west := get_west(matrix, row, col, last)):
            return west
        
    elif pipe == "L":
        if (north := get_north(matrix, row, col, last)):
            return north
        elif (east := get_east(matrix, row, col, last)):
            return east
    elif pipe == "F":
        if (east := get_east(matrix, row, col, last)):
            return east
        elif (south := get_south(matrix, row, col, last)):
            return south 
    elif pipe == "7":
        if (west := get_west(matrix, row, col, last)):
            return west
        elif (south := get_south(matrix, row, col, last)):
            return south 
    elif pipe == "J":
        if (north := get_north(matrix, row, col, last)):
            return north
        elif (west := get_west(matrix, row, col, last)):
            return west
    return None

matrix = [list(line) for line in open("example_input.txt").read().split("\n")]
origin = get_origin(matrix)

loop, length = build_loop(matrix, origin)
farthest = length // 2

reset_origin_pipe(matrix, origin)


print(loop)
area = get_loop_area(matrix, loop)
for line in matrix:
    print("".join(line))
print("part 1: {}\npart 2: {}".format(farthest, area))




