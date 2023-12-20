def parse_monkey_data(monkey_data):
    product_of_divs = 1
    monkeys = []
    for i in range(len(monkey_data)):
        monkey = monkey_data[i]
        start = [int(level) for level in monkey[1].split(': ')[1].split(', ')]
        op = monkey[2].split(': new = ')[1]
        div = int(monkey[3].split('by ')[1])
        product_of_divs *= div
        true = int(monkey[4].split('monkey ')[1])
        false = int(monkey[5].split('monkey ')[1])
        monkeys.append([start, op, div, true, false, 0])
    return monkeys, product_of_divs

def simulate_rounds(monkeys, product_of_divs=None, rounds=20, p1=True):
    for round in range(rounds):
        for monkey in monkeys:
            monkey[5] += len(monkey[0]) # increase items handled count
            while monkey[0]:
                old = monkey[0].pop(0)
                op = monkey[1]
                new = eval(op)
                if p1:
                    new //= 3
                else:
                    new %= product_of_divs
                div = monkey[2]
                true = monkey[3]
                false = monkey[4]
                throw_monkey = true if (new % div == 0) else false
                monkeys[throw_monkey][0].append(new)

monkey_data = [monkey.split('\n') for monkey in open('input.txt').read().split('\n\n')]
monkeys, product_of_divs = parse_monkey_data(monkey_data)
simulate_rounds(monkeys)
monkeys.sort(key = lambda monkey: monkey[5], reverse=True)
p1 = monkeys[0][5] * monkeys[1][5]

monkeys, product_of_divs = parse_monkey_data(monkey_data)
simulate_rounds(monkeys, product_of_divs, 10000, False)
monkeys.sort(key = lambda monkey: monkey[5], reverse=True)
p2 = monkeys[0][5] * monkeys[1][5]

print('part 1: {}\npart 2: {}'.format(p1, p2))
