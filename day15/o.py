with open("input.txt", "r") as f:
    sensors = [[list(map(int,l.split(','))) for l in  line.strip('\n').split(";")] for line in f.readlines()]
row = 2000000
# row = 10

def coord_h(coord):
    return str(coord[0])+','+str(coord[1])


def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


not_beacons = []
beacon_row = set()
for sensor, beacon in sensors:
    print(beacon)
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

sum_nb = -len(beacon_row)
for r in merged:
    sum_nb += r[1]-r[0]+1
print(not_beacons)
print(beacon_row)
print(merged)
print(sum_nb)