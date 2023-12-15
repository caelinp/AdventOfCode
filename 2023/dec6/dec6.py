import math

def get_winning_range(time, distance):
    # quadratic function: ax^2 + bx + c where x is time button is held down, a is 1, b is -time, c is the distance
    sqrt_discriminant = math.sqrt(time**2 - 4*distance)

    root1 = (time + sqrt_discriminant) / 2
    root2 = (time - sqrt_discriminant) / 2
    start = math.ceil(min(root1, root2))
    end = math.floor(max(root1, root2))

    return max(0, end - start + 1)

times, distances = [val.split()[1:] for val in open("input.txt").read().split("\n")]
res = [1, 0]
for i in range(len(times)):
    # part 1: product of all ways to win for all races:
    res[0] *= get_winning_range(int(times[i]), int(distances[i]))

# part 2: taking input as values for one race:
res[1] = get_winning_range(int("".join(times)), int("".join(distances)))
print("part 1: {}\npart 2: {}".format(*res))
