def preprocess_map(mapping_list):
    """ Preprocesses a list of mappings into a direct mapping dictionary. """
    direct_map = {}
    for mapping in mapping_list:
        dest_start, src_start, range_length = mapping.values()
        for i in range(range_length):
            direct_map[src_start + i] = dest_start + i
    return direct_map

def find_minimum_location(seeds, maps):
    """ Finds the minimum location number for the given seeds and maps. """
    # Preprocess all maps into direct mappings
    direct_maps = [preprocess_map(map) for map in maps]

    min_location = float("infinity")

    # Iterate through each seed and find its corresponding location
    for seed in seeds:
        converted = seed
        for direct_map in direct_maps:
            converted = direct_map.get(converted, converted)
        min_location = min(min_location, converted)

    return min_location

# Read and parse the input file
with open("dec5_input.txt", "r") as text:
    data = text.read().splitlines()

# Processing seed ranges
seed_ranges = [int(x) for x in data[0].replace("seeds: ", "").split()]
seeds = set()
for i in range(0, len(seed_ranges), 2):
    start, length = seed_ranges[i], seed_ranges[i+1]
    seeds.update(range(start, start + length))

# Parsing mappings
maps = []
current_map = []
for line in data[1:]:
    if "map:" in line:
        if current_map:
            maps.append(current_map)
            current_map = []
    else:
        mapping = {k: int(v) for k, v in zip(["destStart", "srcStart", "range"], line.split())}
        current_map.append(mapping)
if current_map:
    maps.append(current_map)

# Find the minimum location
min_location = find_minimum_location(seeds, maps)
print(min_location)
