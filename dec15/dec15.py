steps = open("input.txt").read().split(",")
p1 = 0

def get_hash(lens):
    hash = 0
    for c in lens:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash

for step in steps:
    p1 += get_hash(step)

p2 = 0

box_map = {}

for step in steps:
    if "-" in step:
        lens = step[:-1]
        hash = get_hash(lens)
        box = box_map.get(hash, {})
        if lens in box:
            del box[lens]
    elif "=" in step:
        lens, focal = step.split("=")
        hash = get_hash(lens)
        if hash in box_map:
            box = box_map[hash]
            box[lens] = focal
        else:
            box_map[hash] = {lens : focal}

for box, lenses in box_map.items():
    for i, (lens, focal) in enumerate(lenses.items()):
        p2 += (int(box) + 1) * (i + 1) * int(focal)

print("part 1: {}\npart 2: {}".format(p1, p2))
