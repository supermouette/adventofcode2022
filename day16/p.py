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
    previous = 'AA'
    current = 'AA'
    opened = set()
    minutes = 30
    pressure = 0
    while minutes >= 0:
        valve = valves[current]
        if valve[0] != 0 and current not in opened and random() > 0.15:
            minutes -= 1
            opened.add(current)
            pressure += minutes*valves[current][0]

        choices = valve[1][:]
        if random() > 0.05 and previous in choices and len(choices) > 1:
            choices.remove(previous)
        previous = current
        current = choices[randrange(0, len(choices))]
        minutes -= 1
    if pressure > max_pressure:
        max_pressure = pressure
        print(i, max_pressure, time()-t0)
