with open("input.txt", "r") as f:
    lines = [line.strip("\n").split(" ") for line in f.readlines()]

rope = []
for i in range(10):
    rope.append([0, 0])


def pos2string(pos):
    return str(pos[0]) + ',' + str(pos[1])


visited = {pos2string(rope[-1])}

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
        rope[0][0] += h_way[0]
        rope[0][1] += h_way[1]

        for node in range(1,len(rope)):
            dist_hs_x = rope[node-1][0] - rope[node][0]
            dist_hs_y = rope[node-1][1] - rope[node][1]

            t_way = [0, 0]
            if dist_hs_x == 0 and abs(dist_hs_y) > 1:
                t_way = [0, dist_hs_y // abs(dist_hs_y)]
            elif dist_hs_y == 0 and abs(dist_hs_x) > 1:
                t_way = [dist_hs_x // abs(dist_hs_x), 0]
            elif dist_hs_x != 0 and abs(dist_hs_y) > 1 or dist_hs_y != 0 and abs(dist_hs_x) > 1:
                t_way = [dist_hs_x // abs(dist_hs_x), dist_hs_y // abs(dist_hs_y)]
            rope[node][0] += t_way[0]
            rope[node][1] += t_way[1]
        visited.add(pos2string(rope[-1]))

print(visited)
print(len(visited))
