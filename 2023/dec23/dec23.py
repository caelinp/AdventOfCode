import sys
sys.setrecursionlimit(100000)
def in_bounds(pos, island):
    return 0 <= pos[0] < len(island) and 0 <= pos[1] < len(island[0])

def get_start(island):
    for c in range(len(island[0])):
        if island[0][c] == '.':
            return (0, c)

def get_end(island):
    for c in range(len(island[0])):
        if island[len(island) - 1][c] == '.':
            return (len(island) - 1, c)

def traverse(island):
    start = get_start(island)
    end = get_end(island)
    longest = 0
    def hike(pos, visited):
        nonlocal longest
        visited.add(pos)
        if pos == end:
            longest = max(longest, len(visited))
            return
        symbol = island[pos[0]][pos[1]]
        dirs = {'v' : (1, 0), '^' : (-1, 0), '>' : (0, 1), '<' : (0, -1)}
        if symbol in dirs:
            dirs = {symbol : dirs[symbol]}
        for dr, dc in dirs.values():
            r = pos[0] + dr
            c = pos[1] + dc
            if (r, c) not in visited and in_bounds((r, c), island) and island[r][c] != '#':
                hike((r, c), set(visited))
    hike(start, set())
    return longest - 1

def traverse_optimized(island):
    edges = {}
    start = get_start(island)
    end = get_end(island)
    for r in range(len(island)):
        for c in range(len(island[0])):
            if island[r][c] != '#':
                for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    nr, nc = r + dr, c + dc
                    if in_bounds((nr, nc), island) and island[nr][nc] != '#': 
                        # for every edge between two adjacent open positions in the map, add an edge with weight 1
                        # keys are positions, values are lists of neighbours that have an edge, along with the edge weight
                        edges.setdefault((r, c), set()).add(((nr, nc), 1))
                        edges.setdefault((nr, nc), set()).add(((r, c), 1))

    # Remove nodes with degree 2 by merging the edges
    while True:
        for v, e in edges.items():
            if len(e) == 2: # any node that has 2 edges can be removed, as long as we record an edge between their two neighbours, with the correct weight
                e1, e2 = e
                n1, w1, n2, w2 = e1[0], e1[1], e2[0], e2[1]
                edges[n1[:2]].remove((v, w1))
                edges[n2[:2]].remove((v, w2))
                edges[n1[:2]].add((n2, w1 + w2))
                edges[n2[:2]].add((n1, w1 + w2))
                del edges[v]
                break
        else:
            break
    
    longest = 0
    def hike(pos, visited, path_cost):
        nonlocal longest
        if pos in visited:
            return
        visited.add(pos)
        if pos == end:
            longest = max(longest, path_cost)
            return
        for new_pos, w in edges[pos]:
            hike(new_pos, set(visited), path_cost + w)
    hike(start, set(), 0)
    return longest

island = [list(row) for row in open('input.txt').read().splitlines()]
p1 = traverse(island)
p2 = traverse_optimized(island)
print("part 1: {}\npart 2: {}".format(p1, p2))