"""
making_change.py
Given an amount and a list of coin types (of the form [v1, v2, ..., vn])
find the least number of coins that make up that value of money.
"""

US_COINS = [1, 5, 10, 25, 50]
SHMORBIA_COINS = [1, 7, 24, 42]

def cg(amount, coins):
	"""
	Helper function for the change function. Do not use this function,
	use change instead.
	Here preconditions are weaker as coins can be empty as well.

	>>> change(35, [1, 3, 16, 30, 50])
	(3, [3, 16, 16])
	"""
	if amount == 0: 
		return 0, []



	#take first coin
	if not coins or amount < coins[0]:
		return float("inf"), []

	first = coins[0]
	v1, ans1 = cg(amount-first, coins)


	#don't take it
	rest = coins[1:]
	v2, ans2 = cg(amount, coins[1:])

	return (1+v1, [first] + ans1) if (v1 + 1) < v2 else (v2, ans2)



	


def change(amount, coins):
	"""
	Return a non-negative integer indicating the minimum number of coins
	required to make up the given amount.

	Preconditions:
		amount -> non-negative integer
		coins -> list of coin values (1 must always be present in list).

	"""
	assert amount >= 0 and 1 in coins, "Does not satisfy preconditions for fn 'change'."
	return cg(amount, sorted(coins))




	