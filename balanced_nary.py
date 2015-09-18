#balanced n-ary
#for n odd
#use digits -(n-1)/2, ...., 0, ... (n-1)/2
from __future__ import print_function

def balanced_nary(inp, n):
	"""
	Return a list containing the balanced n-ary representation of inp.
	Assume:
		1) n is an integer
		2) 1 < n < 20 [so that 0-9 suffices]
		3) inp is an integer

	>>> balanced_nary(421,7)
	[0, 1, 2, -3, 1]
	#Because 1*(7**0) + (-3)*(7**1) + 2*(7**2) + 1*(7**3) = 421
	"""
	#print("inp:",inp)
	if inp == 0:
		return [0]
	if inp < 0:
		return map(lambda x: -x, balanced_nary(-inp,n))

	if inp%n <= (n-1)//2:
		return balanced_nary(inp//n,n)+[inp%n]

	negative_remainder = inp%n - n #inp%n > (N-1)/2 
	return balanced_nary((inp - negative_remainder)//n, n) + [negative_remainder]

def eval_balanced_nary(s, n):
	if not s:
		return 0
	return s[-1] + n*eval_balanced_nary(s[:-1],n)



if __name__ == '__main__':
	n = int(raw_input("Enter n, the base for conversion. Ensure [1 < n < 20] and n odd.\n"))
	assert n%2, "N must be odd"
	assert 0 < n < 20, "0 < n < 20 must hold"
	x = int(raw_input("Enter the number to be converted to base n:\n"))
	assert isinstance(x, int)
	ans = balanced_nary(x,n)
	print(ans)
	assert eval_balanced_nary(ans, n) == x
	#print(ans)
