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

# returns a list of two ranges, which are range r split at the overlap point
def split_range(range, map):
    rStart, rEnd = range[0], range[1]
    sStart, sEnd = map["srcRange"][0], map["srcRange"][1]

    if rStart < sStart:
        return [[rStart, sStart - 1], [sStart, rEnd]]
    else:
        return [[rStart, sEnd], [sEnd + 1, rEnd]]


maps = []
seed_ranges = []
with open("dec5_input.txt", "r") as text:
    data = text.readlines()

    seeds = data[0].replace("seeds: ", "").replace("\n", "").split(" ")
    for i in range(0, len(seeds), 2):
        start = int(seeds[i])
        end = start + int(seeds[i + 1]) - 1
        seed_ranges.append([start, end])
    
    #print(seed_ranges)
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
    #print(mapGroups)

    mapQ = seed_ranges
    nextRanges = []

    for mapGroup in mapGroups:
        while mapQ:
            range = mapQ.pop(0)
            foundOverlap = False
            for map in mapGroup:
                if not overlaps(range, map["srcRange"]):
                    continue
                foundOverlap = True
                if is_inside(range, map["srcRange"]):
                    nextRanges.append(convert_range(range, map))
                else:
                    mapQ.extend(split_range(range, map))
                break
            if not foundOverlap:
                nextRanges.append(range)
        mapQ = nextRanges
        nextRanges = []
    
    locations = mapQ
    minLocation = min(r[0] for r in mapQ)
    print(minLocation)

