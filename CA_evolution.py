"""
CA_Evolution.
View the evolution of a list using a mutate fn.
"""
import random
from collections import defaultdict

def mutate(i, oldL, user = 0):
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    if i == user:
        new_ith_element = oldL[i]^1
    else:
        new_ith_element = oldL[i] # the new is the same as the old
    return new_ith_element

def evolve(lst, mutate_fn, curr_gen=0):
	if not lst:
		return lst
	print str(lst) + " (g: " + str(curr_gen) + ")"
	if all_ones(lst):
		return curr_gen
	new_lst = [mutate_fn(i, lst) for i, _ in enumerate(lst)]
	return evolve(new_lst, mutate_fn, curr_gen+1)


def lights_off(lst, mutate_fn=mutate, curr_gen=0):
	"""
	Play the lights_off game where there is a lst of switches, each
	switch is either on(0) or off(1). The goal is turn every switch off.
	Each move flips the neighbouring switches as well.

	>>> evolve( [0,0,0,0,0,0,0,0] )
	[0, 0, 0, 0, 0, 0, 0, 0] (g: 0)
	Index? 0
	[1, 1, 0, 0, 0, 0, 0, 0] (g: 1)
	Index? 3
	[1, 1, 1, 1, 1, 0, 0, 0] (g: 2)
	Index? 7
	[1, 1, 1, 1, 1, 0, 1, 1] (g: 3)
	Index? 6
	[1, 1, 1, 1, 1, 1, 0, 0] (g: 4)
	Index? 7
	[1, 1, 1, 1, 1, 1, 1, 1] (g: 5)
	5
	"""
	if not lst:
		return None
	print str(lst) + " (g: " + str(curr_gen) + ")"
	if all_ones(lst):
		return curr_gen
	user = int(raw_input("Index? "))
	if user == -1:
		return None
	new_lst = [mutate_fn(i, lst,user) for i, _ in enumerate(lst)]
	if user < len(lst) - 1:
		new_lst = [mutate_fn(i, new_lst, (user+1)%len(lst)) for i, _ in enumerate(lst)]
	if user > 0:
		new_lst = [mutate_fn(i,new_lst,(user + len(lst) - 1)%len(lst)) for i, _ in enumerate(lst)]
	return lights_off(new_lst, mutate_fn, curr_gen+1)


def all_ones(lst):
	return all(x == 1 for x in lst)


def random_bl(N):
	"""Return a random list containing 0 and 1 only, of length N."""
	return [random.choice([0,1]) for i in range(N)]


def play_game():
	"""
	Plays the lighting game.
	"""
	my_map = defaultdict(int)
	my_map.update(dict(zip(['E', 'M', 'H','I'],[4,6,8,10])))
	while True:
		print "Welcome to the Lights game."
		print "What difficulty mode do you wish? Enter E(4), M(6), H(8), I(10) for Easy, Medium, Hard or Insane."

		N =  my_map[raw_input()]
		lst = random_bl(N)
		print " Here is your list."
		print (lst)
		print "The game starts now, if you wish to stop, enter -1 at any point."
		result = lights_off(lst)
		if result is None:
			print ("Don't worry! It's possible that this list was unsolvable.")
		else:
			print ("Well done, you solved it in %d moves!"%result)

		print("Do you want to continue? y/n")
		ch = raw_input()
		if ch == 'n':
			break
