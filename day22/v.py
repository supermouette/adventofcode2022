import matplotlib.pyplot as plt
import numpy as np
import re

with open("input.txt", "r") as f:
    input = [line.strip('\n') for line in f.readlines()]

instruction = "R" + input.pop()

input.pop()

print(input[-4:])

map = np.zeros((len(input), max([len(input[i]) for i in range(len(input))])), np.uint8)
position = None

for i in range(len(input)):
    for j in range(len(input[i])):
        match input[i][j]:
            case " ":
                map[i, j] = 0
            case ".":
                if position is None:
                    position = [i, j]
                    print("origin", i,j)
                map[i, j] = 1
            case "#":
                map[i, j] = 2

viz = np.copy(map)

# plt.imshow(map)
# plt.show()

way = 3

ways = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def wrap(map, position, direction,):
    newer_pos = [position[0], position[1]]
    tmp_dir = [direction[0]*-1, direction[1]*-1]
    while True:
        newer_pos = [newer_pos[0]+tmp_dir[0], newer_pos[1]+tmp_dir[1]]
        if newer_pos[0] < 0 or newer_pos[1] < 0 or newer_pos[0]>=map.shape[0] or newer_pos[1]>=map.shape[1]:
            break
        elif map[newer_pos[0], newer_pos[1]] == 0:
            break
        new_pos = [newer_pos[0], newer_pos[1]]
    if map[new_pos[0], new_pos[1]]== 2:
        return position
    print("wrapped from", position, 'to', new_pos)
    return new_pos


stopped = False

while not stopped:
    instr = re.search(r"^([A-Z])([0-9]+)", instruction)
    direction, nb = instr.group(1), instr.group(2)
    instruction = instruction[len(direction)+len(nb):]
    nb = int(nb)
    way += 1 if direction == "R" else -1
    way %= 4
    if way < 0:
        way += 4

    print(direction, ways[way], nb)
    for i in range(nb):
        new_pos = [position[0]+ways[way][0], position[1]+ways[way][1]]
        if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0]>=map.shape[0] or new_pos[1]>=map.shape[1]:
            position = wrap(map, position, ways[way])
        elif map[new_pos[0], new_pos[1]] == 0:
            position = wrap(map, position, ways[way])
        elif map[new_pos[0], new_pos[1]] == 1:
            position = new_pos
        elif map[new_pos[0], new_pos[1]] == 2:
            viz[position[0], position[1]] = 4 + way
            break
        viz[position[0], position[1]] = 4 + way
    print(position)

    if len(instruction) == 0:
        stopped = True

print(position[0]+1, position[1]+1, way, ways[way])
print((position[0]+1)*1000+(position[1]+1)*4+way)
plt.imshow(viz)
plt.show()