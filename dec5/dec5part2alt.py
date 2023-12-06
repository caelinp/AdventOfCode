def map_range(src_start, src_end, map_rules):
    """ Maps a range of numbers using the provided mapping rules. """
    result = []
    for dest_start, map_start, length in map_rules:
        map_end = map_start + length - 1
        dest_end = dest_start + length - 1

        # Check if the ranges intersect
        if src_end >= map_start and src_start <= map_end:
            intersect_start = max(src_start, map_start)
            intersect_end = min(src_end, map_end)

            # Calculate the destination range based on the intersection
            offset = intersect_start - map_start
            result.append((dest_start + offset, dest_start + offset + intersect_end - intersect_start))
    
    # Default mapping for unmapped values
    if not result:
        return [(src_start, src_end)]
    
    return result

def apply_maps(seed_ranges, maps):
    """ Applies the mapping rules to the seed ranges. """
    for map_rules in maps:
        new_ranges = []
        for src_start, src_end in seed_ranges:
            new_ranges.extend(map_range(src_start, src_end, map_rules))
        seed_ranges = new_ranges
    return seed_ranges

# Read and parse the input file
with open("dec5_input.txt", "r") as text:
    data = text.read().splitlines()

# Processing seed ranges
seed_input = [int(x) for x in data[0].replace("seeds: ", "").split()]
seed_ranges = [(seed_input[i], seed_input[i] + seed_input[i + 1] - 1) for i in range(0, len(seed_input), 2)]

# Parsing mappings
maps = []
current_map = []
for line in data[1:]:
    if "map:" in line:
        if current_map:
            maps.append(current_map)
            current_map = []
    else:
        mapping = tuple(map(int, line.split()))
        current_map.append(mapping)
if current_map:
    maps.append(current_map)

# Apply the maps to the seed ranges
final_ranges = apply_maps(seed_ranges, maps)

# Find the minimum location
min_location = min(start for start, _ in final_ranges)
print(min_location)
