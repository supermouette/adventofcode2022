import numpy as np
import matplotlib.pyplot as plt

with open("input.txt", "r") as f:
    jets = list(f.readline().strip('\n'))

# jets = list(">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>")

turn = 10000

tower = np.zeros((50000, 7), np.uint(8))

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

history = []

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
            tower[draw_shape(shape, i, j)] = 1
            height = max(height, i+shape.shape[0])
        elif np.max(tower[rr, cc]) > 0:
            # print('b', rr, cc)
            blocked = True
            tower[draw_shape(shape, i, j)] = 1
            height = max(height, i+shape.shape[0])
        else:
            i -= 1

    history.append(height)

from math import pi
# p2 :

# step 0 : try to find some kind of pattern in tower (fail)

# step 1 : notice than history[i]*i is close to 1.57*i
# step 1bis : 1.57 is close to pi/2

plt.plot(list(range(len(history))), history)
plt.plot(list(range(len(history))), [i*pi/2 for i in range(len(history))])
print(1000000000000*pi/2) # not the answser
plt.show()

diff = [(i*pi/2)-history[i] for i in range(len(history))]
plt.plot(list(range(len(history))), diff)
plt.show()
# step 2 : THERE IS KIND OF A PERIOD OF 1720 !!!!!!!
plt.plot(list(range(len(history[:1720]))), diff[:1720])
plt.plot(list(range(len(history[1720:1720*2]))), diff[1720:1720*2])
plt.plot(list(range(len(history[1720*2:1720*3]))), diff[1720*2:1720*3])
plt.show()
print(diff[1720]-diff[1720*2]) # 2.23
print(diff[1720*2]-diff[1720*3]) # 2.23
# WHAT'S 2.23 ??????
plt.plot(list(range(len(history[:1720]))), diff[:1720])
plt.plot(list(range(len(history[1720:1720*2]))), [a+2.230317912777 for a in diff[1720:1720*2]])
plt.plot(list(range(len(history[1720*2:1720*3]))), [a+2.230317912777*2 for a in diff[1720*2:1720*3]])
plt.show()
# IDK BUT LET'S GO

diff_mod = [(i*pi/2)-history[i] for i in range(len(history))][1720:1720*2]
plt.plot(list(range(len(history))), history)

operation = lambda i : i*pi/2 + 2.230317912777*((i//1720)-1) - diff_mod[i%1720] # had to add a - 1 somewhere
plt.plot(list(range(len(history))), [operation(i) for i in range(len(history))])
plt.show()


diff2 = [operation(i)-history[i] for i in range(len(history))]
plt.plot(list(range(len(history))), diff2)

print(operation(2022-1))  # should be 3191
print(operation(1000000000000-1))  # had to add a -1 there
plt.show()
