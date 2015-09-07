#my spell check
import heapq
from memoization import edit_distance
import time

HITS = 10 #How many alternatives?

def load_words():
	words = []
	with open("3esl.txt") as f:
		for line in f:
			words.append(line.strip())
	return words




def main_loop():
	exit_chars = ["~quit", "~q", "~exit", "~e"]
	print("Loading words...")
	words = load_words()
	print("Done.")
	print ("This is a spell checker. Enter ~q or ~quit or ~exit to quit.")
	while True:
		print "spell check>",
		word = raw_input()
		if word in exit_chars:
			print("Exiting Now.")
			break
		if word in words:
			print "Correct."
		else:
			t1 = time.time()
			best = heapq.nsmallest(HITS,map(lambda x: (edit_distance(x,word),x), words))
			print "Suggested alternatives:"
			for wordx in best: print wordx[1]
			t2 = time.time()
			print "Computation time:", t2 - t1, "seconds"








if __name__ == '__main__':
	main_loop()