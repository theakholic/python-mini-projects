import sys
from bigdict import *
sys.setrecursionlimit(10000) 

scrabble_scores = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

#Dictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy", "zzyzva"] 


def word_score(word, scores=None):
	"""
	Return the score of the word using the scorelist scores.

	>>> word_score("holy", {"o": 1, "h":2, "l":5, "y":3})
	11

	Second argument (scores) is optional (defaults to scrabble scores).
	Return value: The score (Int)
	"""
	if scores is None:
		scores = scrabble_scores
	return reduce(lambda x, y: x+y, map(lambda x: scores[x], word),0)

def remove(c, rack):
	if c != rack[0]:
		return [rack[0]] + remove(c, rack[1:])
	return rack[1:]
		


def in_rack(word, rack):
	if not word:
		return True

	if word[0] not in rack:
		return False

	return in_rack(word[1:], remove(word[0], rack))


#Best word returns the highest scoring word for a given group of letters
best_word = lambda rack: reduce(lambda x, y: x if x[1] > y[1] else y, scoreList(list(rack)), (None, -1))


def scoreList(rack):
	return map(lambda x: (x, word_score(x)), filter(lambda word: in_rack(word, rack), Dictionary))











    