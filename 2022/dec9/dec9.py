def move_up(end):
    end[0] -= 1

def move_down(end):
    end[0] += 1

def move_left(end):
    end[1] -= 1

def move_right(end):
    end[1] += 1

def diag_drag_horiz(head, knot):
    if head[1] > knot[1]:
        move_right(knot)
    elif head[1] < knot[1]:
        move_left(knot) 

def diag_drag_vert(head, knot):
    if head[0] > knot[0]:
        move_down(knot)
    elif head[0] < knot[0]:
        move_up(knot)

def are_too_far_apart(head, knot):
    return abs(head[0] - knot[0]) > 1 or abs(head[1] - knot[1]) > 1

move = {"U": move_up, "D": move_down, "L": move_left, "R": move_right}
steps = [step for step in open("input.txt").read().split('\n')]

visited = set()

NUM_KNOTS = 10

knots = [[0, 0] for i in range(NUM_KNOTS)]

visited.add(tuple(knots[-1]))
for step in steps:
    dir, dist = step.split()
    for i in range(int(dist)):
        head = knots[0]
        move[dir](head)
        for knot in knots[1:]:
            if are_too_far_apart(head, knot):
                if head[0] > knot[0]:
                    diag_drag_horiz(head, knot)
                    move_down(knot)
                elif head[0] < knot[0]:
                    diag_drag_horiz(head, knot)
                    move_up(knot)
                elif head[1] > knot[1]:
                    diag_drag_vert(head, knot)
                    move_right(knot)
                elif head[1] < knot[1]:
                    diag_drag_vert(head, knot)
                    move_left(knot)
            head = knot
        visited.add(tuple(knots[-1]))

p1 = len(visited)
p2 = 0
print('part 1: {}\npart 2: {}'.format(p1, p2))
