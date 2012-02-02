#! /usr/bin/env python3.2

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""


import sys
import os
sys.path.append(os.path.abspath('../'))
from primes import sieve

if __name__ == "__main__":
	from timeit import Timer
	try:
		x = int(sys.argv[1])
	
	except:
		x = 2
	t = Timer("sieve("  + str(x) + ")", "from __main__ import sieve")
	print(sieve(x))
	print(t.timeit(number = 10))
	
