def traverse_beam(r, c, dir):
    visited = {}
    beams = [(r, c, dir)]
    while beams:
        r, c, dir = beams.pop()
        while (0 <= r < len(layout)) and (0 <= c < len(layout[0])):
            dir_set = visited.get((r, c), set())
            dir_set.add(dir)
            visited[(r, c)] = dir_set
            thing = layout[r][c]
            if dir == 'L':
                if thing == '.' or thing == '-':
                    c -= 1
                if thing == '|':
                    beams.append((r - 1, c, 'U'))
                    dir = 'D'
                    r += 1
                if thing == '\\':
                    dir = 'U'
                    r -= 1
                if thing == '/':
                    dir = 'D'
                    r += 1
            elif dir == 'R':
                if thing == '.' or thing == '-':
                    c += 1
                if thing == '|':
                    beams.append((r - 1, c, 'U'))
                    dir = 'D'
                    r += 1
                if thing == '\\':
                    dir = 'D'
                    r += 1
                if thing == '/':
                    dir = 'U'
                    r -= 1
            elif dir == 'U':
                if thing == '.' or thing == '|':
                    r -= 1
                if thing == '-':
                    beams.append((r, c - 1, 'L'))
                    dir = 'R'
                    c += 1
                if thing == '/':
                    dir = 'R'
                    c += 1
                if thing == '\\':
                    dir = 'L'
                    c -= 1
            elif dir == 'D':
                if thing == '.' or thing == '|':
                    r += 1
                if thing == '-':
                    beams.append((r, c - 1, 'L'))
                    dir = 'R'
                    c += 1
                if thing == '/':
                    dir = 'L'
                    c -= 1
                if thing == '\\':
                    dir = 'R'
                    c += 1
            if (r, c) in visited and dir in visited[(r, c)]:
                break
    return len(visited)

layout = [list(row) for row in open("input.txt").read().split('\n')]
p1 = traverse_beam(0, 0, 'R')

max_energized = 0
for i in range(len(layout)):
    max_energized = max(max_energized, traverse_beam(i, 0, 'R'), traverse_beam(i, len(layout[0])- 1, 'L'))
for j in range(len(layout[0])):
    max_energized = max(max_energized, traverse_beam(0, j, 'D'), traverse_beam(len(layout) - 1, j, 'U'))
p2 = max_energized
print("part 1: {}\npart 2: {}".format(p1, p2))
