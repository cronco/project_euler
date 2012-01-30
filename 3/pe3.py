#! /usr/bin/env python3.2

import math
primes = []
def is_prime(x):
	if x in primes:
		return False
	else:
		if x == 1:
			return False
		if x == 2 or x == 3:
			primes.append(x)
			return True
		for i in range(6,int(math.sqrt(x)),6):
			if x % (i - 1) == 0 or x % (i + 1) == 0:
				return False
		primes.append(x)
		return True

def max_prime(x):

	maxim = 0
	if x % 2 == 0:
		maxim = 2
	if x % 3 == 0:
		maxim = 3
	for i in range(6, int(math.sqrt(x)), 6):
		if x % (i - 1) == 0 and is_prime(i -1):
			maxim = i - 1
		elif x % (i + 1) == 0 and is_prime(i + 1):
			maxim = i + 1
	return maxim


if __name__ == "__main__":
	import sys
	from timeit import Timer
	x = int(sys.argv[1])
	t = Timer("max_prime(6008514751433)", "from __main__ import max_prime, is_prime")
	print(t.timeit(number=10))
	print(max_prime(x))
