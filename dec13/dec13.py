def get_above_value(pattern):
    for i in range(len(pattern) - 1):
        u, d = i, i + 1
        mirror = True
        while u >= 0 and d < len(pattern):
            if pattern[u] != pattern[d]:
                mirror = False
                break
            u -= 1
            d += 1
        if mirror:
            return i + 1
    return 0

def get_above_value_smudge(pattern):
    for i in range(len(pattern) - 1):
        u, d = i, i + 1
        valid = True
        diff = 0
        while u >= 0 and d < len(pattern):
            for j in range(len(pattern[0])):
                if pattern[u][j] != pattern[d][j]:
                    diff += 1
                    if diff > 1:
                        valid = False
                        break
            if not valid:
                break
            u -= 1
            d += 1
        if diff == 1 and valid:
            return i + 1
    return 0

def get_left_value_smudge(pattern):
    for j in range(len(pattern[0]) - 1):
        l, r = j, j + 1
        valid = True
        diff = 0
        while l >= 0 and r < len(pattern[0]):
            for i in range(len(pattern)):
                if pattern[i][l] != pattern[i][r]:
                    diff += 1
                    if diff > 1:
                        valid = False
                        break
            if not valid:
                break
            l -= 1
            r += 1
        if diff == 1 and valid: 
            return j + 1
    return 0

def get_left_value(pattern):
    for j in range(len(pattern[0]) - 1):
        l, r = j, j + 1
        mirror = True
        while l >= 0 and r < len(pattern[0]):
            if not all([pattern[i][l] == pattern[i][r] for i in range(len(pattern))]):
                mirror = False
                break
            l -= 1
            r += 1
        if mirror: 
            return j + 1
    return 0

patterns = [[list(line) for line in pattern.split("\n")] for pattern in open("input.txt").read().split("\n\n")]
p1, p2 = 0, 0
for pattern in patterns:
    p1 += 100 * get_above_value(pattern) + get_left_value(pattern)
    p2 += 100 * get_above_value_smudge(pattern) + get_left_value_smudge(pattern)

print("part 1: {}\npart 2: {}".format(p1, p2))