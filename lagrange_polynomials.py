# #lagrange_polynomial
from __future__ import division
# def lagrange(points):
# 	"""
# 	Given a list of n distinct points, return a polynomial function
# 	which passes through each point.
# 	"""
# 	#PI yj*(x-x1)(x-x2)....(x-xj_1)(x-xj+1)...(x-xn)/(xj - x1)...(xj-xn)
# 	#NEED THIS PRODUCT FOR EACH X
# 	#[(1,1),(2,4),(3,9)]
# 	#print(points)
# 	#functions = [lambda w: (y*reduce(lambda p,q: p*q, [w - t for (t, _) in points if t != x])/reduce(lambda p,q: p*q,[x-t for (t,_) in points if t != x])) for (x,y) in points]
# 	functions = []
# 	for (x,y) in points:
# 		prod = 1
# 		fs = []
# 		for (p, _) in points:
# 			if x != p:
# 				prod = prod*(x-p)
# 				fs.append(lambda t: (x-t))
# 		curr_f = reduce(lambda f1, f2: lambda t: f1(t)*f2(t),fs)
# 		functions.append(lambda w: y*curr_f(w)/prod)


# 	f = reduce(lambda f1, f2: lambda x: f1(x)+f2(x),functions)
# 	return f, functions


def lagrange(points):
	"""
	Given a list of n distinct points, return a polynomial function
	which passes through each point.
	"""
	def P(w): #Return this Polynomial function
		res = 0
		for (x,y) in points: #for each tearm
			def curr_f(t): #Create a function
				prod = y
				for (p,_) in points:
					if p != x:
						prod = prod * (t-p)
						prod = prod/(x-p)
				return prod
			res += curr_f(w) 
		return res
	return P



