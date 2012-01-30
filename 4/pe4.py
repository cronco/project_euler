#! /usr/bin/env python3.2

import math

def make_palyndrome(l)

	for i, x in enumerate(l):
		pal += 10**i * x + 10**(len(l)*2 -1)*x
	return pal

if __name__ == "__main__":
	import sys
	l = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
	print(make_palyndrome(l))
