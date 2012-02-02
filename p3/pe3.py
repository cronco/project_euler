#! /usr/bin/env python3.2

import math
import sys
import os
sys.path.append(os.path.abspath('../'))
from primes import is_prime

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
	from timeit import Timer
	x = int(sys.argv[1])
	t = Timer("max_prime(60085147514331)", "from __main__ import max_prime, is_prime")
	print(t.timeit(number=100))
	print(max_prime(x))
