#-----------RNA FOLDING---------------#
# An RNA is a string made up of letters from "A","U","C" and "G".
# RNA folds in a way that puts it in the most stable, low energy states.
# We can approximate as max number of paired bases.
# Using the following rules
# 	A can pair with U and G can pair with C.
#	A base can pair only once
#	When two nucleotides pair, any bases between them can pair too
#	Pairing cannot take place between a nucleotide inside the loop and one outside
opposite = {"A": "U", "U": "A", "G" : "C", "C": "G"}

def fold(RNA):
	if len(RNA) < 2:
		return 0
	#more than 2 elements
	first = RNA[0]
	#loseit
	o1 = fold(RNA[1:])
	t = [1 + fold(RNA[1:i]) + fold(RNA[i+1:]) for i,c in enumerate(RNA) if c == opposite[first]]
	t = [0] if not t else t
	return max(max(t), o1)

fold_cache = {}
def mfold(RNA):
	if RNA in fold_cache:
		return fold_cache[RNA]
	if len(RNA) < 2:
		fold_cache[RNA] = (0,[])
		return 0,[]
	#more than 2 elements
	first = RNA[0]
	#loseit
	o1 = mfold(RNA[1:])
	t = [(1 + mfold(RNA[1:i])[0] + mfold(RNA[i+1:])[0], [(0,i)] + map(lambda x: (x[0]+i+1,x[1]+i+1),mfold(RNA[i+1:])[1]) + map(lambda x: (x[0]+1,x[1]+1),mfold(RNA[1:i])[1])) for i,c in enumerate(RNA) if c == opposite[first]]
	t = [(0,[])] if not t else t
	fold_cache[RNA] = max(max(t, key = lambda x: x[0]), o1, key=lambda x: x[0])
	return fold_cache[RNA]


	

