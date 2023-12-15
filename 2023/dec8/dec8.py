from math import gcd
instructions, data = open("input.txt").read().split("\n\n")
mapping = {}
starting_nodes = []
for line in data.split("\n"):
    node, children = line.split(" = ")
    mapping[node] = children.replace("(", "").replace(")", "").split(", ")
    if node[2] == "A":
        starting_nodes.append(node)
# part 1
steps = 0
node = "AAA"
while node != "ZZZ":
    for step in instructions:
        if node == "ZZZ":
            break
        node = mapping[node][1 if step == 'R' else 0]
        steps += 1
# part 2
step_counts = []
for node in starting_nodes:
    steps = 0
    while node[2] != "Z":
        for step in instructions:
            if node[2] == "Z":
                break
            node = mapping[node][1 if step == 'R' else 0]
            steps += 1
    step_counts.append(steps)
lcm = 1
for steps in step_counts:
    lcm = lcm * steps // gcd(lcm, steps)
print("part 1: {}\npart 2: {}".format(steps, lcm))