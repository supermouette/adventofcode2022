from time import time
import functools

with open("input.txt", "r") as f:
    monkeys = [elf.split("\n") for elf in "".join(f.readlines()).split("\n\n")]


class Monkey:

    monkeys = []

    def __init__(self, input):
        self.id = int(input[0].split(" ")[1][:-1])
        self.items = list(map(int, input[1][len('  Starting items: '):].split(', ')))
        self.operation = lambda old: eval(input[2].split("=")[1])
        self.divisible_number = int(input[3].split(" ")[-1])
        self.divisible = lambda item: item % int(input[3].split(" ")[-1]) == 0
        self.toMonkey = {True: int(input[4].split(" ")[-1]), False: int(input[5].split(" ")[-1])}
        self.monkeys.append(self)
        self.inspected = 0

    def __repr__(self):
        return f"Monkey {self.id}: {self.items}"

    def play_turn(self):
        item_len = len(self.items)
        self.inspected += item_len
        for i in range(item_len):
            item = self.operation(self.items.pop(0)) % mod
            self.monkeys[self.toMonkey[self.divisible(item)]].items.append(item)


for monkey in monkeys:
    Monkey(monkey)

mod = functools.reduce(lambda a, b: a*b, [m.divisible_number for m in Monkey.monkeys])

t0 = time()
for turn in range(10000):
    if turn % 100 == 0:
        print(turn)
    for m in Monkey.monkeys:
        m.play_turn()

print(time() - t0)

inspected = [m.inspected for m in Monkey.monkeys]
inspected.sort(reverse=True)
monkey_business = inspected[0]*inspected[1]
print(monkey_business)
