p1, p2 = 0, 0

sacks = open("input.txt").read().split("\n")
for i, sack in enumerate(sacks):
    if i % 3 == 0:
        s1, s2, s3 = set(sack), set(sacks[i + 1]), set(sacks[i + 2])
        overlap = s1.intersection(s2).intersection(s3).pop()
        value = (ord(overlap) - ord('A') + 27) if overlap.isupper() else  (ord(overlap) - ord('a') + 1)
        p2 += value
    c1, c2 = set(sack[:len(sack)//2]), set(sack[len(sack)//2:])
    overlap = c1.intersection(c2).pop()
    value = (ord(overlap) - ord('A') + 27) if overlap.isupper() else  (ord(overlap) - ord('a') + 1)
    p1 += value
print("part 1: {}\npart 2: {}".format(p1, p2))