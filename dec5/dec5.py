seeds = set()
maps = []
with open("dec5_input.txt", "r") as text:
    data = text.readlines()

    seeds = data[0].replace("seeds: ", "").replace("\n", "").split(" ")
    for i in range(len(seeds)):
        seeds[i] = int(seeds[i])
    
    print(seeds)
    
    # parsing out data:
    map = []
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
    maps.append(map)
    minLoc = float("infinity")
    for seed in seeds:
        converted = seed
        for map in maps:
            before = converted
            for mapping in map:
                #print("before: " + str(before))
                #print("srcStart: " +  str(mapping["srcStart"]) + " range: " + str(mapping["range"]))
                if converted >= mapping["srcStart"] and converted < mapping["srcStart"] + mapping["range"]:
                    print("in range so converting")
                    difference = converted - mapping["srcStart"]
                    converted = mapping["destStart"] + difference
                    break
            print("converting " + str(before) + " to " + str(converted))
        print("location: " + str(converted) + "\n")
        minLoc = min(minLoc, converted)
    
    print(minLoc)

        
            


