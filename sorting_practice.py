#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Akshay
#
# Created:     19-06-2015
# Copyright:   (c) Akshay 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import operator




def main():
    pass

if __name__ == '__main__':
    main()

def linear_search(p, x):
    """Search for x in p."""
    for e in p:
        if e == x:
            return True
    return False


def search(p, e):
    """
    List[E] E -> Boolean
    Produce true if e is in list p at least once, false otherwise.
    """
    def binary_search(q, f):
        """
        List[E] E -> Boolean
        Produce true if f is in list q at least once, false otherwise.
        """
        low = 0
        high = len(q)
        while low < high:
            mid = (low + high)//2
            if q[mid] == f:
                return True
            elif q[mid] > f:
                high = mid
            else:
                low = mid + 1

        return False

    if len(p) == 0:
        return False

    return binary_search(p, e)

def check_expect(f, args, expected_value):
    """
    function tuple -> Boolean
    Return whether f applied to tuple args returns the value expected.
    """
    return f(*args) == expected_value


def test_search():
    args_list = [([1,2,4,4,4], 1), ([0,3,3,13], 13), ([],5), ([1,21,123], 13), ([1,2,3,4,4,5,6,6,6], 6), ([6,6,6,6],7), ([10,12],11), ([10,12,14], 13)]
    expectations = [True, True, False, False, True, False, False, False]
    for i,e in enumerate(args_list):
        print(e)
        assert check_expect(search, e, expectations[i]), "{} not equal to {} for {}".format(search(*e), expectations[i], e)

    print("All tests for search passed!")

def linear_search(p, x):
    """
    List[E] E -> Boolean
    Produce true if x is in list p at least once, false otherwise.
    """
    for e in p:
        if e == x:
            return True
    return False

def sel_sort(p):
    """Sort in place."""
    for sorted_till in range(len(p)):
        current_min = sorted_till
        for i in range(sorted_till, len(p)):
            if p[i] < p[current_min]:
                current_min = i

        p[current_min], p[sorted_till] = p[sorted_till], p[current_min]

    return p
def test_sort():
    assert(check_expect(sel_sort, ([3,3,4,1,1,132,1,5,1,1],), sorted([3,3,4,1,1,132,1,5,1,1])))
    assert(check_expect(sel_sort, ([],), []))
    assert(check_expect(sel_sort, ([1,3,2],), [1,2,3]))
    print('All selection sort tests passed!')


def merge(p,q, compare = operator.lt):
    """Merge two sorted lists p and q into one sorted list and return it."""
    assert sorted(p) == p
    assert sorted(q) == q

    if not q:
        return p

    if not p:
        return q

    res = []
    p_pointer = 0
    q_pointer = 0
    while p_pointer < len(p) and q_pointer < len(q):
        if compare(p[p_pointer],q[q_pointer]):
            res.append(p[p_pointer])
            p_pointer += 1
        else:
            res.append(q[q_pointer])
            q_pointer += 1

    if p_pointer < len(p):
        res.extend(p[p_pointer:])
    if q_pointer < len(q):
        res.extend(q[q_pointer:])

    return res




def merge_sort(L, compare = operator.lt):

    if len(L) < 2:
        return L[:]

    mid = len(L)//2
    lower = merge_sort(L[:mid], compare)
    upper = merge_sort(L[mid:],compare)
    return merge(lower, upper, compare)


def a_search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        print('i = {}'.format(i))
        print('L[size-i-1] = {}'.format(L[size-i-1]))
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False