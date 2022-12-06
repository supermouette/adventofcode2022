with open("input.txt", "r") as f:
    line = f.readline().strip('\n')


def first_message(packet_size):
    for i in range(packet_size-1,len(line)):
        sub = set(line[i-packet_size:i])
        if len(sub) == packet_size:
            return i


print(first_message(4))
print(first_message(14))
