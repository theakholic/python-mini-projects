from math import sqrt

def smallest_divisor(n,curr):
	if (curr*curr) > n:
		return n	
	if n%curr == 0:
		return curr

	return smallest_divisor(n, curr+1)


def prime(n):
	return smallest_divisor(n,2) == n

def p_sos(n):
	for x in range(1,n+1):
		for y in range(x,n+1):
			if x*x + y*y == n:
				print n, (x,y)

def prime_sum_of_squares(n):
	for i in range(2,n+1):
		if prime(i):
			p_sos(i)


def exp(b,e):
	def my_exp(b,e, val):
		if e == 0:
			return val
		if e%2 == 0:
			return my_exp(b*b, e/2, val)
		return my_exp(b, e-1, val*b)
	return my_exp(b,e,1)

def divides(k,n):
	return n%k == 0

def try_it(n):
	for i in range(2,n+1):
		if divides(i,exp(2,i-1) - 1):
			print i


def question_5(n):
	a_old = 1
	b = 1
	for i in range(n):
		a_new = a_old + b
		b = a_old + a_new
		#print (a_new/float(b))**2	
		a_old = a_new
	print (a_new/float(b))**2








