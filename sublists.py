#Threeze!
from scrabble_dict import *
import scrabble

def listToString(p):
	"""Convert list of characters to a string."""
	return ''.join(p)

def my_filter(f, p):
	if not p:
		return []
	return p[0] + my_filter(f, p[1:]) if f(p[0]) else my_filter(f, p[1:])

def sublists(l, n):
	"""Return all sublists of length n of l."""
	if n == 0:
		return [[]] #THERE IS ONE SUBLIST, THE EMPTY LIST
	if n > len(l):
		return [] #THERE ARE NO SUBLISTS
	if n < 0:
		raise ValueError("Cannot construct sublist of negative length.")
	#either the sublist contains n or not.
	return map(lambda x: [l[0]] + x, sublists(l[1:], n-1)) + sublists(l[1:], n)

def my_reduce(f, L):
	"""Reduce L by f."""
	if not L:
		raise ValueError("Cannot reduce a list with no elements")
	if len(L) == 1:
		return L[0]

	return my_reduce(f, [f(L[0], L[1])] + L[2:])

def permutations(L):
	"""Return all permutations of a list."""
	def stick_at_i(i, item, lst):
		return map(lambda x: x[:i] + [item] + x[i:],lst)
	if not L:
		return [[]]
	rest = permutations(L[1:])
	#stick into pos 0, .... pos(n-1)
	head = L[0]
	stick_head = [stick_at_i(i, head, rest) for i in range(len(L))]
	return reduce(lambda x, y: x+y, stick_head)


def best_three(rack):
	"""Return highest scoring three letter word and its score."""
	return scrabble.best_word(filter(lambda x: len(x[0]) == 3, scrabble.wordList(rack)))



#threeze = lambda rack: reduce(lambda x,y: x+y,[map(listToString,filter(lambda y: y in words, sublists(rack,n))) for n in range(len(rack))])
threeze = lambda rack: reduce(lambda x,y: x+y,[filter(lambda y: y in words, map(listToString,sublists(rack,n))) for n in range(len(rack))])
