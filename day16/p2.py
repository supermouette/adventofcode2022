from random import random, randrange
from time import time
t0 = time()
with open("input.txt", "r") as f:
    valves = eval(f.readline())

max_pressure = 0
iter_max = 10000000000
for i in range(iter_max):
    if i % (iter_max // 100) == 0:
        print(i/iter_max)
    previous = ['AA', 'AA']
    current = ['AA', 'AA']
    opened = set()
    minutes = 26
    pressure = 0
    while minutes >= 0:
        for move in range(len(["me", "an elephant"])):
            valve = valves[current[move]]
            if valve[0] != 0 and current[move] not in opened and random() > 0.15:
                opened.add(current[move])
                pressure += (max(0,minutes-1))*valves[current[move]][0]
            else:
                choices = valve[1][:]
                if random() > 0.05 and previous[move] in choices and len(choices) > 1:
                    choices.remove(previous[move])
                if random() > 0.20 and move == 1 and current[0] in choices and len(choices) > 1:
                    choices.remove(current[0])
                previous[move] = current[move]
                current[move] = choices[randrange(0, len(choices))]
        minutes -= 1
    if pressure > max_pressure:
        max_pressure = pressure
        print(i, max_pressure, time()-t0)
