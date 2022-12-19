from random import random

with open("input.txt", "r") as f:
    raw = [line.strip('\n').split(" ") for line in f.readlines()]

blueprints = {}
mat = ["ore", "clay", "obsidian", "geode"]
for r in raw:
    blueprints[int(r[1][:-1])] = {0: (int(r[6]), 0, 0, 0),
                                  1: (int(r[12]), 0, 0, 0),
                                  2: (int(r[18]), int(r[21]), 0, 0),
                                  3: (int(r[-5]), 0, int(r[-2]), 0)}


def updateResources(r, dr, sign=1):
    r[0] += dr[0] * sign
    r[1] += dr[1] * sign
    r[2] += dr[2] * sign
    r[3] += dr[3] * sign


def isEnough(r, cost):
    return r[0] >= cost[0] and r[1] >= cost[1] and r[2] >= cost[2] and r[2] >= cost[2]


quality = 0
for idx in blueprints.keys():
    blueprint = blueprints[idx]
    max_geode = 0
    for search in range(10000):
        resources = [0, 0, 0, 0]
        robots = [1, 0, 0, 0]
        old_resources = resources[:]
        for i in range(1, 25):
            new_robots = [0, 0, 0, 0]
            for r in (3, 2, 1, 0):
                if isEnough(resources, blueprint[r]) and (
                        r == 3 or
                        (r == 2 and random() > 0.1) or
                        (r < 2 and random() > 0.5)):
                    new_robots[r] += 1
                    updateResources(resources, blueprint[r], -1)
                    # print(i, mat[r])
                    break
            old_resources = resources
            resources[0] += robots[0]
            resources[1] += robots[1]
            resources[2] += robots[2]
            resources[3] += robots[3]
            updateResources(robots, new_robots)
        if resources[3] > max_geode:
            max_geode = resources[3]
            print(robots, resources, search)
    print(idx, max_geode)
    quality += idx * max_geode
print(quality)
