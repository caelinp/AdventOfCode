with open("dec6_input.txt", "r") as text:
    data = text.readlines()
    times = data[0].split()[1:]
    distances = data[1].split()[1:]
    print(times)
    print(distances)
    res = 1
    for i in range(len(times)):
        ways = 0
        for holdTime in range(1, int(times[i])):
            speed = holdTime
            time = int(times[i])
            if speed * (time - holdTime) > int(distances[i]):
                ways += 1
        res *= ways
    print(res)
