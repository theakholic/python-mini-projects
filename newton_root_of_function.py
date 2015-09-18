
# newton's method to find roots of any function
dx = 1e-8
EPSILON = 1e-8


def deriv(g):
	"""Return a function f such that f(x) is approximately dg/dx(x)"""
	return lambda x: (g(x+dx) - g(x))/dx

def fixed_point(f, start, max):
	"""
	Find x such that f(x) is approximately x.
	start is the initial guess.
	max is the maximum number of iterations.
	"""
	def average_damp(g):
		return lambda x: (x + g(x))/2.0

	def good_enough(x):
		return abs(f(x) - x) < EPSILON

	curr = 0
	guess = start
	ad = average_damp(f)
	while curr < max:
		if good_enough(guess):
			break
		guess = ad(guess)
		curr += 1
	return guess

def newton_root(g, initial_guess, max_iter=1000):
	"""Given a function g: Float -> Float, estimate x such that g(x) = 0"""
	def newton_modify(f):
		return lambda x: x - f(x)/(deriv(f))(x)
	d = deriv(g)
	return fixed_point(newton_modify(g),initial_guess,max_iter)


#Using this newton root, we can define many functions!
newton_sqrt = lambda x: newton_root(lambda y: y*y - x, 1.0)
