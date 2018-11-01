from sys import stdin

for line in stdin:
	x, y = line.split()
	print(int(x) + int(y))