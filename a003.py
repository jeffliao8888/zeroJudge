from sys import stdin

for line in stdin:
	month, day = line.split()
	s = (int(month) * 2 + int(day)) % 3
	if(s == 0):
		print("普通")
	elif(s == 1):
		print("吉")
	elif(s == 2):
		print("大吉")