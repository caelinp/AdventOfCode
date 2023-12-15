p1 = max([sum(int(cal) for cal in elf.split("\n")) for elf in open("input.txt").read().split("\n\n")])

elves = open("input.txt").read().split("\n\n")
top_three = []
for elf in elves:
    top_three.append(sum([int(cal) for cal in elf.split("\n")]))
    if len(top_three) > 3:
        top_three.sort(reverse=True)
        top_three = top_three[:3]

p2 = sum(top_three)
print("part 1: {}\npart 2: {}".format(p1, p2))