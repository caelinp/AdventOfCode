from math import gcd
input_file = "dec8_input.txt"
mapping = {}

with open(input_file, "r") as text:
    instructions, data = text.read().split("\n\n")
    instructions = list(instructions)
    data = data.split("\n")
    starting_nodes = []
    for line in data:
        node, children = line.split(" = ")
        children = children.replace("(", "").replace(")", "")
        children = children.split(", ")
        mapping[node] = children
        if node[2] == "A":
            starting_nodes.append(node)
    
    step_counts = []
    nodes = starting_nodes
    for node in starting_nodes:
        steps = 0
        while node[2] != "Z":
            for step in instructions:
                if node[2] == "Z":
                    break
                node = mapping[node][1 if step == 'R' else 0]
                steps += 1
        step_counts.append(steps)
    print(step_counts)
    lcm = 1
    for steps in step_counts:
        lcm = lcm * steps // gcd(lcm, steps)
    print(lcm)

    