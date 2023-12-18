def parse_step(step, p1=False):
    if p1:
        dir, dist = step.split()[:-1]
        dist = int(dist)
        dr, dc = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}[dir]
    else:
        step = step.split()[-1]
        dir = step[-2]
        dist = int(step[2:-2], 16)
        dr, dc = {'0': (0, 1), '1': (1, 0), '2': (0, -1), '3': (-1, 0)}[dir]
    return dist, (dr, dc)

    
def get_dig_vertices_and_edge_area(steps, p1=False):
    x, y = 0, 0
    vertices = []
    perimeter = 0
    for step in steps:
        dist, (dr, dc) = parse_step(step, p1)
        perimeter += dist
        x += dc * dist
        y += dr * dist
        vertices.append((x, y))
    return vertices, perimeter / 2 + 1

def calculate_area(vertices):
    area = 0
    for i in range(len(vertices)):
        x0, y0 = vertices[i]
        x1, y1 = vertices[(i + 1) % len(vertices)]  # Wrap around to the first point
        area += (x0 * y1) - (x1 * y0)
    return abs(area) / 2

steps = open('input.txt').read().split('\n')
vertices, edge_area = get_dig_vertices_and_edge_area(steps, True)
area_interior = calculate_area(vertices)
p1 = int(area_interior + edge_area)
vertices, edge_area = get_dig_vertices_and_edge_area(steps)
area_interior = calculate_area(vertices)
p2 = int(area_interior + edge_area)
print("part 1: {}\npart 2: {}".format(p1, p2))