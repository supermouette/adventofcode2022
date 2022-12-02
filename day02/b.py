with open("input.txt", "r") as f:
    rounds = [l.strip("\n") for l in f.readlines()]

# rock < paper < cisor
# X < Y < Z < X
# A < B < C < A
# no shame
guide = {'A X': 1 + 3, 'A Y': 2 + 6, 'A Z': 3 + 0,
         'B X': 1 + 0, 'B Y': 2 + 3, 'B Z': 3 + 6,
         'C X': 1 + 6, 'C Y': 2 + 0, 'C Z': 3 + 3}

score = 0
for round in rounds:
    score += guide[round]

print(score)

# X loose, Y draw, Z win
guide_2 = {'A X': 3 + 0, 'A Y': 1 + 3, 'A Z': 2 + 6,
           'B X': 1 + 0, 'B Y': 2 + 3, 'B Z': 3 + 6,
           'C X': 2 + 0, 'C Y': 3 + 3, 'C Z': 1 + 6}

score_2 = 0

for round in rounds:
    score_2 += guide_2[round]

print(score_2)
