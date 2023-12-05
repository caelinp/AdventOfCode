# Open the file named 'calsum_inputs.txt' in read mode
numbers = {"one": 1,
           "two": 2,
           "three": 3,
           "four": 4,
           "five": 5,
           "six": 6,
           "seven": 7,
           "eight": 8,
           "nine": 9}

# add a helper function that checks if a substring in a string matches the word for a number, given the starting index of the substring
# returns the value of the number if the substring matches a number and returns None if it does not
def isNumber(s, i):
    for num in numbers:
        # if a substring from index i and is the length of the number word would bring us past the end of the string, continue
        if len(s) <  i + len(num):
            continue
        # else we can check if the substring matches a number word:
        elif s[i:i + len(num)] == num:
            return numbers[num]
    return None
        
    
with open('calsum_inputs.txt', 'r') as file:
    # Read the contents of the file
    contents = file.readlines()
    res = 0
    for line in contents:
        l = 0
        r = len(line) - 1
        lDigit = None
        rDigit = None
        # find left digit
        while True:
            if line[l].isnumeric():
                lDigit = line[l]
                break
            lDigit = isNumber(line, l)
            if lDigit:
                break
            l += 1
        # find right digit
        while True:
            if line[r].isnumeric():
                rDigit = line[r]
                break
            rDigit = isNumber(line, r)
            if rDigit:
                break
            r -= 1
        number = int(lDigit) * 10 + int(rDigit)
        print(number)
        res += number
    print(res)

