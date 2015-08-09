###  sieve.py
###  Compute a list of all primes <= n, and use it to create other prime related functions.


def get_int(msg, MAX=1e9):
    """Read an integer between -MAX and MAX from stdin."""
    x = None
    while True:
        inp = input(msg)
        try:
            x = int(inp)
            if abs(x) > MAX:
                print('Enter a number between {0} and {1} only.'.format(-MAX, MAX))
            else:
                break

        except ValueError as e:
            print('Enter an integer only! \nError: ', str(e))

    return x

def main():
    inp = get_int("Enter the limit for the sieve. Must be an integer.")
    print(sieve(inp))

##if __name__ == '__main__':
##    main()


def sieve(n):
    """
    Return list of all primes <= n.

    >>> sieve(10)
    [2, 3, 5, 7]

    >>> sieve(5)
    [2,3,5]

    >>> sieve(-1)
    []

    n -> integer
    """
    sieve = [(i,True) for i in range(n+1)]
    if n < 2:
        return []
    primes = []
    i = 2

    while i < n+1:
        if sieve[i][1]:
            primes.append(i)
            j = i #For j < i i*j would be crossed by j*i
            while i*j <= n:
                sieve[i*j] = (i*j, False)
                j += 1
        i += 1

    return primes

def prime_before(n):
    """
    Return the largest prime <= n, and None if n <= 1.

    n -> Integer

    >>> prime_before(15)
    13

    >>> prime_before(1)
    """
    return sieve(n)[-1] if sieve(n) else None


def lower_bound(p, e):
    """
    Find and return the last element x and position of that element (1 indexing)
    such that x <= e. Return (None, 0) if p is empty or e < min(p).

    Precondition: p is sorted, e is an integer.

    >>> lower_bound([3,5,7,9,11,13], 5)
    (5, 2)

    >>> lower_bound([3,5,7,9,11,13], 10)
    (9, 4)

    >>> lower_bound([3,5,7,9,9,9,9,9, 11, 11,11, 13, 13], 10)
    (9, 8)

    >>> lower_bound([9,9,9,9,9], 9)
    (9, 5)
    """
    if not p or e < p[0]: #Works due to short circuit evaluation
        return (None, 0)

    if e > p[-1]: #Greater than max(p)
        return p[-1], len(p)

    low = 0
    high = len(p) - 1

    #We perform an O(log(len(p)) iteration where p[low] <= e <= p[high]
    #is maintained at each step.
    mid = (high + low)//2
    while low < high:
        mid = (high + low)//2
        if (high - low) == 1: #The search space is two elements.
            if p[high] == e:
                return p[high], high + 1
            else:
                return p[low], low + 1
        if p[mid] <= e:
            low = mid
        else:
            high = mid


    return (p[mid], mid + 1)

def pi(p):
    """
    Print "p[i], PI(p[i])" for every element in list p
    where PI(x) is number of primes <= x.

    >>> pi([10,100])
    x: 10 PI(X): 4
    x: 100 PI(X): 25

    p -> [Int]
    """
##    for e in p:
##        if isinstance(e, int):
##            print("x: {0} PI(x): {1}".format(e, len(sieve(e))))
##        else:
##            raise ValueError("Cannot compute PI(x) for non-integral x.")

    #----------REFACTORED-------------

    for e in p:
        assert isinstance(e, int), "Elements in the argument (list) must be integral."

    #It is sufficient to call sieve once.
    primes = sieve(max(p))

    for e in p:
        prev_prime, pi = lower_bound(primes, e)
        print("x: {} PI(x): {}".format(e, pi))


def mersennes(n):
    """
    Return a list of mersenne primes <= n.
    n -> Integer
    A prime p is a Mersenne prime if p = 2**k - 1 for some integer k > 0.

    >>> mersennes(1000)
    [3, 7, 31, 127]
    """
    primes = sieve(n)
    k = 0

    mersenne_list = []
    t = 2**k - 1
    while t < primes[-1]:
        t = 2**k - 1

        if lower_bound(primes, t)[0] == t: #If the lower_bound is the element itself (binary search)
            mersenne_list.append(t)

        k += 1
    return mersenne_list

def twin_primes(n):
    """Return list of pairs of all twin primes <= n."""
    primes = sieve(n)
    twin_primes = [(primes[i], primes[i+1]) for i in range(len(primes) - 1) if primes[i+1] - primes[i] == 2]
    return twin_primes
