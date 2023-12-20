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

def a_star(heightmap, start, end):
    frontier = []
    # state is current path cost + min heuristic distance from pos to goal, current path cost, (row, col)
    visited = set()
    state = (heuristic(start, end), 0, start)
    while not(state[2] == end):
        cur_path_cost, pos = state[1], state[2]
        cur_height = ord('a') if pos == start else ord(heightmap[pos[0]][pos[1]])
        # add neighbours of current position to frontier:

        for (dr, dc) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_pos = (pos[0] + dr, pos[1] + dc)
            if in_bounds(new_pos, heightmap) and new_pos not in visited:
                new_height = ord(heightmap[new_pos[0]][new_pos[1]])
                if new_height - cur_height <= 1:
                    heur_val = heuristic(new_pos, end)
                    new_path_cost = cur_path_cost + 1
                    # need to increment steps in one direction if new dir is same as current dir, else reset it to 1
                    new_state = (heur_val + new_path_cost, new_path_cost, new_pos)
                    visited.add(new_pos)
                    heappush(frontier, new_state)
        state = heappop(frontier)
    return state[1]            

heightmap = [[height for height in row] for row in open('example_input.txt').read().split('\n')]
start, end = get_start_and_end(heightmap)
print(start, end)
p1 = a_star(heightmap, start, end)

p2 = 0
print("part 1: {}\npart 2: {}".format(p1, p2))
