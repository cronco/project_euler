#! /usr/bin/env python3.2


def reduce(func, iterable, start = None):
	"""
	Recreate the py 2.x reduce function.
	Poorly, probably.
	"""

	try:
		it = iterable.__iter__()
	except AttributeError:
		return start

	try:
		acc = start if start else next(it)
	except StopIteration:
		return start
	for i in range(0 if start else 1, len(iterable)):
		acc = func(acc, next(it))
	
	return acc
