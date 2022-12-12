import dijkstra

with open("input.txt", "r") as f:
    height = [list(map(ord, line.strip("\n"))) for line in f.readlines()]

start = []
end = []
graph = {}
list_a = []

def c2s(i, j):
    return str(i) + "," + str(j)

print(len(height), len(height[0]))
for i in range(len(height)):
    for j in range(len(height[0])):
        if height[i][j] == ord("S"):
            start = [i, j]
            height[i][j] = ord('a')
        elif height[i][j] == ord("E"):
            end = [i, j]
            height[i][j] = ord("z")
        if height[i][j] == ord('a'):
            list_a.append(c2s(i, j))

        possible_dir = []
        if i != 0:
            if height[i][j] + 1 >= height[i - 1][j]:
                possible_dir.append((1, c2s(i - 1, j)))
        if i != len(height) - 1:
            if height[i][j]+1 >= height[i + 1][j]:
                possible_dir.append((1, c2s(i + 1, j)))
        if j != 0:
            if height[i][j] + 1 >= height[i][j-1]:
                possible_dir.append((1, c2s(i, j-1)))
        if j != len(height[0]) - 1:
            if height[i][j]+1 >= height[i][j+1]:
                possible_dir.append((1, c2s(i, j+1)))
        graph[c2s(i,j)] = possible_dir

shortest, path, d = dijkstra.dijkstra(c2s(start[0], start[1]), c2s(end[0], end[1]), graph)

print(shortest)
print(d[c2s(end[0], end[1])])

