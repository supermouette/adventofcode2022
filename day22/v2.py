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

def wrap(map, position, direction):
    new_pos = [position[0], position[1]]
    # Face 1
    if position[0] == 0 and 50 <= position[1] <= 99 and direction == 3:
        new_pos = [150+position[1]-50, 0]
        new_way = 0
    elif position[1] == 50 and 0 <= position[0] <= 49 and direction == 2:
        new_pos = [149-position[0], 0]
        new_way = 0
    # Face 2
    elif position[0] == 0 and 100 <= position[1] <= 149 and direction == 3:
        new_pos = [199, 0 + position[1]-100]
        new_way = 3
    elif position[1] == 149 and 0 <= position[0] <= 49 and direction == 0:
        new_pos = [149 - position[0], 99]
        new_way = 2
    elif position[0] == 49 and 100 <= position[1] <= 149 and direction == 1:
        new_pos = [50+position[1]-100, 99]
        new_way = 2
    # Face 3
    elif position[1] == 50 and 50 <= position[0] <= 99 and direction == 2:
        new_pos = [100, position[0]-50]
        new_way = 1
    elif position[1] == 99 and 50 <= position[0] <= 99 and direction == 0:
        new_pos = [49, 100+position[0]-50]
        new_way = 3
    # Face 4
    elif position[1] == 99 and 100 <= position[0] <= 149 and direction == 0:
        new_pos = [49-position[0]+100, 149]
        new_way = 2
    elif position[0] == 149 and 50 <= position[1] <= 99 and direction == 1:
        new_pos = [150+position[1]-50, 49]
        new_way = 2
    # Face 5
    elif position[0] == 100 and 0 <= position[1] <= 49 and direction == 3:
        new_pos = [50+position[1], 50]
        new_way = 0
    elif position[1] == 0 and 100 <= position[0] <= 149 and direction == 2:
        new_pos = [49-position[0]+100, 50]
        new_way = 0
    # Face 6
    elif position[1] == 0 and 150 <= position[0] <= 199 and direction == 2:
        new_pos = [0, 50 + position[0]-150]
        new_way = 1
    elif position[0] == 199 and 0 <= position[1] <= 49 and direction == 1:
        new_pos = [0, 100+position[1]]
        new_way = 1
    elif position[1] == 49 and 150 <= position[0] <= 199 and direction == 0:
        new_pos = [149, 50+position[0]-150]
        new_way = 3
    else:
        print(position, direction, "error")
    if map[new_pos[0], new_pos[1]] == 2:
        return position, direction
    print("wrapped", position, direction, new_pos, new_way)
    return new_pos, new_way


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
            position, way = wrap(map, position, way)
        elif map[new_pos[0], new_pos[1]] == 0:
            position, way = wrap(map, position, way)
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