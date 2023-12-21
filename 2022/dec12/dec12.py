from heapq import heappush, heappop

def in_bounds(pos, heightmap):
    return (0 <= pos[0] < len(heightmap)) and (0 <= pos[1] < len(heightmap[0]))

def get_start_and_end(heightmap):
    start, end = None, None
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if heightmap[i][j] == 'S':
                start = (i, j)
            elif heightmap[i][j] == 'E':
                end = (i, j)
            if start and end:
                return start, end

def heuristic(pos, goal):
    return abs(goal[0] - pos[0]) + abs(goal[1] - pos[1])

def a_star_p1(heightmap, start, end):
    frontier = []
    visited = set()
    state = (heuristic(start, end), 0, start)
    heappush(frontier, state)

    while frontier:
        _, cur_path_cost, pos = heappop(frontier)
        if pos in visited:
            continue
        visited.add(pos)

        if pos == end:
            return cur_path_cost

        cur_height = ord('a') if pos == start else ord(heightmap[pos[0]][pos[1]])

        for (dr, dc) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_pos = (pos[0] + dr, pos[1] + dc)
            if in_bounds(new_pos, heightmap) and new_pos not in visited:
                new_height = ord('z') if heightmap[new_pos[0]][new_pos[1]] == 'E' else ord(heightmap[new_pos[0]][new_pos[1]])
                if new_height - cur_height <= 1:
                    heur_val = heuristic(new_pos, end)
                    new_path_cost = cur_path_cost + 1
                    new_state = (heur_val + new_path_cost, new_path_cost, new_pos)
                    heappush(frontier, new_state)
    return float('inf')
    
def a_star_p2(heightmap, end):
    shortest_path_from_a = float('inf')
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if heightmap[i][j] == 'a':
                shortest_path_from_a = min(shortest_path_from_a, a_star_p1(heightmap, (i, j), end))
    return shortest_path_from_a


# Load heightmap from file (adjust the path to your file)
heightmap = [[height for height in row] for row in open('example_input.txt').read().split('\n')]
start, end = get_start_and_end(heightmap)
p1 = a_star_p1(heightmap, start, end)

p2 = a_star_p2(heightmap, end)
print(f"Part 1: {p1}\nPart 2: {p2}")
