my_dict = {-1:'-', 1: '+', 0: '0'}
other_dict = {2: -1, 0: 0, 1: 1}
reverse = {'-': -1, '+': 1, '0': 0}
def balanced_ternary(n):
	assert n >= -1 and isinstance(n, int)
	return bternary(n)
	
def bternary(n):
	if n < 2:
		return my_dict[n]
	last = other_dict[n%3]
	if last == -1:
		x = bternary(n//3 + 3)
		return x[:-1]+my_dict[reverse[x[-1]] - 1]
		 
	else:
		return bternary(n//3) + my_dict[last]

	



