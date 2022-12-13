with open("input.txt", "r") as f:
    pairs = [list(map(eval, line.split("\n"))) for line in "".join(f.readlines()).split("\n\n")]


def compare(p1, p2):
    #print(p1, p2)
    if type(p1) == int and type(p2) == int:
        if p1 == p2:
            return 'who knows'
        if p1 < p2:
            return 'ye'
        else:
            return 'na'
    elif type(p1) == list and type(p2) == list:
        for i in range(min(len(p1), len(p2))):
            res = compare(p1[i], p2[i])
            if res != "who knows":
                return res
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


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if compare(arr[j], arr[j+1]) != 'ye':
                arr[j], arr[j+1] = arr[j+1], arr[j]


signals = []
for p in pairs:
    signals += p
signals += [[[2]],[[6]]]
print(len(signals))

bubble_sort(signals)
mult = 1
for i in range(len(signals)):
    print(signals[i])
    if signals[i]==[[2]] or  signals[i]==[[6]]:
        mult*=i+1

print(mult)
