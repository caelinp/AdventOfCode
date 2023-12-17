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

init = ((0,0), None, 0)
hp = [(0, init)]
on_list = set()
on_list.add(init)

grid = [[int(c) for c in line] for line in grid]

iters = 0
while True:
    (cur_cost, (p, hist_dir, hist_dist)) = heappop(hp)
    if hist_dist >= 4 and p == (w-1, h-1):
        print(cur_cost)
        break

    e = []

    if hist_dir is None:
        for next_dir in [NORTH, SOUTH, EAST, WEST]:
            np = v_add(p, next_dir)
            if not in_bounds(np):
                continue
            e.append((np, next_dir, 1))
    elif hist_dist < 4:
        # must continue
        next_dir = hist_dir
        np = v_add(p, next_dir)
        if in_bounds(np):
            e.append((np, next_dir, hist_dist + 1))
    elif hist_dist < 10:
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
    else:
        # must turn
        for next_dir in [NORTH, SOUTH, EAST, WEST]:
            if next_dir == turn180(hist_dir):
                continue
            if next_dir == hist_dir:
                continue
            np = v_add(p, next_dir)
            if not in_bounds(np):
                continue
            e.append((np, next_dir, 1))

    for nc in e:
        if nc in on_list:
            continue
        on_list.add(nc)
        (nx, ny) = nc[0]
        nc_cost = cur_cost + grid[ny][nx]
        heappush(hp, (nc_cost, nc))
