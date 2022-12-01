with open("input.txt", "r") as f:
    elves = [list(map(int,elf.split("\n"))) for elf in "".join(f.readlines()).split("\n\n")]

elves_sum = [sum(elf) for elf in elves]
elves_sum.sort(reverse=True)

print("first answer", elves_sum[0])
print("second answer", sum(elves_sum[:3]))

# data viz

import matplotlib.pyplot as plt

plt.plot(elves_sum)
plt.show()

snacks = [snack for snack_list in elves for snack in snack_list]
snacks.sort(reverse=True)
plt.plot(snacks)
plt.show()

bag_size = [len(elf) for elf in elves]
bag_size.sort(reverse=True)
plt.plot(bag_size)
plt.show()