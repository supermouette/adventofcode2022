with open("input.txt", "r") as f:
    lava = [list(map(int, line.strip("\n").split(","))) for line in f.readlines()]

# part 1
surface = 6 * len(lava)
print(surface)
for i in range(len(lava)):
    for j in range(i, len(lava)):
        if abs(lava[i][0] - lava[j][0]) + abs(lava[i][1] - lava[j][1]) + abs(lava[i][2] - lava[j][2]) == 1:
            surface -= 2
print(surface)

# part 2
sides = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
water = set()
to_fill = [(0, 0, 0)]

while to_fill:
    x, y, z = to_fill.pop()
    if (x, y, z) in water or [x, y, z] in lava:
        continue
    water.add((x, y, z))
    for dx, dy, dz in sides:
        new_x, new_y, new_z = x + dx, y + dy, z + dz
        if -1 <= new_x <= 25 and -1 <= new_y <= 25 and -1 <= new_z <= 25:
            to_fill.append((new_x, new_y, new_z))

surface = 0
for x, y, z in lava:
    for dx, dy, dz in sides:
        if (x + dx, y + dy, z + dz) in water:
            surface += 1
print(surface)
