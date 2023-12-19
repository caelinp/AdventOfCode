cycle = 0
x = 1
next_x = 0
cycles_of_interest = set([20, 60, 100, 140, 180, 220])
p1 = 0
for inst in open('input.txt').read().split('\n'):
    if 'addx' in inst:
        add_x = int(inst.replace('addx ', ''))
        for i in range(2):
            cycle += 1
            if cycle in cycles_of_interest:
                p1 += cycle * x
        x += add_x
    else:
        cycle += 1
        if cycle in cycles_of_interest:
            p1 += cycle * x
print(p1)
