def drop_sand(rocks):
    floor = max([y for _, y in rocks])
    settled = set()
    while True:
        x, y = 500, 0
        while True:
            if y > floor:
                return settled 
            new_x, new_y = x, y + 1
            if (new_x, new_y) in settled or (new_x, new_y) in rocks:
                new_x -= 1
            else:
                x, y = new_x, new_y
                continue
            if (new_x, new_y) in settled or (new_x, new_y) in rocks:
                new_x += 2
            else:
                x, y = new_x, new_y
                continue
            if (new_x, new_y) in settled or (new_x, new_y) in rocks:
                break
            else:
                x, y = new_x, new_y
                continue
        settled.add((x, y))
def drop_sand_with_bottom(rocks):
    floor = max([y for _, y in rocks]) + 2
    floor_rocks = set([(x, floor) for x in range(664)])
    rocks.update(floor_rocks)
    settled = set()
    while True:
        x, y = 500, 0
        while True:
            new_x, new_y = x, y + 1
            if (new_x, new_y) in settled or (new_x, new_y) in rocks:
                new_x -= 1
            else:
                x, y = new_x, new_y
                continue
            if (new_x, new_y) in settled or (new_x, new_y) in rocks:
                new_x += 2
            else:
                x, y = new_x, new_y
                continue
            if (new_x, new_y) in settled or (new_x, new_y) in rocks:
                break
            else:
                x, y = new_x, new_y
                continue
        settled.add((x, y))
        if (x, y) == (500, 0):
            return settled
def get_points_between(p1, p2):
    points = set()
    if p1[0] > p2[0]:
        y = p1[1]
        for x in range(p2[0], p1[0] + 1):
            points.add((x, y))
        return points
    if p1[0] < p2[0]:
        y = p1[1]
        for x in range(p1[0], p2[0] + 1):
            points.add((x, y))
        return points
    if p1[1] > p2[1]:
        x = p1[0]
        for y in range(p2[1], p1[1] + 1):
            points.add((x, y))
        return points
    if p1[1] < p2[1]:
        x = p1[0]
        for y in range(p1[1], p2[1] + 1):
            points.add((x, y))
    return points
rock_patterns = [[tuple([int(x) for x in point.split(',')]) for point in path.split(' -> ')] for path in open('input.txt').read().splitlines()]
rocks = set()
for path in rock_patterns:
    for i in range(len(path) - 1):
        rocks.update(get_points_between(path[i], path[i + 1]))
p1 = len(drop_sand(rocks))
p2 = len(drop_sand_with_bottom(rocks))
print(f"part 1: {p1}\npart 2: {p2}")