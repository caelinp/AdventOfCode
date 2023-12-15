p1, p2 = 0, 0

for pair in open("input.txt").read().split("\n"):
    pair = pair.split(",")
    (r1_start, r1_end) = (int(num) for num in pair[0].split('-'))
    (r2_start, r2_end) = (int(num) for num in pair[1].split('-'))
    if r1_start >= r2_start and r1_end <= r2_end or r1_start <= r2_start and r1_end >= r2_end:
        p1 += 1
        p2 += 1
    elif r1_end >= r2_start and r1_start <= r2_start or r2_end >= r1_start and r2_start <= r1_start:
        p2 += 1
print("part 1: {}\npart 2: {}".format(p1, p2))
