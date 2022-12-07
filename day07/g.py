with open("input.txt", "r") as f:
    lines = [l.strip("\n") for l in f.readlines()[1:]]


pwd = []
tree = {}
sum = 0
total_space = 70000000
needed_space = 30000000
used_space = 51334861
space_to_delete = (total_space-used_space-needed_space)*-1

smallest_deleted = 48381165

def add_dir(path, name):
    global tree
    sub_tree = tree
    for d in path:
        sub_tree = sub_tree[d]
    sub_tree[name] = {}

def add_file(path, name, size):
    global tree
    sub_tree = tree
    for d in path:
        sub_tree = sub_tree[d]
    sub_tree[name] = {'_SIZE' : int(size)}

def count_current_dir(path):
    global tree
    sub_tree = tree
    size = 0
    for d in path:
        sub_tree = sub_tree[d]
    for key, value in sub_tree.items():
        size += sub_tree[key]["_SIZE"]
    sub_tree["_SIZE"] = size
    return size


for line in lines:
    if line.startswith("$ cd"):
        if line == "$ cd ..":
            size = count_current_dir(pwd)
            if size < 100000:
                sum += size
            if size < smallest_deleted and size > space_to_delete:
                smallest_deleted = size
            pwd.pop()
        else:
            pwd.append(line.split(" ")[2])
        print("/".join(pwd))
    if not line.startswith("$"):
        if line.startswith("dir"):
            add_dir(pwd, line.split(" ")[1])
        else:
            instr = line.split(" ")
            add_file(pwd, instr[1], instr[0])

print(sum)


total = 0
for key, value in tree.items():
    print(key)
    sum += tree[key]["_SIZE"]

print("used_space", sum)
print(total_space-used_space-needed_space)
print(smallest_deleted)