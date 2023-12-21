def get_start(garden):
    for r, row in enumerate(garden):
        for c, val in enumerate(row):
            if val == 'S':
                return r, c
            
def get_plots_from_steps(garden, steps):
    height, width = len(garden), len(garden[0])
    plots = {get_start(garden)}
    points = []
    for step in range(1, steps):
        new_plots = set()
        for plot in plots:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r = (plot[0] + dr) 
                c = (plot[1] + dc)
                if garden[r % height][c % width] in '.S':
                    new_plots.add((r, c))
        plots = new_plots
        if step == 64:
            p1 = len(plots)
        if step % width == steps % width:
            points.append(len(plots))
        if len(points) == 3:
            break
    def f(n):
        y0, y1, y2 = points
        a = (y2 + y0 - 2 * y1) / 2
        b = y1 - y0 - a
        c = y0
        return int(a * n ** 2 + b * n + c )
    p2 = f(steps // width)
    return p1, p2
# Load the garden from the file
garden = [[plot for plot in row] for row in open('input.txt').read().splitlines()]
total_steps = 26501365
p1, p2 = get_plots_from_steps(garden, total_steps)
print("part 1: {}\npart 2: {}".format(p1, p2))
