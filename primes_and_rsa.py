import random

#prime sieve:

def sieve(n):
	"""Return a list of primes in [1, 2, ..., n]:"""
	if not isinstance(n, int):
		try:
			n = int(n)
		except ValueError as e:
			print('Cannot create sieve. Invalid input for sieve limit. ' + e)

	if n < 2:
		return []
	numbers = range(n+1)
	primes = []
	#not primes
	numbers[0] = -1
	numbers[1] = -1
	i = 2
	while i <= n:
		if numbers[i] != -1:
			primes.append(i)
			j = i
			while i*j <= n:
				numbers[i*j] = -1
				j += 1
		i += 1

	return primes


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def fast_exp(x, e, modulo=None):
	if e == 0:
		return x%modulo
	if modulo is None:
		res = 1
		while e:
			if e%2:
				res = res*x
				e -= 1
			else:
				e = e>>1
				x = x*x
		return res
	else:
		res = 1
		while e:
			if e%2: #e is odd
				res = res*x
				res = res%modulo
				e -= 1
			else:
				e = e>>1
				x = x*x
				x = x%modulo
		return res



def rsa(primes = None):
	"""Return an encoder and decoder function for the sender and receiver respectively."""
	if primes is None:
		primes = sieve(10**6)

	p1 = random.choice(primes)
	p2 = random.choice(primes)
	while p2 == p1 and p2 < 10:
		p2 = random.choice(primes)

	n = p1*p2
	m = (p1 - 1)*(p2 - 1)
    # e is prime between 1 and m which is coprime to m.
	e = None
	while True:
		e = random.choice(primes)
		if e < m and m%e != 0:
			break



    # d is the inverse of e under m.

	d = modinv(e, m)
	encrypter = lambda msg: fast_exp(msg, e, modulo=n)#can make this fast_exp
	decrypter = lambda x: fast_exp(x, d, modulo=n)
	return encrypter, decrypter









	




