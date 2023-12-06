# returns True if range r1 and r2 overlap, and false otherwise
def overlaps(r1, r2):
    return not (r1[0] > r2[1] or r2[0] > r1[1])

#returns True is range r1 is entirely inside r2, and false otherwise
def is_inside(r1, r2):
    return 


    
maps = []
seed_ranges = []
with open("dec5_example_input.txt", "r") as text:
    data = text.readlines()

    seeds = data[0].replace("seeds: ", "").replace("\n", "").split(" ")
    for i in range(0, len(seeds), 2):
        start = int(seeds[i])
        end = start + int(seeds[i + 1]) - 1
        seed_ranges.append([start, end])
    
    print(seed_ranges)
    # parsing out data:
    groups = "".join(data[1:]).split("\n\n")
    mapGroups = []
    mapGroupIdx = 0
    for group in groups:
        group = group.split("\n")
        print(group)
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
    print(mapGroups)

    mapQ = seed_ranges
    nextRanges = []
    for mapGroup in mapGroups:
        while mapQ:
            range = mapQ.pop()
            foundOverlap = False
            for map in mapGroup:
                if not overlaps(range, map["srcRange"]):
                    continue
                foundOverlap = True
                



    


                

        

'''
    for line in data[1: ]:
        if line == "\n":
            continue

        if "map:" in line:
            if map:
                maps.append(map.copy())
                map = []
        else:
            mapping = line.replace("\n", "").split(" ")
            map.append({"destStart": int(mapping[0]), "srcStart": int(mapping[1]), "range": int(mapping[2])})
    
    minLoc = float("infinity")
    i = 0
    while i < len(seeds):
        for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
            converted = seed
            for map in maps:
                before = converted
                for mapping in map:
                    #print("before: " + str(before))
                    #print("srcStart: " +  str(mapping["srcStart"]) + " range: " + str(mapping["range"]))
                    if converted >= mapping["srcStart"] and converted < mapping["srcStart"] + mapping["range"]:
            #            print("in range so converting")
                        difference = converted - mapping["srcStart"]
                        converted = mapping["destStart"] + difference
                        break
             #   print("converting " + str(before) + " to " + str(converted))
            #print("location: " + str(converted) + "\n")
            minLoc = min(minLoc, converted)
        i += 2
        
    print(minLoc)
'''
        
            


