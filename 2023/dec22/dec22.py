class Brick: 
    def __init__(self, brick):
        self.end1 = brick[0]
        self.end2 = brick[1]
        self.supby = set()
        self.sups = set()
        self.disint = True
    def inc_z(self):
        self.end1[2] += 1
        self.end2[2] += 1
    def dec_z(self):
        self.end1[2] -= 1
        self.end2[2] -= 1
    def get_max_z(self):
        return max(self.end1[2], self.end2[2])
    def get_min_z(self):
        return min(self.end1[2], self.end2[2])
    def __str__(self):
        return f'end1: {self.end1}, end2: {self.end2}, directly supports: {self.sups}, directly supported by: {self.supby}, can safely disintegrate: {self.disint}'

def would_bricks_overlap(b1, b2):
    return all([do_ranges_overlap(*ranges) for ranges in [[sorted([b1.end1[i], b1.end2[i]]), sorted([b2.end1[i], b2.end2[i]])] for i in range(3)]])

def do_ranges_overlap(r1, r2):
    return not (r1[0] > r2[1] or r2[0] > r1[1])

def drop_all_bricks_at_z(bricks, bricks_below, ids_to_bricks):
    [drop_brick(brick_id, bricks_below, ids_to_bricks) for brick_id in bricks]

def drop_brick(brick_id, bricks_below, ids_to_bricks):
    brick = ids_to_bricks[brick_id]
    while brick.get_min_z() > 1:
        brick.dec_z()
        z_min = brick.get_min_z()
        would_overlap = 0
        # if there are bricks at this index, check if we would overlap with any of them if current brick were to fall here
        # if there are no bricks at this index, we can definitely settle here or lower
        if z_min in bricks_below:
            for other_brick_id in bricks_below[z_min]:
                other_brick = ids_to_bricks[other_brick_id]
                if would_bricks_overlap(brick, other_brick):
                    pot_key_support = other_brick
                    # if this brick would overlap with the other brick, other brick might be a key support
                    brick.supby.add(other_brick_id)
                    other_brick.sups.add(brick_id)
                    would_overlap += 1
        if would_overlap > 0:
            if would_overlap == 1:
                pot_key_support.disint = False
            brick.inc_z()
            z_min += 1
            break
    z_max = brick.get_max_z()
    bricks_below[z_max] = bricks_below.get(z_max, set())
    bricks_below[z_max].add(brick_id)

def simulate_fall(all_bricks):
    # index all bricks with an id and initialize starting z index for all bricks
    ids_to_bricks, z_to_brick_ids = {}, {}
    for id, brick in enumerate(all_bricks):
        brick = Brick(brick)
        ids_to_bricks[id], z = brick, brick.get_max_z()
        z_to_brick_ids[z] = z_to_brick_ids.get(z, set())
        z_to_brick_ids[z].add(id)
    # go through all z indices, and for each brick, see how far we can lower it before it intersects with any bricks already settled at lower indices.
    z_to_brick_ids_fallen = {1 : z_to_brick_ids[1]}
    for z, brick_ids in z_to_brick_ids.items():
        # we don't have to simulate fall for any bricks already at z = 1 so skip
        if z == 1:
            continue
        # else simulate each brick at this level falling down as many levels as possible onto the settled levels
        drop_all_bricks_at_z(brick_ids, z_to_brick_ids_fallen, ids_to_bricks)
    return ids_to_bricks

def get_disintegrable(bricks):
    return len([brick for brick in bricks.values() if brick.disint])

def get_chain_reactions(bricks):
    def get_chain(brick_id, sups_removed):
        sups_removed.add(brick_id)
        for sup_id in bricks[brick_id].sups:
            sup_brick = bricks[sup_id]
            # Check if all supports of the sup brick are removed
            if sup_brick.supby.issubset(sups_removed):
                get_chain(sup_id, sups_removed)
        return len(sups_removed) - 1
    chain_sum = 0
    for id in bricks:
        chain_sum += get_chain(id, set())
    return chain_sum
bricks = simulate_fall(sorted([[[int(coord) for coord in end.split(',')] for end in line.split('~')] for line in open('input.txt').read().splitlines()], key=lambda b: max(b[0][2], b[1][2])))
print("part 1: {}\npart 2: {}".format(get_disintegrable(bricks), get_chain_reactions(bricks)))