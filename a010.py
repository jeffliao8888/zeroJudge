from sys import stdin
from collections import Counter

for number in stdin:
	number = int(number)
	factors = list()
	div = 2
	while(number > 1):
		if(number % div == 0):
			factors.append(div)
			number /= div
		else:
			div += 1
	count = dict(Counter(factors))
	ans = str()
	for i in count:
		if(count[i]!=1):
			ans += "%d^%d * " %(i, count[i])
		else:
			ans += "%d * " %(i)

	print(ans[:-2])