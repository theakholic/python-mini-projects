

def insert(ls, pos):
    """
    Insert ls[pos] into ls[:pos].
    ASSUME: pos >= 1, ls[:pos] is sorted, len(ls) > pos"""
    if pos == 0:
        return ls
    assert pos >= 1

    elem = ls.pop(pos)
    j = pos - 1
    while j >= 0 and ls[j] > elem:
        j -= 1

    ls.insert(j + 1, elem) #WHY j+1? The prev loop ends when j < 0 or ls[j] <= elem. Our elem should be at ls[j+1]

def insertion_sort(a):
    #sorted = [14 17]  [16 18 20]
    if len(a) <= 1:
        return a

    i = 1
    l = len(a)
    while i < l:
        #insert a[i] in a[0:i]
        insert(a, i)
        i+=1

    return a


def rev_recursive(ls):
    if len(ls) < 2:
        return ls

    return rev_recursive(ls[1:]) + [ls[0]]


def gray_codes(n):
    """
    A list of n-bit Gray codes.
    Gray code -> two successive bit patterns differ one by only 1 character.

    >>> gray_codes(3)
    ['000', '001', '011', '010', '110', '111', '101', '100']
    """
    if n == 1:
        return ['0', '1']

    p = gray_codes(n-1)
    return list(map(lambda s: '0' + s,p)) + list(map(lambda s: '1' + s, p[::-1]))










import operator

def merge(l1, l2, less_than):
    """Merge two sorted lists l1 and l2"""
    if not l1:
        return l2
    if not l2:
        return l1

    p1 = 0
    p2 = 0

    res = []

    #print("l1: {}, l2: {}".format(l1, l2))
    #print("lt == operator.lt {}".format(less_than==operator.lt))
    while p1 < len(l1) and p2 < len(l2):
        if less_than(l1[p1], l2[p2]):
            res.append(l1[p1])
            p1 += 1
        else:
            res.append(l2[p2])
            p2 += 1

    if p1 < len(l1):
        res.extend(l1[p1:])

    if p2 < len(l2):
        res.extend(l2[p2:])

    #print("res: {}".format(res))

    return res

def merge_sort_r(a, less_than = operator.lt):
    """Sort a, Assumption: a is a list."""
    if len(a) < 2:
        return a

    #print(less_than)

    return merge(merge_sort_r(a[:len(a)//2], less_than), merge_sort_r(a[len(a)//2:], less_than), less_than)


def merge_sort_desc(a):
    return merge_sort_r(a, operator.gt)






def scrabble_sort(ls):
    """Sort list of strings according to length, and then arrange words of same length in alphabetical order."""
    def f(s1, s2):
        if len(s1) == len(s2):
            return s1 < s2

        return len(s1) < len(s2)

    return merge_sort_r(ls, f)






def gcd(a,b):
    assert isinstance(a,int) and isinstance(b, int), "Cannot compute gcd if both not natural numbers"
    if a <= 0 or b <= 0:
        return None

    a, b = (a,b) if a < b else (b,a) #ensure a < b

    while b%a:
        a, b = b%a, a


    return a





ITERATION_LIMIT = 100

def collatz(n, lim = ITERATION_LIMIT):
    results = []
    results.append(n)
    i = 0
    while n != 1 and i < lim:
        i += 1
        if n%2:
            n = 3*n + 1
        else:
            n = n//2
        results.append(n)

    return results






import random

def qsort(a, less_than=operator.lt):
    def partition(a, pos):
        """Partition a into elements < a[pos], a[pos] and elements >= a[pos]"""
        e = a.pop(pos)
        lesser = [x for x in a if less_than(x, e)]
        greater = [x for x in a if not less_than(x, e)]
        return (lesser + [e] + greater, len(lesser))

    if len(a) < 2:
        return a

    pos = random.choice(range(len(a)))
    a, splitter = partition(a, pos)

    return qsort(a[:splitter], less_than) + [a[splitter]] + qsort(a[splitter + 1:], less_than)
