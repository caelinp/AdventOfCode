boxes_layout, steps = open("example_input.txt").read().split("\n\n")
stacks = {}
for j in range(len(boxes_layout[0])):
    boxes_layout = boxes_layout.split('\n')
    stack_num = boxes_layout[-1][j]
    print(stack_num)
    if stack_num.isnumeric():
        stacks[stack_num] = []
        for i in range(len(boxes_layout) - 1):
            if (ord('A') <= ord(box := boxes_layout[i][j]) <= ord('Z')):
                stacks[box] = [box] + stacks.get(j, [])
    
print(stacks)
        