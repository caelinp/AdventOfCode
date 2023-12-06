with open("dec6_input.txt", "r") as text:
    data = text.readlines()
    times = data[0].split()[1:]
    time = int("".join(times))
    print(time)
    distances = data[1].split()[1:]
    distance = int("".join(distances))
    print(distance)
    ways = 0
    start = 0
    end = 0
    for holdTime in range(1, time):
        speed = holdTime
        if speed * (time - holdTime) > distance:
            start = holdTime
            break
    for holdTime in range(time - 1, 1, -1):
        speed = holdTime
        if speed * (time - holdTime) > distance:
            end = holdTime
            break
    
    
    print(end - start + 1)
