with open("input.txt", "r") as f:
    ruck_sacks = [l.strip("\n") for l in f.readlines()]

sacks = [[s[:len(s) // 2], s[len(s) // 2:]] for s in ruck_sacks]


def get_priority(char):
    return ord(char) - ord('a') + 1 if ord(char) >= ord('a') else ord(char) - ord('A') + 27


priority = 0
for sack in sacks:
    for item in sack[0]:
        if item in sack[1]:
            priority += get_priority(item)
            break
print(priority)

priority = 0
for i in range(0, len(sacks) - 1, 3):
    for item in ruck_sacks[i]:
        if item in ruck_sacks[i + 1] and item in ruck_sacks[i + 2]:
            priority += get_priority(item)
            break
print(priority)
