with open("input.txt", "r") as f:
    lines = [line.strip("\n") for line in f.readlines()]

cycle = 0
x = 1
sum = 0
screen = [[], [], [], [], [], []]
row = 0
col = 0


def draw():
    global cycle, x, row, col, screen
    screen[row].append("██" if abs(x-col) < 2 else "  ")
    if col == 39:
        col = 0
        row += 1
    else:
        col += 1


def tick():
    global cycle, sum, x
    draw()
    # print("start",cycle, x, sum)
    cycle += 1
    if cycle in (20, 60, 100, 140, 180, 220):
        sum += x*cycle
        # print(x, cycle, x*cycle)

for line in lines:
    if line == "noop":
        tick()
    else:
        addx = int(line.split(" ")[1])
        tick()
        tick()
        # print("addx", addx)
        x += addx

print(x)
print(sum)

for row in screen:
    print("".join(row))