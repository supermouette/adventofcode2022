with open("input.txt", "r") as f:
    lines = [line.strip("\n").split(" ") for line in f.readlines()]

head = [0, 0]
tail = [0, 0]


def pos2string(pos):
    return str(pos[0]) + ',' + str(pos[1])


visited = {pos2string(tail)}

for instr in lines:
    way = instr[0]
    step = int(instr[1])
    h_way = [0, 0]
    if way == "R":
        h_way = [0, 1]
    elif way == "L":
        h_way = [0, -1]
    elif way == "D":
        h_way = [-1, 0]
    else:
        h_way = [1, 0]

    for i in range(step):
        head[0] += h_way[0]
        head[1] += h_way[1]

        dist_hs_x = head[0] - tail[0]
        dist_hs_y = head[1] - tail[1]

        t_way = [0, 0]
        if dist_hs_x == 0 and abs(dist_hs_y) > 1:
            t_way = [0, dist_hs_y // abs(dist_hs_y)]
        elif dist_hs_y == 0 and abs(dist_hs_x) > 1:
            t_way = [dist_hs_x // abs(dist_hs_x), 0]
        elif dist_hs_x != 0 and abs(dist_hs_y) > 1 or dist_hs_y != 0 and abs(dist_hs_x) > 1:
            t_way = [dist_hs_x // abs(dist_hs_x), dist_hs_y // abs(dist_hs_y)]
        tail[0] += t_way[0]
        tail[1] += t_way[1]
        visited.add(pos2string(tail))

print(visited)
print(len(visited))
