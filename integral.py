"""
integral.py
Estimate the integral under a function using trapezoids and rectangles.
"""
from __future__ import division

def integrate(f, low, high, N=1000,rectangles=True):
	"""
	Estimate Integral of f between low and high using 1000 rectangles.
	TODO: Fix when function is not defined at a point (try moving it by epsilon to the left or right).
	"""
	try:
		if low > high:
			return - integrate(f, high, low,N,rectangles)

		
		width = high - low
		if width == 0:
			return 0
			if N == 1:
				return f(low)*(f(high) - f(low))
		#steps = [low, low+delta, low+2*delta, ....., low+(n-1)*delta]
		delta = width/N
		lows = [low for i in range(N)]

		steps = map(lambda x: x[0] + delta*x[1], zip(lows, range(N)))
		#print("Steps = %s"%steps)
		if rectangles:
			rect_heights = map(f, steps)
			rect_areas = map(lambda x: x*delta, rect_heights)
			#return reduce(lambda x, y: x+y, map(lambda x: x*delta, map(f, steps)))
			return reduce(lambda x, y: x+y, rect_areas)
		else: #Trapezoids
			
			steps.append(high)	
			try:
				heights = map(f, steps)
			except ZeroDivisionError:
				steps.pop(-1)
				steps.append(high-1e-8) #sometimes the function is not defined at the boundary
				heights = map(f, steps)

			trapezoids = map(lambda x: 0.5*delta*(x[0]+x[1]), zip(heights[1:], heights))
			return reduce(lambda x,y: x+y, trapezoids)

		return None
	except ZeroDivisionError as e:
		print("Could be because of N == 0?")
		raise ZeroDivisionError(e)
	