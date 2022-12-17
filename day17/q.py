import numpy as np
import matplotlib.pyplot as plt

with open("input.txt", "r") as f:
    jets = list(f.readline().strip('\n'))

# jets = list(">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>")

turn = 2022

tower = np.zeros((3500, 7))

shapes = [np.asarray([[1, 1, 1, 1]]),
          np.asarray([[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
          np.asarray([[1, 1, 1], [0, 0, 1], [0, 0, 1]]),
          np.asarray([[1], [1], [1], [1]]),
          np.asarray([[1, 1], [1, 1]])]


def draw_shape(s, i, j):
    rr, cc = [], []
    for x in range(s.shape[0]):
        for y in range(s.shape[1]):
            if s[x, y] == 1:
                rr.append(x + i)
                cc.append(y + j)
    return np.asarray(rr), np.asarray(cc)


height = 0
i_jet = 0
for turn in range(turn):
    shape = shapes[turn % len(shapes)]
    i, j = height + 3, 2
    blocked = False
    while not blocked:
        # on the side
        jet = 1 if jets[i_jet % len(jets)] == ">" else -1
        """ # viz
        tower2 = tower.copy()
        tower2[draw_shape(shape, i, j)] = turn + 1
        plt.imshow(tower2[height+7::-1, :])
        plt.show()
        """
        i_jet += 1
        rr, cc = draw_shape(shape, i, j + jet)
        if np.min(cc) >= 0 and np.max(cc) < tower.shape[1]:
            if np.max(tower[rr, cc]) == 0:
                j += jet
        # down
        rr, cc = draw_shape(shape, i - 1, j)
        if np.min(rr) < 0:
            # print('a', rr, cc)
            blocked = True
            tower[draw_shape(shape, i, j)] = turn + 1
            height = max(height, i+shape.shape[0])
        elif np.max(tower[rr, cc]) > 0:
            # print('b', rr, cc)
            blocked = True
            tower[draw_shape(shape, i, j)] = turn + 1
            height = max(height, i+shape.shape[0])
        else:
            i -= 1

print(height)
