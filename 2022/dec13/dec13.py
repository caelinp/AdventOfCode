import functools

pairs = [[eval(packet) for packet in pair.split('\n')] for pair in open('input.txt').read().split('\n\n')]


def less_than(l, r):
    if type(l) is int and type(r) is int:
        if l < r:
            return 1
        elif l > r:
            return -1
        else:
            return 0
    if type(l) is list and type(r) is list:
        if l and not r:
            return -1
        elif not l and r:
            return 1
        elif not l and not r:
            return 0
        else:
            is_ordered = less_than(l[0], r[0])
            if is_ordered == 1:
                return 1
            elif is_ordered == 0:
                return less_than(l[1:], r[1:])
            elif is_ordered == -1:
                return -1
    if type(l) is int and type(r) is list:
        return less_than([l], r)
    if type(l) is list and type(r) is int:
        return less_than(l, [r])

p1 = 0
all_packets = [[[2]], [[6]]]
for i, pair in enumerate(pairs):
    l, r = pair
    all_packets.extend([l, r])
    if less_than(l, r) == 1:
         p1 += i + 1

key_func = functools.cmp_to_key(less_than)
all_packets.sort(key=key_func, reverse=True)
p2 = (all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1)
print(f"part 1: {p1}\npart 2: {p2}")

