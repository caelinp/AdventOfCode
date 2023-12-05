# Open the file named 'calsum_inputs.txt' in read mode
with open('calsum_inputs.txt', 'r') as file:
    # Read the contents of the file
    contents = file.readlines()
    res = 0
    for line in contents:
        l = 0
        r = len(line) - 1
        # find left digit
        while not line[l].isnumeric():
            l += 1
        # find right digit
        while not line[r].isnumeric():
            r -= 1
        number = int(line[l]) * 10 + int(line[r])
        print(number)
        res += number
    print(res)

