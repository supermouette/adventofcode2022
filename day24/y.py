with open("input.txt", "r")  as f :
	lines = [line.strip('\n')[::-1] for line in f.readlines()]

print(lines[0])
print(lines[-1])
total_fuel = 0
for line in lines:
	fuel = 0
	for i in range(len(line)):
		digit = 0
		if line[i] == "-":
			digit=-1
		elif line[i] == "=":
			digit=-2
		else:
			digit = int(line[i])

		fuel += digit*(5**i)
	total_fuel += fuel

print(total_fuel)

def number2base(n,b):
	if n == 0:
		return [0]
	digits = []
	while n:
		digits.append(int(n%b))
		n//=b
	return digits

b5 = number2base(total_fuel, 5)

snafu = ""
ret = 0
print(b5)
for nb in b5:
	nb += ret
	ret = nb // 5
	nb = nb % 5
	if nb == 3:
		ret += 1
		snafu = "="+snafu
	elif nb == 4:
		ret += 1
		snafu = "-"+snafu
	else:
		snafu = str(nb)+snafu
print(snafu)
