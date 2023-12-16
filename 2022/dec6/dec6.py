def get_chars_before_start_of_packet(stream, n):
    last_n = []
    for i in range(len(stream)):
        if (c:=stream[i]) in last_n:
            last_n = last_n[last_n.index(c) + 1:] + [stream[i]]
        elif len(last_n) == n - 1:
            return i + 1
        else:
            last_n.append(stream[i])
            
stream = open("example_input.txt").read()

p1 = get_chars_before_start_of_packet(stream, 4)
p2 = get_chars_before_start_of_packet(stream, 14)

print("part 1: {}\npart 2: {}".format(p1, p2))