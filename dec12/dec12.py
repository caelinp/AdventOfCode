from functools import cache
@cache
def count_arrangements(pattern, groups):
    arrangements = 0
    if not groups:
        return not "#" in pattern
    while sum(groups) + len(groups) - 1 <= len(pattern):
        to_add = "#" * groups[0] + ("." if len(groups) > 1 else "")
        if not any(pattern[i] != "?" and pattern[i] != to_add[i] for i in range(len(to_add))):
            arrangements += count_arrangements(pattern[len(to_add):], groups[1:])
        if pattern[0] == "#":
            break
        pattern = pattern[1:]
    return arrangements   
p1, p2 = 0, 0
for line in [line.split() for line in open("input.txt").read().split("\n")]:
    p1 += count_arrangements(line[0], tuple(int(group) for group in line[1].split(',')))
    line = ["?".join([line[0]] * 5), ",".join([line[1]] * 5)]
    p2 += count_arrangements(line[0], tuple(int(group) for group in line[1].split(',')))
print("part 1: {}\npart 2: {}".format(p1, p2))

    


