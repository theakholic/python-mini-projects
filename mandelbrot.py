import sys
sys.path.insert(0,r"./mandelbrot")

from cs5png import *


NUM_ITERATIONS = 100
WIDTH = 600
HEIGHT = 400
# X_MIN = -1.3
# X_MAX = -1.0
# Y_MIN = 0.1
# Y_MAX = 0.3

X_MAX = -.6
X_MIN = -1.2
Y_MAX = -.1
Y_MIN = -.5

def update(c,n):
	"""
	Start with z = 0, and run z' = z**2 + c n times.
	The Mandelbrot update step.
	"""
	z = 0
	for i in range(n):
		z = z**2 + c
	return z

#Mandelbrot set.
#Choose a complex number c. 
#With this c in mind, start with z_0 = 0
#and repeatedly iterate 
# z_n+1 = z_n**2 + c
# the mandelbrot set is the collection of all c
# for which this does not diverge to infinity 

def inMSet(c, n):
	"""Return True if c is likely in mandelbrot set."""
	z = 0
	for i in range(n):
		z = z**2 + c
		if abs(z) > 2:
			return False
	return True

def weWantThisPixel(col, row):
	return inMSet(col+row*1j,NUM_ITERATIONS)


def scale(current_pix, max_pix, f_min, f_max):
	"""Map 0 to max onto f_min to f_max."""
	f = lambda x: f_min + x*(f_max-f_min)/max_pix
	return f(current_pix)

def draw():
	width = WIDTH
	height = HEIGHT
	image = PNGImage(width,height)

	for col in range(width):
		for row in range(height):
			if weWantThisPixel(scale(col,width,X_MIN,X_MAX),scale(row, height,Y_MIN,Y_MAX)):
				image.plotPoint(col,row)

	image.saveFile()

