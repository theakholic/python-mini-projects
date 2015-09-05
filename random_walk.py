from __future__ import division
import random
import sys


sys.setrecursionlimit(20000)

#Random Walks


def random_step():
	"""Make a random step in either forward or backward direction."""
	return random.choice([-1,1])


def rwpos(start, steps):
	"""
	Return the position of the random walker after "steps"
	number of steps if he starts from position "start".
	"""
	if steps <= 0:
		return start
	#print "start is", start
	return rwpos(start+random_step(), steps-1) #An interative process

def sleeper_image(left=False):
	if left:
		return "0->-<"
	return ">"+"0->-<"[-2::-1]




def display(start, low, high, moving_left=False):
	#low, low + 1, ..., low + k = start, ..., low + r = high
	r = high - low
	k = start - low
	beg = max(0, k)
	rest = max(0, r-k)
	return "||" + " "*beg + sleeper_image(moving_left) + " "*rest + "||" + " (pos = " + str(start) + ")"

def rwsteps(start, low, high, prev_start=None):
	"""
	Simulate a random walk and return number of steps
	for walker to get out of range(low, high+1).
	Assume: low <= start <= high
	"""
	if start < low or start > high:
		return 0
	if high == low:
		return 1
	moving_left = (start - prev_start) < 0 if prev_start is not None else False
	print display(start, low, high,moving_left=moving_left)
	return 1 + rwsteps(rwpos(start,1), low, high, start)



def avg_distance(steps, trials=1000):
	"""
	Calculate the avg_distance of the random walker for
	"steps" number of steps.
	"""
	return sum(abs(rwpos(0, steps)) for i in xrange(trials))/trials

def avg_sqrd_distance(steps, trials=1000):
	def sqr(x): return x*x
	return sum(sqr(rwpos(0, steps)) for i in xrange(trials))/trials

def avg_signed_distance(steps,trials=1000):
	return sum(rwpos(0, steps) for i in xrange(trials))/trials

def test_walker():
	numbers = [10,20,40,80,100,200,400,1000,5000, 10000]
	return zip(numbers, map(avg_distance,numbers))


def TODO():
	return ["Multiple walkers", "2d random walk using turtle maybe?"]

