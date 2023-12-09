input_file = "dec9_input.txt"
histories = []

def all_zeroes(diffs):
    for diff in diffs:
        if diff:
            return False
    return True

def get_differences(values):
    differences = []
    for i in range(1, len(values)):
        differences.append(values[i] - values[i - 1])
    return differences

def predict_before(values):
    pyramid = [values]
    pyramid.append(get_differences(values))
    # construct difference pyramid
    while(not all_zeroes(pyramid[-1])):
        pyramid.append(get_differences(pyramid[-1]))
    while len(pyramid) > 1:
        pyramid[-2].insert(0, pyramid[-2][0] - pyramid[-1][0])
        pyramid.pop()
    return pyramid[0][0]

def predict_after(values):
    pyramid = [values]
    pyramid.append(get_differences(values))
    while(not all_zeroes(pyramid[-1])):
        pyramid.append(get_differences(pyramid[-1]))
    while len(pyramid) > 1:
        pyramid[-2].append(pyramid[-1][-1] + pyramid[-2][-1])
        pyramid.pop()
    return pyramid[0][-1]
    
with open(input_file, "r") as text:
    data = text.read().split("\n")
    for line in data:
        line = line.split()
        readings = []
        for num in line:
            readings.append(int(num))
        histories.append(readings)
    sum_before = 0
    sum_after = 0
    for history in histories:
        sum_before += predict_before(history)
        sum_after += predict_after(history)
    print("part 1: " + str(sum_after))
    print("part 2: " + str(sum_before))