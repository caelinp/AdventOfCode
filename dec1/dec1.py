numbers = {"one": "1",
           "two": "2",
           "three": "3",
           "four": "4",
           "five": "5",
           "six": "6",
           "seven": "7",
           "eight": "8",
           "nine": "9"}

# add a helper function that checks if a substring in a string matches the word for a number, given the starting index of the substring
# returns the value of the number if the substring matches a number and returns None if it does not
def isNumber(s, i):
    for num in numbers:
        # if a substring from index i and is the length of the number word would bring us past the end of the string, this does nothing. else check for match in numbers
        if len(s) >= i + len(num) and s[i:i + len(num)] == num:
           return numbers[num]
    return None

res = [0, 0]
for line in open("input.txt").read().split("\n"):
    # part 1:
    # find left digit
    for l in range(0, len(line)):
        if (l_digit := line[l]).isnumeric():
            break
    # find right digit
    for r in range(len(line) - 1, -1, -1):
        if (r_digit := line[r]).isnumeric():
            break
    res[0] += int(l_digit + r_digit)
    
    # part 2:
    # find left digit
    for l in range(0, len(line)):
        if (l_digit := line[l]).isnumeric() or (l_digit := isNumber(line, l)):
            break
    # find right digit
    for r in range(len(line) - 1, -1, -1):
        if (r_digit := line[r]).isnumeric() or (r_digit := isNumber(line, r)):
            break
    res[1] += int(l_digit + r_digit)
print("part 1: {}\npart 2: {}".format(*res))



