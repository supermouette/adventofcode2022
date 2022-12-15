with open("input.txt", "r") as f:
    sensors = [[list(map(int,l.split(','))) for l in  line.strip('\n').split(";")] for line in f.readlines()]


def coord_h(coord):
    return str(coord[0])+','+str(coord[1])


def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


for row in range(4000000, 2000000, -1):
    if row % 100000 == 0:
        print(row/4000000)
    not_beacons = []
    beacon_row = set()
    for sensor, beacon in sensors:
        # print(beacon)
        if beacon[1] == row:
            beacon_row.add(coord_h(beacon))
        if sensor[1] == row:
            beacon_row.add(coord_h(beacon))
        d = manhattan(sensor, beacon)
        if sensor[1]-d <= row <= sensor[1]+d:
            d_row = d-abs(sensor[1]-row)
            not_beacons.append([sensor[0]-d_row, sensor[0]+d_row])

    merged = []
    not_beacons.sort()
    for n_b in not_beacons:
        if len(merged) == 0 or merged[-1][1] < n_b[0]:
            merged.append(n_b)
        else:
            merged[-1][1] = max(merged[-1][-1], n_b[1])
    if len(merged) == 2:
        if merged[0][1] +1 == merged[1][0]:
            merged = [[merged[0][0],merged[1][1]]]
    sum_nb = -len(beacon_row)
    for r in merged:
        sum_nb += r[1]-r[0]+1
    #print(not_beacons)
    #print(beacon_row)
    #print(merged)
    #print(row, sum_nb, merged, beacon_row)
    if len(merged) == 2:
        print(row, merged, (merged[0][1]+1)*4000000+row)
        exit()