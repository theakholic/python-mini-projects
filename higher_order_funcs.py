import math
import functools
import itertools

def combine(f,g):
	def h(*args):
		return f(g(*args))

	return h

fourth_root = combine(math.sqrt, math.sqrt)

def repeated_applications(f, n):
	"""Return a function equivalent to fofo...of n times"""
	h = (f for i in range(n))
	return itertools.reduce(combine, h)