res = 0
numbers = []
stars = {}
valid_stars = {}

def getStarNeighbour(r, c):
    if (r, c - 1) in stars:
        return (r, c - 1)
    if (r, c + 1) in stars:
        return (r, c + 1)
    if (r - 1, c) in stars:
        return (r - 1, c)
    if (r + 1, c) in stars:
        return (r + 1, c)
    if (r - 1, c - 1) in stars:
        return (r - 1, c - 1)
    if (r + 1, c - 1) in stars:
        return (r + 1, c - 1)
    if (r - 1, c + 1) in stars:
        return (r - 1, c + 1)
    if (r + 1, c + 1) in stars:
        return (r + 1, c + 1)
    return None

with open("dec3_input.txt", "r") as text:
    data = text.readlines()
    matrix = []
    for i, line in enumerate(data):
        matrix.append([])
        for c in line:
            if c != "\n":
                matrix[i].append(c)
    
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == '*':
                stars[(r, c)] = []
    

    for r in range(len(matrix)):
        c = 0
        while c < len(matrix[0]):
            char = matrix[r][c]
            if char.isnumeric():
                number = int(char)
                starNeighbour = getStarNeighbour(r, c)
                while c + 1 < len(matrix[0]) and matrix[r][c + 1].isnumeric():
                    c += 1
                    if not starNeighbour:
                        starNeighbour = getStarNeighbour(r, c)   
                    number *= 10
                    number += int(matrix[r][c])
                c += 1
                if starNeighbour:
                    stars[starNeighbour].append(number)
            c += 1

    for star in stars:
        if len(stars[star]) == 2:
            res += stars[star][0] * stars[star][1]
            valid_stars[star] = stars[star]

    print(valid_stars) 
    print(res)



