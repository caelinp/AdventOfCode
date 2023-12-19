def get_rule_index_from_effect(rules, effect):
    for i, rule in enumerate(rules):
        if rule[1] == effect:
            return i

workflow_lines, parts = [section.split('\n') for section in open('input.txt').read().split('\n\n')]
workflows = {}
accept_workflows = []

for workflow in workflow_lines:
    label, rules  = workflow.strip('}').split('{')
    rules = rules.split(',')
    rules_parsed = []
    for i, rule in enumerate(rules):
        condition, effect = (None, rule) if ':' not in rule else rule.split(':')
        if effect == 'A':
            accept_workflows.append((label, i))
        elif effect != 'R':
            child = effect
            if child in workflows:
                workflows[child][1] = label
            else:
                workflows[child] = [None, label]
        rules_parsed.append([condition, effect])
    if label in workflows:
        workflows[label][0] = rules_parsed
    else:
        workflows[label] = [rules_parsed, None]

p2 = 0
for (label, rule_idx) in accept_workflows:
    ranges = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
    rules, parent = workflows[label]
    desired_effect = 'A'
    while True:
        for i in range(rule_idx, -1, -1):
            rule = rules[i]
            condition, effect = rule
            if condition:
                if '>' in condition:
                    rating, limit = condition.split('>')
                    comp = '>'
                else:
                    rating, limit = condition.split('<')
                    comp = '<'
                limit = int(limit)
                # if i is not rule idx, then condition must be false, since we are working backward from rule idx
                if i != rule_idx:
                    # condition needs to be false
                    if comp == '>':
                        ranges[rating][1] = min(limit, ranges[rating][1])
                    else: # '<'
                        ranges[rating][0] = max(limit, ranges[rating][0])
                # else i is rule idx, so this condition must be true
                else:
                    # condition needs to be true
                    if comp == '>':
                        ranges[rating][0] = max(limit + 1, ranges[rating][0])
                    else: # '<'
                        ranges[rating][1] = min(limit  - 1, ranges[rating][1])
        desired_effect = label
        label = parent
        if not label:
            break
        rules, parent = workflows[label]
        rule_idx = get_rule_index_from_effect(rules, desired_effect)
    combos = 1
    for r in ranges.values():
        combos *= r[1] - r[0] + 1
    p2 += combos

p1 = 0
part_idx = 0
next_part = True
while part_idx < len(parts):
    part = parts[part_idx]
    x, m, a, s = [int((val.replace('{', '').replace('}', '')).split('=')[1]) for val in part.split(',')]
    if next_part:
        rules = workflows['in'][0]
    for rule in rules:
        condition, effect = rule
        if not condition or eval(condition):
            if effect == 'A':
                p1 += x + m + a + s
                next_part = True
                part_idx += 1
            elif effect == 'R':
                next_part = True
                part_idx += 1
            else:
                next_part = False
                rules = workflows[effect][0]
            break
print("part 1: {}\npart 2: {}".format(p1, p2))


