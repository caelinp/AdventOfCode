
def get_visible_trees(trees):
    visible = set()
    for r in range(1, len(trees) - 1):
        max_height_idx = 0
        for c in range(1, len(trees[0]) - 1):
            if (height := int(trees[r][c])) > int(trees[r][max_height_idx]):
                visible.add((r, c))
                max_height_idx = c

        max_height_idx = len(trees[0]) - 1
        for c in range(len(trees[0]) - 2, 0, -1):
            if (height := int(trees[r][c])) > int(trees[r][max_height_idx]):
                visible.add((r, c))
                max_height_idx = c

    for c in range(1, len(trees[0]) - 1):
        max_height_idx = 0
        for r in range(1, len(trees) - 1):
            if (height := int(trees[r][c])) > int(trees[max_height_idx][c]):
                visible.add((r, c))
                max_height_idx = r   

        max_height_idx = len(trees) - 1
        for r in range(len(trees) - 2, 0, -1):
            if (height := int(trees[r][c])) > int(trees[max_height_idx][c]):
                visible.add((r, c))
                max_height_idx = r
    return len(visible) + len(trees) * 2 + len(trees[0]) * 2 - 4

def get_max_scenic_score(trees):
    max_score = 0
    north_limit, east_limit, south_limit, west_limit = 0, 0, 0, 0
    for r in range(1, len(trees) - 1):
        for c in range(1, len(trees) - 1):
            score = 1
            height = trees[r][c]

            north_limit = r - 1
            while north_limit > 0 and height > trees[north_limit][c]:
                north_limit -= 1
            val = r - north_limit
            if val == 0:
                break
            score *= val

            south_limit = r + 1
            while south_limit < len(trees) - 1 and height > trees[south_limit][c]:
                south_limit += 1
            val = south_limit - r
            if val == 0:
                break
            score *= val

            west_limit = c - 1
            while west_limit > 0 and height > trees[r][west_limit]:
                west_limit -= 1
            val = c - west_limit
            if val == 0:
                break
            score *= val
            east_limit = c + 1
            while east_limit < len(trees[0]) - 1 and height > trees[r][east_limit]:
                east_limit += 1
            val = east_limit - c
            if val == 0:
                break
            score *= val
            max_score = max(max_score, score)
    return max_score


trees = open("input.txt").read().split('\n')
p1 = get_visible_trees(trees)
p2 = get_max_scenic_score(trees)

print('part 1: {}\npart 2: {}'.format(p1, p2))
