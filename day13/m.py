with open("test.txt", "r") as f:
    pairs = [list(map(eval, line.split("\n"))) for line in "".join(f.readlines()).split("\n\n")]


def compare(p1, p2):
    print(p1, p2)

    if type(p1) == int and type(p2) == int:
        if p1 == p2:
            return 'who knows'
        if p1 < p2:
            return 'ye'
        else:
            return 'na'
    elif type(p1) == list and type(p2) == list:
        print(p1, p2, len(p1), len(p2))
        for i in range(min(len(p1), len(p2))):
            res = compare(p1[i], p2[i])
            if res != "who knows":
                return res
        print("end", len(p1), len(p2))
        if len(p2) < len(p1):
            return 'na'
        elif len(p1) < len(p2):
            return 'ye'
        else:
            return 'who knows'
    elif type(p1) == int:
        return compare([p1], p2)
    elif type(p2) == int:
        return compare(p1, [p2])
    return 'who knows'


pair_index = 0
index_sum = 0

for p1, p2 in pairs:
    pair_index += 1
    print("         START " + str(pair_index))

    print("         "+compare(p1, p2) + "  " + str(pair_index))

    if compare(p1, p2) != 'na':
        index_sum += pair_index
print(index_sum)
