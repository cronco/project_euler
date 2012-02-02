#! /usr/bin/env python3.2

import math

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


def sieve(length = 2):
	"""
	The so called Eratostene's Sieve for prime numbers

	"""

	sieve = []

	power = 0
	while len(sieve) < length:
		for i in range(10**(power) + 1, 10**(power + 1)):
			if not any(i % x == 0 for x in sieve):
				sieve.append(i)
				if len(sieve) == length: break
		power += 1

	return sieve

