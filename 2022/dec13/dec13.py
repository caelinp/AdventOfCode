import functools

pairs = [[eval(packet) for packet in pair.split('\n')] for pair in open('input.txt').read().split('\n\n')]


def is_less_than(l, r):
    if type(l) is int and type(r) is int:
        if l < r:
            return True
        elif l > r:
            return False
        else:
            return None
    if type(l) is list and type(r) is list:
        if l and not r:
            return False
        elif not l and r:
            return True
        elif not l and not r:
            return None
        else:
            if (is_ordered := is_less_than(l[0], r[0])):
                return True
            elif is_ordered == None:
                return is_less_than(l[1:], r[1:])
            elif is_ordered == False:
                return False
    if type(l) is int and type(r) is list:
        return is_less_than([l], r)
    if type(l) is list and type(r) is int:
        return is_less_than(l, [r])

def is_greater_than(l, r):
    val = is_less_than(l, r)
    if val == True:
        return -1
    if val == None:
        return 0
    else:
        return 1

p1 = 0
all_packets = [[[2]], [[6]]]
for i, pair in enumerate(pairs):
    l, r = pair
    all_packets.extend([l, r])
    if is_less_than(l, r):
         p1 += i + 1

key_func = functools.cmp_to_key(is_greater_than)
all_packets.sort(key=key_func)
p2 = (all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1)
print(f"part 1: {p1}\npart 2: {p2}")

