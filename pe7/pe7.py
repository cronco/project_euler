#! /usr/bin/env python3.2

import sys
import os
sys.path.append(os.path.abspath('../'))
from primes import sieve

if __name__ == "__main__":
	from timeit import Timer
	x = int(sys.argv[1])
	t = Timer("sieve(" x ")", "from __main__ import sieve")
	print(t.timeit(number = 10))
	
