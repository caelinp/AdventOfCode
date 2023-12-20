cycle = 0
x = 1
cycles_of_interest = set([20, 60, 100, 140, 180, 220])
p1 = 0
crt = [['.' for _ in range(40)] for _ in range(6)]
row = 0
crt_pos = 0
def draw_pixel(row, x, crt, cycle):
    crt_pos = cycle % 40  # Current drawing position of the CRT
    if crt_pos in [x - 1, x, x + 1]:
        crt[row][crt_pos] = '#'

for inst in open('input.txt').read().split('\n'):
    if 'addx' in inst:
        add_x = int(inst.split()[1])
        for _ in range(2):
            draw_pixel(row, x, crt, cycle)
            cycle += 1
            if cycle % 40 == 0:
                row += 1
            if cycle in cycles_of_interest:
                p1 += cycle * x

        x += add_x  # Update X after both cycles of addx

    else:  # noop case
        draw_pixel(row, x, crt, cycle)
        cycle += 1
        if cycle % 40 == 0:
            row += 1

        if cycle in cycles_of_interest:
            p1 += cycle * x

print('part 1: {}\npart 2'.format(p1))


# Print the CRT screen
for row in crt:
    print(''.join(row))
