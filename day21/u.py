with open("input.txt", "r") as f:
    monkeys_raw = [line.strip('\n').split(" ") for line in f.readlines()]

monkeys = {}
monkeys_done = {}

for m in monkeys_raw:
    if len(m) == 2:
        monkeys_done[m[0][:-1]] = int(m[1])
    else:
        monkeys[m[0][:-1]] = m[1:]

ops = {"+": lambda a,b: a+b, "-": lambda a,b: a-b, "*":lambda a,b: a*b, "/": lambda a,b: a//b}

while monkeys:
    to_delete = []
    for m in monkeys:
        monkey = monkeys[m]
        if monkey[0] in monkeys_done and monkey[2] in monkeys_done:
            monkeys_done[m] = ops[monkey[1]](monkeys_done[monkey[0]], monkeys_done[monkey[2]])
            to_delete.append(m)
    for m in to_delete:
        del monkeys[m]

print(monkeys_done["root"])