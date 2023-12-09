input_file = "dec9_input.txt"
histories = []

def get_differences(values):
    return [values[i] - values[i - 1] for i in range(1, len(values))]
    
def predict(values):
    pyramid = [values]
    # construct difference pyramid
    while(not all(num == 0 for num in pyramid[-1])):
        pyramid.append(get_differences(pyramid[-1]))
    
    
    while len(pyramid) > 1:
        pyramid[-2].append(pyramid[-1][-1] + pyramid[-2][-1])
        pyramid[-2].insert(0, pyramid[-2][0] - pyramid[-1][0])

        pyramid.pop()
    return pyramid[0][0], pyramid[0][-1]

with open(input_file, "r") as text:
    data = text.read().split("\n")
    histories = [[int(num) for num in line.split()] for line in data]
    sum_before, sum_after = map(sum, zip(*(predict(history) for history in histories))) 
    print("part 1: " + str(sum_after))
    print("part 2: " + str(sum_before))
