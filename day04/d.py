with open("input.txt", "r") as f:
    pairs = [l.strip("\n").split(",") for l in f.readlines()]

pairs = [[[int(r) for r in e.split('-')] for e in p] for p in pairs]

overlap = 0

for p in pairs:
    if p[0][0] <= p[1][0] and p[0][1] >= p[1][1] or p[1][0] <= p[0][0] and p[1][1] >= p[0][1]:
        overlap += 1

print(overlap)

overlap = 0
for p in pairs:
    if p[0][0] <= p[1][0] <= p[0][1] or p[1][0] <= p[0][1] <= p[1][1] or p[1][0] <= p[0][0] <= p[1][1] or p[1][0] <= p[0][1] <= p[1][1]:
        overlap += 1
print(overlap)