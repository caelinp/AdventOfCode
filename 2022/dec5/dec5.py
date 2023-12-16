
def build_stacks(boxes_layout):
    stacks = {}
    for j in range(len(boxes_layout[0])):
        if (stack_num := boxes_layout[-1][j]).isnumeric():
            stacks[stack_num] = []
            i = len(boxes_layout) - 2
            while ord('A') <= ord(box := boxes_layout[i][j]) <= ord('Z'):
                stacks[stack_num].append(box)
                i -= 1
    return stacks

def get_step_details(step):
    num_boxes = int(step.split(' from ')[0].replace('move ', ''))
    source, dest = step.split(' from ')[1].split(' to ')
    return num_boxes, source, dest

def move_boxes_one_by_one(steps, stacks):
    for step in steps:
        num_boxes, source, dest = get_step_details(step)
        for _ in range(num_boxes):
            stacks[dest].append(stacks[source].pop())
    return ''.join([stack[-1] for stack in stacks.values()])

def move_boxes_all_at_once(steps, stacks):
    for step in steps:
        num_boxes, source, dest = get_step_details(step)
        stacks[dest] += stacks[source][-num_boxes:]
        stacks[source] = stacks[source][:-num_boxes]
    return ''.join([stack[-1] for stack in stacks.values()])
    
boxes_layout, steps = [section.split('\n') for section in open("input.txt").read().split("\n\n")]
stacks = build_stacks(boxes_layout)
p1 = move_boxes_one_by_one(steps, stacks)
stacks = build_stacks(boxes_layout)
p2 = move_boxes_all_at_once(steps, stacks)
print("part 1: {}\npart 2: {}".format(p1, p2))
