def predict(pyramid):
    # construct difference pyramid
    while(any(pyramid[-1])):
        pyramid += [[pyramid[-1][i] - pyramid[-1][i - 1] for i in range(1, len(pyramid[-1]))]]
    # compute new first and last elements of each pyramid level and remove levels until 1 left. This will contain the a list of the two predicted values
    while len(pyramid) > 1:
        pyramid[-2] = [pyramid[-2][0] - pyramid[-1][0],  pyramid[-1][-1] + pyramid[-2][-1]]
        pyramid.pop()
    return reversed(pyramid[0])

# extract all histories into array
histories = [[int(num) for num in line.split()] for line in open("input.txt").read().split("\n")]
# Process each history and sum up the results
print("part 1: {}\npart 2: {}".format(*map(sum, zip(*([predict([history]) for history in histories])))))