import matplotlib.pyplot as plt

with open("input.txt", "r") as f:
    monkeys_raw = [line.strip('\n').split(" ") for line in f.readlines()]

monkeys = {}
monkeys_done = {}

for m in monkeys_raw:
    if len(m) == 2:
        if m[0] == "humn:":
            monkeys_done[m[0][:-1]] = "a"
        else:
            monkeys_done[m[0][:-1]] = int(m[1])
    else:
        monkeys[m[0][:-1]] = m[1:]

ops = {"+": lambda a,b: a+b, "-": lambda a,b: a-b, "*":lambda a,b: a*b, "/": lambda a,b: a//b}

final_stuff = []

while monkeys:
    to_delete = []
    for m in monkeys:
        monkey = monkeys[m]
        if monkey[0] in monkeys_done and monkey[2] in monkeys_done:
            if m=="root":
                print("root", monkey)
                print(monkeys_done[monkey[0]], monkeys_done[monkey[2]])
                if type(monkeys_done[monkey[0]]) == int:
                    final_stuff = [monkeys_done[monkey[0]], monkeys_done[monkey[2]]]
                else:
                    final_stuff = [monkeys_done[monkey[2]], monkeys_done[monkey[0]]]
            if type(monkeys_done[monkey[0]]) != int or type(monkeys_done[monkey[2]]) != int:
                monkeys_done[m] = f"({monkeys_done[monkey[0]]} {monkey[1]} {monkeys_done[monkey[2]]})"
            else:
                monkeys_done[m] = ops[monkey[1]](monkeys_done[monkey[0]], monkeys_done[monkey[2]])
            to_delete.append(m)
    for m in to_delete:
        del monkeys[m]

print(final_stuff)
operation = lambda a: eval(final_stuff[1])

nb = 100000

print(final_stuff[0], operation(0))
print(final_stuff[0], operation(10000000000000))
val = final_stuff[0]

min_val = 0
max_val = 10000000000000
while True:
    next_val = min_val + (max_val-min_val)//2
    res = operation(next_val)
    if res == val:
        print(next_val)
        exit()
    elif res > val:
        min_val = next_val
    else:
        max_val = next_val