
def get_above_value(pattern, max_diff=0):
    for i in range(len(pattern) - 1):
        u, d = i, i + 1
        valid = True
        diff = 0
        while u >= 0 and d < len(pattern):
            for j in range(len(pattern[0])):
                if pattern[u][j] != pattern[d][j]:
                    diff += 1
                    if diff > max_diff:
                        valid = False
                        break
            if not valid:
                break
            u -= 1
            d += 1
        if diff == max_diff and valid:
            return i + 1
    return 0

def get_left_value(pattern, max_diff=0):
    for j in range(len(pattern[0]) - 1):
        l, r = j, j + 1
        valid = True
        diff = 0
        while l >= 0 and r < len(pattern[0]):
            for i in range(len(pattern)):
                if pattern[i][l] != pattern[i][r]:
                    diff += 1
                    if diff > max_diff:
                        valid = False
                        break
            if not valid:
                break
            l -= 1
            r += 1
        if diff == max_diff and valid: 
            return j + 1
    return 0



patterns = [[list(line) for line in pattern.split("\n")] for pattern in open("input.txt").read().split("\n\n")]
p1, p2 = 0, 0
for pattern in patterns:
    p1 += 100 * get_above_value(pattern) + get_left_value(pattern)
    p2 += 100 * get_above_value(pattern, 1) + get_left_value(pattern, 1)

print("part 1: {}\npart 2: {}".format(p1, p2))