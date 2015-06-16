#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Akshay
#
# Created:     16-06-2015
# Copyright:   (c) Akshay 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    if b > x:
        return 0

    res = []
    while x:
        res.append(x%b)
        x = x//b
    return (len(res) - 1)