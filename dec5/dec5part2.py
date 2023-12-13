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


maps = []
seed_ranges = []
with open("input.txt", "r") as text:
    data = text.readlines()

    seeds = data[0].replace("seeds: ", "").replace("\n", "").split(" ")
    for i in range(0, len(seeds), 2):
        start = int(seeds[i])
        end = start + int(seeds[i + 1]) - 1
        seed_ranges.append([start, end])
    
    # parsing out data:
    groups = "".join(data[1:]).split("\n\n")
    mapGroups = []
    mapGroupIdx = 0
    for group in groups:
        group = group.split("\n")
        cleaned_lines = []
        for line in group:
            if line != '':
                cleaned_lines.append(line)
        mapGroups.append([])
        for line in cleaned_lines[1:]:
            dest, source, range = line.split(' ')
            dest, source, range = int(dest), int(source), int(range)
            mapGroups[mapGroupIdx].append({"srcRange": [source, source + range - 1], "destRange": [dest, dest + range - 1]})
        mapGroupIdx += 1

    # mapQ stores all the ranges at one level, that have yet to be compared against ranges in the next mapping level
    # if ranges overlap with ranges in the next mapping level, they are split along the overlap points and put back into the map queue
    mapQ = seed_ranges

    # iterate through all mapping levels in the mapGroups
    for mapGroup in mapGroups:
        # keep processing mappings at this level until all overlaps are detected and ranges are split
        nextRanges = []
        while mapQ:
            range = mapQ.pop(0)
            foundOverlap = False
            for map in mapGroup:
                # do nothing if the range does not overlap with the src range we're checking
                if not overlaps(range, map["srcRange"]):
                    continue
                # else there is some kind of overlap
                foundOverlap = True
                # if range is completely inside the mapping's src range, we can convert the range and add it to the next ranges to be processed by the next map group
                if is_inside(range, map["srcRange"]):
                    nextRanges.append(convert_range(range, map))
                # else there are more complex overlaps, and some splitting has to be done of the range, and these splits need to be put back in the queue for further processing
                else:
                    mapQ.extend(split_range(range, map))
                # if an overlap was detected, we don't need to keep comparing the range against more mappings, as its been either split up or converted
                # so break here
                break
            # if no overlap of the range was detected in all the mappings, then there was no mapping for this range, so add it to the next ranges to be be processed by the next map group
            if not foundOverlap:
                nextRanges.append(range)
        # now that the mapQ is empty, fill it with all the next ranges to be processed by the next map group
        mapQ = nextRanges
    
    # the ranges in the final mapQ after all map groups were processed, are the possible location ranges
    locations = mapQ
    # the minimum location will be the start value of one of the ranges in the locations array
    minLocation = min(r[0] for r in locations)
    print(minLocation)

