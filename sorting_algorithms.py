#sorting algorithms
import sys
import random

sys.setrecursionlimit(20000)

def random_perm(n):
	"""
	Return a random permutation of 0,1,...,n.
	
	>>> random_perm(3)
	[1, 0, 2]
	"""
	return random.sample(range(0,n),n)