with open("input.txt", "r") as f:
    file = [int(line.strip('\n')) for line in f.readlines()]

coords = []
for i in range(len(file)):
    coords.append((file[i], i))

print([c[0] for c in coords])

for i in range(len(coords)):
    real_i = -1
    for j in range(len(coords)):
        if i == coords[j][1]:
            real_i = j
            # print(coords[real_i])
            break

    new_coord = real_i + coords[real_i][0]
    if new_coord < 0 or new_coord > len(coords):
        new_coord += new_coord // len(coords)
    new_coord = abs(new_coord % len(coords))
    coords.insert(new_coord, coords.pop(real_i))
    # print(i, [c[0] for c in coords], new_coord)

# serach for 0
for i in range(len(coords)):
    if coords[i][0] == 0:
        coords_0 = i
        break

print(coords[(coords_0 + 1000) % len(file)][0] + coords[(coords_0 + 2000) % len(file)][0] +
      coords[(coords_0 + 3000) % len(file)][0])
