res = 0

# (r, c) coordinates of all symbols
symbols = set()

# helper function that takes in coorindates r, c and returns True if any neighbors, diagonal, up, down, left, or right, are symbols, and false otherwise
def hasSymbolNeighbour(r, c):
    return (r, c - 1) in symbols or (r, c + 1) in symbols or (r - 1, c) in symbols or (r + 1, c) in symbols or (r - 1, c - 1) in symbols or (r - 1, c + 1) in symbols or (r + 1, c - 1) in symbols or (r + 1, c + 1) in symbols

with open("dec3_input.txt", "r") as text:
    data = text.readlines()
    matrix = []
    
    # create 2d matrix from input data
    for i, line in enumerate(data):
        matrix.append([])
        for c in line:
            if c != "\n":
                matrix[i].append(c)
    
    # record coordinates of all symbols
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if not matrix[r][c].isnumeric() and matrix[r][c] != ".":
                symbols.add((r, c))
    
    # now iterate through all characters
    for r in range(len(matrix)):
        c = 0
        while c < len(matrix[0]):
            # skip if coord is a symbol
            if (r, c) in symbols:
                c += 1
                continue
            char = matrix[r][c]

            # else if it's a number
            if char.isnumeric():
                number = int(char)
                # check if first digit has a symbol neighbour
                hasSymbol = hasSymbolNeighbour(r, c)
                while c + 1 < len(matrix[0]) and matrix[r][c + 1].isnumeric():
                    # here we extend the number until the end
                    c += 1
                    if hasSymbol or hasSymbolNeighbour(r, c):
                        hasSymbol = True
                    number *= 10
                    number += int(matrix[r][c])
                c += 1

                if hasSymbol:
                    res += number

            elif char != '.':
                symbols.add((r, c))
            c += 1
    print(res)



