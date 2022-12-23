import numpy as np
import matplotlib.pyplot as plt

with open("input.txt", "r") as f:
    input = [list(line.strip('\n')) for line in f.readlines()]

elves = {}

for i in range(len(input)):
    for j in range(len(input)):
        if input[i][j] == '#':
            elves[(i, j)] = ["N", "S", "W", "E"]

stopped = False

around = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
around_dir = {"N": [[-1, -1], [-1, 0], [-1, 1]],
              "S": [[1, -1], [1, 0], [1, 1]],
              "E": [[-1, 1], [0, 1], [1, 1]],
              "W": [[-1, -1], [0, -1], [1, -1]]}


def look(pos, directions, stuff):
    cpt = 0
    for d in directions:
        if (pos[0]+d[0], pos[1]+d[1]) in stuff:
            cpt += 1
    return cpt

round = 0
while not stopped:
    round+=1

    """
    img = np.zeros((20,20))
    for i,j in elves:
        img[i,j] = 1
    print(len(elves))
    plt.imshow(img)
    plt.show()
    """

    proposition = {}
    not_moved = []
    for elf in elves:
        if look(elf, around, elves) != 0:
            for d in elves[elf]:
                if look(elf, around_dir[d], elves) == 0:
                    pos = (elf[0]+around_dir[d][1][0], elf[1]+around_dir[d][1][1])
                    if pos in proposition:
                        proposition[pos].append((elf, d))
                    else:
                        proposition[pos] = [(elf, d)]
                    break
            else:
                not_moved.append(elf)
        else:
            not_moved.append(elf)
    if len(not_moved) == len(elves):
        stopped = True
    else:
        new_elves = {}
        # print(len(proposition))
        for prop in proposition:
            if len(proposition[prop]) == 1:
                elf, d = proposition[prop][0]
                # new_ds = elves[elf]
                # new_ds = new_ds[1:]+ [new_ds[0]]
                # new_ds.remove(d)
                # new_ds.append(d)
                new_elves[prop] = elves[elf]
            else:
                # print(len(proposition[prop]))
                for i in range(len(proposition[prop])):
                    new_elves[proposition[prop][i][0]] = elves[proposition[prop][i][0]]
        # print(len(elves), len(new_elves))
        for elf in not_moved:
            new_elves[elf] = elves[elf]
        for elf in new_elves:
            new_ds = new_elves[elf]
            new_ds = new_ds[1:] + [new_ds[0]]
            new_elves[elf] = new_ds
        # print(new_elves[elf])
        # print(len(elves), len(new_elves))
        elves = new_elves

print(round)
coords_i = [e[0] for e in elves.keys()]
coords_j = [e[1] for e in elves.keys()]
print(min(coords_i), max(coords_i), min(coords_j), max(coords_j), len(elves))
print((max(coords_i)-min(coords_i)+1)*(max(coords_j)-min(coords_j)+1) - len(elves))