#! /usr/bin/env python3.2

import math

def make_palyndrome(l):
	"""
		takes a list of ints and creates a palyndrome from it
	"""
	pal = 0
	for i, x in enumerate(l):
		pal += 10**i * x + 10**(len(l)*2 - i - 1)*x
	return pal

def make_all():
	return [make_palyndrome([x,y,z]) for x in range(9, 0, -1) for y in range (9, -1, -1) for z in range(9, -1, -1)]

if __name__ == "__main__":
	import sys
	#l = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
	print(make_all())
