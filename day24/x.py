import numpy as np
import matplotlib.pyplot as plt

with open("input.txt", "r") as f:
    input = [list(line.strip('\n')) for line in f.readlines()]

blizzards = []
size = (len(input), len(input[0]))
for i in range(size[0]):
    for j in range(size[1]):
        match input[i][ j]:
            case '>':
                blizzards.append(((i, j), (0, 1)))
            case '<':
                blizzards.append(((i, j), (0, -1)))
            case 'v':
                blizzards.append(((i, j), (1, 0)))
            case '^':
                blizzards.append(((i, j), (-1, 0)))


def meteo(blizzards, size):
    new_blizzards = []
    bzz_7 = set()
    for b, d in blizzards:
        new_b = (b[0] + d[0], b[1] + d[1])
        if new_b[0] == 0:
            new_b = (size[0]-2, new_b[1])
        elif new_b[0] == size[0]-1:
            new_b = (1, new_b[1])
        elif new_b[1] == 0:
            new_b = (new_b[0], size[1]-2)
        elif new_b[1] == size[1]-1:
            new_b = (new_b[0], 1)
        bzz_7.add(new_b)
        new_blizzards.append((new_b, d))
    return new_blizzards, bzz_7


def available_moves(pos, bzz, size):
    moves = []
    # up
    if pos[0] > 1 and (pos[0] - 1, pos[1]) not in bzz:
        moves.append((-1, 0))
    # left
    if pos[1] > 1 and (pos[0], pos[1] - 1) not in bzz and pos[0] != size[0]-1:
        moves.append((0, -1))
    # wait
    if (pos[0], pos[1]) not in bzz:
        moves.append( (0, 0))
    # down
    if pos[0] < size[0] - 2 and (pos[0] + 1, pos[1]) not in bzz:
        moves.append((1, 0))
    # right
    if pos[1] < size[1] - 2 and (pos[0], pos[1] + 1) not in bzz and pos[0] != 0:
        moves.append((0, 1))
    return moves


def viz(bzz, hdd):
    print("bzz", len(bzz))
    print("hdd", len(hdd))
    img = np.zeros(size)
    img[0, :] = 1
    img[-1, :] = 1
    img[:, 0] = 1
    img[:, -1] = 1
    img[0, 1] = 0
    img[-1, -2] = 0
    for b, _ in bzz:
        img[b[0], b[1]] = 2
    for h in hdd:
        img[h[0], h[1]] = 3
    plt.imshow(img)
    plt.show()

pos = [0, 1]
minute = 0
heads = [pos]
found = False

while not found:
    # viz(blizzards, heads)
    blizzards, bzz = meteo(blizzards, size)
    new_heads = set()
    for head in heads:
        moves = available_moves(head, bzz, size)
        for move in moves:
            new_head = (head[0]+move[0], head[1]+move[1])
            if new_head == (size[0]-2, size[1]-2):
                found = True
            new_heads.add(new_head)
    heads = new_heads
    minute += 1
minute += 1
blizzards, bzz = meteo(blizzards, size)
print("exited the valley in ", minute)

pos = [size[0]-1, size[1]-2]
heads = [pos]
found = False
while not found:
    # viz(blizzards, heads)
    blizzards, bzz = meteo(blizzards, size)
    new_heads = set()
    for head in heads:
        moves = available_moves(head, bzz, size)
        for move in moves:
            new_head = (head[0]+move[0], head[1]+move[1])
            if new_head == (2, 2):
                found = True
            new_heads.add(new_head)
    heads = new_heads
    minute += 1
minute += 1
blizzards, bzz = meteo(blizzards, size)
print("went back for Tobby in ", minute)

pos = [0, 1]
heads = [pos]
found = False
while not found:
    # viz(blizzards, heads)
    blizzards, bzz = meteo(blizzards, size)
    new_heads = set()
    for head in heads:
        moves = available_moves(head, bzz, size)
        for move in moves:
            new_head = (head[0]+move[0], head[1]+move[1])
            if new_head == (size[0]-2, size[1]-2):
                found = True
            new_heads.add(new_head)
    heads = new_heads
    minute += 1
minute += 1
print("out again ", minute)
