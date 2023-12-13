# returns True if range r1 and r2 overlap, and false otherwise
def overlaps(r1, r2):
    return not (r1[0] > r2[1] or r2[0] > r1[1])

# returns True is range r1 is entirely inside r2, and false otherwise
def is_inside(r1, r2):
    return r1[0] >= r2[0] and r1[1] <= r2[1]

# returns a new range that is the range r, offset by the difference between dest and start in the given mapping
def convert_range(r, mapping):
    offset = mapping["destRange"][0] - mapping["srcRange"][0]
    return [r[0] + offset, r[1] + offset]

# returns a list of two ranges, which are range r split at an overlap point. This should only be called if the range and mapping's src range have an overlap, and range is not completely inside
# the src range
def split_range(range, map):
    rStart, rEnd = range[0], range[1]
    sStart, sEnd = map["srcRange"][0], map["srcRange"][1]

    # in the case where the src range is totally contained within the range r, the first case will be taken
    # there will still be an overlap between the mapping's source range and the ranges returned from this function,
    # but they will be caught and split again according to the second case, the next time this function is called.

    # in this case, the right side of range r overlaps with the left side of the src range of the mapping
    # we need to partition r based on the starting value of the src range
    if rStart < sStart:
        return [[rStart, sStart - 1], [sStart, rEnd]]
    # else the left side of r overlaps with the right side of the src range
    # we need to partition r based on the ending value of the src range
    else:
        return [[rStart, sEnd], [sEnd + 1, rEnd]]

def get_min_location(seed_ranges, map_groups):
    # iterate through all mapping levels in the map_groups
    map_q = seed_ranges
    for map_group in map_groups:
        # keep processing mappings at this level until all overlaps are detected and ranges are split
        next_ranges = []
        while map_q:
            range = map_q.pop(0)
            found_overlap = False
            for map in map_group:
                # do nothing if the range does not overlap with the src range we're checking
                if not overlaps(range, map["srcRange"]):
                    continue
                # else there is some kind of overlap
                found_overlap = True
                # if range is completely inside the mapping's src range, we can convert the range and add it to the next ranges to be processed by the next map group
                if is_inside(range, map["srcRange"]):
                    next_ranges.append(convert_range(range, map))
                # else there are more complex overlaps, and some splitting has to be done of the range, and these splits need to be put back in the queue for further processing
                else:
                    map_q.extend(split_range(range, map))
                # if an overlap was detected, we don't need to keep comparing the range against more mappings, as its been either split up or converted
                # so break here
                break
            # if no overlap of the range was detected in all the mappings, then there was no mapping for this range, so add it to the next ranges to be be processed by the next map group
            if not found_overlap:
                next_ranges.append(range)
        # now that the map_q is empty, fill it with all the next ranges to be processed by the next map group
        map_q = next_ranges
    # the ranges in the final map_q after all map groups were processed, are the possible location ranges
    locations = map_q
    # the minimum location will be the start value of one of the ranges in the locations array
    return min(r[0] for r in locations)

data = [group.split("\n") for group in open("input.txt").read().split("\n\n")]
seeds = [int(seed) for seed in data[0][0].split()[1:]]
map_groups = []
for group in data[1:]:
    maps = []
    for line in group[1:]:
        if line:
            nums = [int(num) for num in line.split()]
            maps.append({"srcRange" : [nums[1], nums[1] + nums[2] - 1], "destRange" : [nums[0], nums[0] + nums[2] - 1]})
    map_groups.append(maps)

seed_ranges = [[seed, seed] for seed in seeds]
p1 = get_min_location(seed_ranges, map_groups)
seed_ranges = [[seeds[i], seeds[i] + seeds[i + 1] - 1] for i in range(0, len(seeds), 2)]
p2 = get_min_location(seed_ranges, map_groups)
# map_q stores all the ranges at one level, that have yet to be compared against ranges in the next mapping level
# if ranges overlap with ranges in the next mapping level, they are split along the overlap points and put back into the map queue

print("part 1: {}\npart 2: {}".format(p1, p2))


