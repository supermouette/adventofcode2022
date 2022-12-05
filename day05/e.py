import re

"""
[N]         [C]     [Z]
[Q] [G]     [V]     [S]         [V]
[L] [C]     [M]     [T]     [W] [L]
[S] [H]     [L]     [C] [D] [H] [S]
[C] [V] [F] [D]     [D] [B] [Q] [F]
[Z] [T] [Z] [T] [C] [J] [G] [S] [Q]
[P] [P] [C] [W] [W] [F] [W] [J] [C]
[T] [L] [D] [G] [P] [P] [V] [N] [R]
 1   2   3   4   5   6   7   8   9
"""

piles = {1: ['N', 'Q', 'L', 'S', 'C', 'Z', 'P', 'T'],
         2: ['G', 'C', 'H', 'V', 'T', 'P', 'L'],
         3: ['F', 'Z', 'C', 'D'],
         4: ['C', 'V', 'M', 'L', 'D', 'T', 'W', 'G'],
         5: ['C', 'W', 'P'],
         6: ['Z', 'S', 'T', 'C', 'D', 'J', 'F', 'P'],
         7: ['D', 'B', 'G', 'W', 'V'],
         8: ['W', 'H', 'Q', 'S', 'J', 'N'],
         9: ['V', 'L', 'S', 'F', 'Q', 'C', 'R']}

for i in range(1,10):
    piles[i] = piles[i][::-1] # yeah...

with open("input.txt", "r") as f:
    lines = [l.strip("\n") for l in f.readlines()[10:]]

for line in lines:
    instruction = list(map(int,re.search(r"move ([0-9]+) from ([0-9]) to ([0-9])", line).groups()))
    for i in range(instruction[0]):
        piles[instruction[2]].append(piles[instruction[1]].pop())

for i in range(1,10):
    print(piles[i][-1], end="")
print()

# no shame
piles = {1: ['N', 'Q', 'L', 'S', 'C', 'Z', 'P', 'T'],
         2: ['G', 'C', 'H', 'V', 'T', 'P', 'L'],
         3: ['F', 'Z', 'C', 'D'],
         4: ['C', 'V', 'M', 'L', 'D', 'T', 'W', 'G'],
         5: ['C', 'W', 'P'],
         6: ['Z', 'S', 'T', 'C', 'D', 'J', 'F', 'P'],
         7: ['D', 'B', 'G', 'W', 'V'],
         8: ['W', 'H', 'Q', 'S', 'J', 'N'],
         9: ['V', 'L', 'S', 'F', 'Q', 'C', 'R']}

for i in range(1,10):
    piles[i] = piles[i][::-1] # yeah...

for line in lines:
    instruction = list(map(int,re.search(r"move ([0-9]+) from ([0-9]) to ([0-9])", line).groups()))
    piles[instruction[2]] += piles[instruction[1]][-1*instruction[0]:]
    piles[instruction[1]] = piles[instruction[1]][:-1 * instruction[0]]

for i in range(1,10):
    print(piles[i][-1], end="")
print()
