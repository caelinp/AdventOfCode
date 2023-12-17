from heapq import heappop, heappush

def read_grid_xy(infile):
    g = []
    w = 0
    h = 0
    for y, line in enumerate(infile):
        line = line.strip()
        if len(line) == 0:
            break
        g.append(line)
        w = max(w, len(line))
        h = max(h, y+1)
    return (w, h, g)

def v_add(p0, p1):
    return (p0[0] + p1[0], p0[1] + p1[1])

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

NORTH = UP
SOUTH = DOWN
EAST = LEFT
WEST = RIGHT

def turn180(d):
    return (-d[0], -d[1])

infile = open("input.txt")
(w, h, grid) = read_grid_xy(infile)

def in_bounds(p):
    return (p[0] >= 0 and p[1] >= 0 and p[0] < w and p[1] < h)

# Every move takes you to a plane with 1 less move allowed in that direction. But a move in
# any direction resets the counters for the other direction. Except no backwards moves are
# ever allowed.
# The entrance is the only point with none of these restrictions (no past), but it is in
# the upper left so it only has two exits anyway. Still must be a special case.
# The exit is on all planes, any might be reached first.

edges = {}

for y in range(h):
    for x in range(w):
        p = (x, y)
        for hist_dir in [NORTH, SOUTH, EAST, WEST]:
            for hist_dist in [1, 2]:
                cur = (p, hist_dir, hist_dist)
                e = []
                edges[cur] = e

                for next_dir in [NORTH, SOUTH, EAST, WEST]:
                    if next_dir == turn180(hist_dir):
                        # no U-turn
                        continue
                    np = v_add(p, next_dir)
                    if not in_bounds(np):
                        continue
                    if next_dir == hist_dir:
                        e.append((np, next_dir, hist_dist + 1))
                    else:
                        e.append((np, next_dir, 1))
            # only turn state
            cur = (p, hist_dir, 3)
            e = []
            edges[cur] = e
            for next_dir in [NORTH, SOUTH, EAST, WEST]:
                if next_dir == turn180(hist_dir):
                    continue
                if next_dir == hist_dir:
                    continue
                np = v_add(p, next_dir)
                if not in_bounds(np):
                    continue
                e.append((np, next_dir, 1))


init = ((0,0), None, 0)
edges[init] = []
for next_dir in [NORTH, SOUTH, EAST, WEST]:
    np = v_add((0,0), next_dir)
    if not in_bounds(np):
        continue
    edges[init].append((np, next_dir, 1))

hp = [(0, (w-1) + (h - 1), init)]
on_list = set()
on_list.add(init)

grid = [[int(c) for c in line] for line in grid]

while True:
    (cur_cost, e_cost, cur) = heappop(hp)
    cp = cur[0]
    if cp == (w-1, h-1):
        print(cur_cost)
        break
    for nc in edges[cur]:
        if nc in on_list:
            continue
        on_list.add(nc)
        ncp = nc[0]
        nc_cost = cur_cost + grid[ncp[1]][ncp[0]]
        heappush(hp, (nc_cost, (w - 1 - ncp[0] + h - 1 - ncp[1]), nc))