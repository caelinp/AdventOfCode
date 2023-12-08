input_file = "dec8_example_input.txt"
mapping = {}
with open(input_file, "r") as text:
    instructions, data = text.read().split("\n\n")
    instructions = list(instructions)
    data = data.split("\n")
    for line in data:
        node, children = line.split(" = ")
        children = children.replace("(", "").replace(")", "")
        children = children.split(", ")
        mapping[node] = children
    
    steps = 0
    node = "AAA"
    while node != "ZZZ":
        for step in instructions:
            if node == "ZZZ":
                break
            node = mapping[node][1 if step == 'R' else 0]
            steps += 1
    print(steps)

    