from heapq import heappush, heappop

def in_bounds(pos, blocks):
    return (0 <= pos[0] < len(blocks)) and (0 <= pos[1] < len(blocks[0]))

def heuristic(pos, goal):
    return abs(goal[0] - pos[0]) + abs(goal[1] - pos[1])

def a_star(blocks, max_straight_steps=3, min_straight_steps=0):
    frontier = []
    goal = (len(blocks) - 1, len(blocks[0]) - 1)
    # state is current path cost + min heuiristic distance from pos to goal, current path cost, (row, col), number of steps taken in current direction, current direction
    # don't count count heat loss for start block, so current path cost is 0
    visited = set()
    state = (heuristic((0, 0), goal), 0, (0, 0), 0, None)
    while not(state[2] == goal and state[3] >= min_straight_steps):
        cur_path_cost, pos, steps_in_one_dir, dir = state[1], state[2], state[3], state[4]
        # add neighbours of current position to frontier:
        if not dir:
            # if no direction yet, we are in starting square
            new_dirs = {'E', 'S'}
        elif steps_in_one_dir < min_straight_steps:
            new_dirs = {dir}
        else:
            new_dirs = {'N', 'E', 'S', 'W'}

            # if we've moved max steps in the current direction, need to choose a different direction
            if steps_in_one_dir == max_straight_steps:
                new_dirs.discard(dir)
                steps_in_one_dir = 0
            # can't go in the opposite direction of current direction
            new_dirs.discard({'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}[dir])
        
        for new_dir in new_dirs:
            dr, dc = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}[new_dir]
            new_pos = (pos[0] + dr, pos[1] + dc)
            if in_bounds(new_pos, blocks):
                heur_val = heuristic(new_pos, goal)
                new_path_cost = cur_path_cost + blocks[new_pos[0]][new_pos[1]]
                # need to increment steps in one direction if new dir is same as current dir, else reset it to 1
                new_steps_in_one_dir = steps_in_one_dir * (dir == new_dir) + 1
                new_state = (heur_val + new_path_cost, new_path_cost, new_pos, new_steps_in_one_dir, new_dir)
                if (new_pos, new_steps_in_one_dir, new_dir) not in visited:
                    visited.add((new_pos, new_steps_in_one_dir, new_dir))
                    heappush(frontier, new_state)
        state = heappop(frontier)
    return state[1]            

blocks = [[int(heat_loss) for heat_loss in list(row)] for row in open('input.txt').read().split()]

p1 = a_star(blocks, 3)

p2 = a_star(blocks, 10, 4)
print("part 1: {}\npart 2: {}".format(p1, p2))
