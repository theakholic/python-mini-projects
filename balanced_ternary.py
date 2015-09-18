#num to balanced ternary
#so i have a number first
from __future__ import print_function

forward_map = {1: '+', -1: '-', 0: '0'}
backward_map = {value: key for key,value in forward_map.items()}

def bter(n):
	if n == 0:
		return '0'
	if n < 2:
		return forward_map[n]
	remainder = n%3
	#if n == 0 or 1 needs to be zero at the end
	if n%3 != 2:
		return bter(n//3)+forward_map[n%3]
	return bter((n+1)//3)+forward_map[-1]
	#what about n%3 == 2 14


#Think time
# 3 = 0+0
# 4 = 0++
# 5 = +-- Nine minus 4
# 6 = +-0
# 7 = +-+ 
# 8 = +0-
# 9 = +00
# 10 = +0+
# 11 = ++-
# 12 = 
# 13 = +++ #9+3+1
# 14 = +--- 27-9-4  +-- = 5*3
# 3^n = +00000..n zeroes...0




def evaluate_bter(s):
	#a string of the form "+0-"
	if not s:
		return 0
	return backward_map[s[-1]] +  3*evaluate_bter(s[:-1])


if __name__ == '__main__':
	print("Enter positive number to be converted to balanced ternary")
	n = int(raw_input())
	assert n > 0, "Input must be a positive integer"
	s = bter(n)
	try:
		assert evaluate_bter(s) == n
	except KeyError as e:
		print("The answer has extraneous characters.\n",e)
	else:
		print(s)

