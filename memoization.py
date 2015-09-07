#memoization
import sys
sys.setrecursionlimit(20000)

##### Memoization in LCS
lcs_cache = {}
def lcs_memo(s1, s2):
	if (s1,s2) in lcs_cache:
		return lcs_cache[(s1,s2)]

	if not s1 or not s2:
		lcs_cache[(s1, s2)] = (0, '')
	elif s1[0] == s2[0]:
		len_rest, rest = lcs_memo(s1[1:], s2[1:])
		lcs_cache[(s1,s2)] = (1+len_rest, s1[0] + rest)
	else:
		#print "Here,", s1,s2
		l1, o1 = lcs_memo(s1, s2[1:]) 
		l2, o2 = lcs_memo(s1[1:], s2)
		lcs_cache[(s1,s2)] = (l1, o1) if l1 > l2 else (l2,o2)
	#print "returning", lcs_cache[(s1,s2)]
	return lcs_cache[(s1,s2)]

align_cache = {}
def align(s1, s2):
	if (s1,s2) in align_cache:
		return align_cache[(s1,s2)]

	if not s1:
		align_cache[(s1, s2)] = (0, '-'*len(s2), s2)
	elif not s2:
		align_cache[(s1,s2)] = (0, s1, '-'*len(s1))
	elif s1[0] == s2[0]:
		len_rest, rest_1, rest_2 = align(s1[1:], s2[1:])
		align_cache[(s1,s2)] = (1+len_rest, s1[0] + rest_1, s1[0] + rest_2)
	else:
		#print "Here,", s1,s2
		l1, os11, os12 = align(s1, s2[1:]) 
		l2, os21, os22 = align(s1[1:], s2)
		align_cache[(s1,s2)] = (l1, '-'+os11,s2[0]+os12) if l1 > l2 else (l2,s1[0]+os21,'-'+os22)
	#print "returning", lcs_cache[(s1,s2)]
	return align_cache[(s1,s2)]
 

###### Memoizing Coin change
coins_memo = {}
def coin_change_memo(amount, coins):
	"""Minimum number of coins required to make an amount."""
	if (amount, coins) in coins_memo:
		return coins_memo[(amount, coins)]
	#not memoized? memoize now.
	if amount <= 0:
		coins_memo[(amount, coins)] = (0, [])
	elif not coins:
		#print amount, coins
		coins_memo[(amount, coins)] = (float("inf"), [])
	elif coins[0] > amount:
		coins_memo[(amount, coins)] = coin_change_memo(amount, coins[1:])
	else:
		o1, c1 = coin_change_memo(amount - coins[0], coins)
		o2, c2 = coin_change_memo(amount, coins[1:])
		coins_memo[(amount, coins)] = (1 + o1, [coins[0]]+c1) if (1+o1) < o2 else (o2,c2)
	#print amount, coins, coins_memo[(amount, coins)]
	return coins_memo[(amount, coins)]


edit_cache = {}

def edit_distance(s1, s2):
	"""Return the minimum number of edits required to move from s1 to s2."""
	if (s1,s2) in edit_cache:
		return edit_cache[(s1,s2)]
	if len(s1) == 0:
		edit_cache[(s1,s2)] = len(s2)
		return len(s2) #need at add s2 one by one. because only an addition increases length.
	if len(s2) == 0:
		edit_cache[(s1,s2)] = len(s1)
		return len(s1)
	#neither of s1 or s2 is zero
	if s1[0] == s2[0]:
		#cool 
		return edit_distance(s1[1:], s2[1:])
	#fix s1
	o1 = 1 + edit_distance(s1, s2[1:]) #insert
	o2 = 1 + edit_distance(s1[1:], s2) #delete
	o3 = 1 + edit_distance(s1[1:], s2[1:]) #substitute
	#print (s1,s2,o1,o2,o3)
	edit_cache[(s1,s2)] = min(o1,o2,o3)
 	return edit_cache[(s1,s2)]