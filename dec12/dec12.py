def is_valid(solution, original):
    if len(solution) > len(original):
        return False
    for i in range(len(solution)):
        if original[i] != "?" and solution[i] != original[i]:
            return False
    return True
def unfold(data):
    for line in data:
        data[0] += (["?"] + data[0]) * 4
        data[1] += data[1] * 4
def count_arrangements(springs):
    arrangements = 0
    original = springs[0]
    groups = [int(group) for group in springs[1].split(',')]
    def backtrack(cur, groups):
        nonlocal arrangements
        nonlocal original
        if not is_valid(cur, original) or len(cur) == len(original) and groups:
            return
        if not groups:
            cur += "." * (len(original) - len(cur))
            arrangements += is_valid(cur, original)
            return
        while len(cur) < len(original):
            to_add = "#" * groups[0] 
            if len(groups) > 1:
                to_add += "." 
            backtrack(cur + to_add, groups[1:])
            cur += "."
    backtrack("", groups)
    return arrangements
        
data = [line.split() for line in open("example_input.txt").read().split("\n")]
unfold(data)
print(data)
arrangements_sum = 0
for line in data:
    arrangements_sum += count_arrangements(line)
print(arrangements_sum)
    


