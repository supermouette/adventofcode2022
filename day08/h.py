import numpy as np
import matplotlib.pyplot as plt

with open("input.txt", "r") as f:
    lines = [list(map(int, l.strip("\n"))) for l in f.readlines()]

img = np.asarray(lines)

mask = np.zeros(img.shape)
mask[0, :] = 1
mask[-1, :] = 1
mask[:, 0] = 1
mask[:, -1] = 1

for i in range(1, img.shape[0]):
    max_height = img[i, 0]
    for j in range(1, img.shape[1]):
        if img[i, j] > max_height:
            mask[i, j] = 1
            max_height = img[i, j]

for j in range(1, img.shape[1]):
    max_height = img[0, j]
    for i in range(1, img.shape[0]):
        if img[i, j] > max_height:
            mask[i, j] = 1
            max_height = img[i, j]

for i in range(img.shape[0] - 2, 0, -1):
    max_height = img[i, -1]
    for j in range(img.shape[1] - 2, 0, -1):
        if img[i, j] > max_height:
            mask[i, j] = 1
            max_height = img[i, j]

for j in range(img.shape[1] - 2, 0, -1):
    max_height = img[-1, j]
    for i in range(img.shape[0] - 2, 0, -1):
        if img[i, j] > max_height:
            mask[i, j] = 1
            max_height = img[i, j]

print(np.sum(mask))

dist = np.zeros(img.shape)

for i in range(1, img.shape[0] - 1):
    for j in range(1, img.shape[1] - 1):
        up = 1
        for x in range(i - 1, 0, -1):
            if img[x, j] < img[i, j]:
                up += 1
            else:
                break
        left = 1
        for y in range(j - 1, 0, -1):
            if img[i, y] < img[i, j]:
                left += 1
            else:
                break
        down = 1
        for x in range(i + 1, img.shape[0]-1):
            if img[x, j] < img[i, j]:
                down += 1
            else:
                break
        right = 1
        for y in range(j + 1, img.shape[1]-1):
            if img[i, y] < img[i, j]:
                right += 1
            else:
                break
        dist[i, j] = up*down*left*right

print(np.max(dist))

plt.imshow(dist)
plt.show()

fig = plt.figure()
ax1 = plt.subplot(221)
ax2 = plt.subplot(222, sharex=ax1, sharey=ax1)
ax3 = plt.subplot(223, sharex=ax1, sharey=ax1)

ax1.imshow(img)
ax2.imshow(mask)
ax3.imshow(dist)
plt.show()
