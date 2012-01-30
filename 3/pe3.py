#! /usr/bin/env python3.2

import math
primes = []
def is_prime(x):
#	if x in primes:
#		return True
#	else:
	if x in [0, 1]:
		return False
	if x in [2, 3, 5]:
#		primes.append(x)
		return True
	if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
		return False
	for i in range(6, int(math.sqrt(x)), 6):
		if x % (i - 1) == 0 or x % (i + 1) == 0:
			return False
#	primes.append(x)
#	print(x)
	return True

def max_prime(x):

	maxim = 0
	if x % 2 == 0:
		maxim = 2
	if x % 3 == 0:
		maxim = 3
	for i in range(6, int(math.sqrt(x)), 6):
		if  x % (i - 1) == 0 and is_prime(i - 1):
			maxim = i - 1
		if  x % (i + 1) == 0 and is_prime(i + 1):
			maxim = i + 1
	return maxim


if __name__ == "__main__":
	import sys
	from timeit import Timer
	x = int(sys.argv[1])
	t = Timer("max_prime(60085147514331)", "from __main__ import max_prime, is_prime")
	print(t.timeit(number=100))
	print(max_prime(x))
