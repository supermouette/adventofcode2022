import numpy as np
import matplotlib.pyplot as plt

with open("input.txt", "r") as f:
    paths = [[list(map(int, l.split(",")))[::-1] for l in line.strip("\n").split(" -> ")]for line in f.readlines()]

max_x, min_x, max_y, min_y = 0, 0, 0, 0

for p in paths:
    for l in p:
        max_x = max(max_x, l[0])
        min_x = min(min_x, l[0])
        max_y = max(max_y, l[0])
        min_y = min(min_y, l[0])

print(max_x, min_x, max_y, min_y)

cave = np.zeros((510,1000))

for p in paths:
    for i in range(1,len(p)):
        if p[i-1][0] == p[i][0]:
            max_y = max(p[i-1][1], p[i][1])
            min_y = min(p[i-1][1], p[i][1])
            cave[p[i][0], min_y:max_y+1] = 1
        else:
            max_x = max(p[i - 1][0], p[i][0])
            min_x = min(p[i - 1][0], p[i][0])
            cave[min_x:max_x+1, p[i][1]] = 1

cave[0,500] = 3
cave[163, :]=1
# cave[11, :] = 1
n=0
i,j = -1,0
while i!=0 or i > 506:
    i,j = 0, 500
    stopped = False

    while not stopped:
        if i>506:
            stopped = True
            print(n)
            plt.imshow(cave)
            plt.show()
            exit()
        elif cave[i+1,j] == 0:
            i += 1
        elif cave[i+1][j-1] == 0:
            i += 1
            j -= 1
        elif cave[i+1][j+1] == 0:
            i += 1
            j += 1
        else:
            cave[i, j] = 2
            stopped = True

    n+= 1
plt.imshow(cave)
plt.show()

print(n)