def deep_reverse(p):
	return d_r(p,[])

def d_r(p,r):
	"""Regular reverse"""
	if not p:
		return r
	if isinstance(p[0], list):
	    return  d_r(p[1:], [deep_reverse(p[0])]+r)
	else:
		return d_r(p[1:], [p[0]]+r)

def member(e,l):
	"""e in l?"""
	if not l:
		return False
	return e == l[0] or member(e,l[1:])


def recur_sieve(L):
	if L == []:
		return []
	return [L[0]] + recur_sieve(filter(lambda x: x%L[0] != 0, L[1:]))

def powerset(L):
	"""Take a list and find all subsets of it."""
	if not L:
		return [[]] 
	rest = powerset(L[1:]) #all subsets which don't contain the first element.
	return rest + \
	map(lambda p: [L[0]] + p, rest) #stick first element in each of the previous ones.


def subset(target, L):
	"""Subset sum."""
	def ss(tget, lst):
		if tget == 0:
			return True

		if not lst:
			return False

		if tget == lst[0]:
			return True

		if target < lst[0]:
			return False
		#never returns true haha!


		return ss(tget - lst[0], lst[1:]) or ss(tget, lst[1:])

	return ss(target, sorted(L))

def knapsack(max_wgt, items):
	""" 
	Find max value possible with wgt below max_wgt.
	>>> knapsack(7, [ [2, 100], [3, 112], [4, 125] ])
	237
	Assume weights of all items > 0.
	Return (Max val possible, items to pick)
	"""
	if max_wgt <= 0:
		return 0, []

	if not items:
		return 0, []

	#we either take the first item or not.
	if items[0][0] > max_wgt:
		return knapsack(max_wgt, items[1:])
	v1, s1 = knapsack(max_wgt - items[0][0], items[1:])
	v2, s2 = knapsack(max_wgt, items[1:])
	return (items[0][1] + v1, [items[0]] + s1) if (items[0][1] + v1) > v2 else (v2, s2)



	
def lcs(s1, s2):
	"""
	Find longest common subsequence in s1 and s2.
    Easy optimization? Use 2d array. 
	"""
	if not s1 or not s2:
		return (0, '')

	if s1[0] == s2[0]:
	    x = lcs(s1[1:], s2[1:])
	    return (1+x[0], s1[0]+x[1])

	v1,option1 = lcs(s1[1:], s2) #example: bac and acbd. 
	v2, option2 = lcs(s1, s2[1:]) #example bc and abc
	v3,option3 = lcs(s1[1:], s2[1:]) #example asbc and faebcd
	if v1 >= v2 and v1 >= v3:
		return v1, option1
	if v2 >= v1 and v2 >= v3:
		return v2, option2
	return v3, option3






