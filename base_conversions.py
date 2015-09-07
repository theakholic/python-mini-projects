#convert numbers from decimal to other system


numToTernary = lambda n: numToTernary(n//3) + str(n%3) if n > 2 else str(n)

ternaryToNum = lambda s: 3*ternaryToNum(s[:-1]) + int(s[-1]) if len(s) > 1 else int(s)

#1 < k < 10 please!
numToBaseK = lambda n, k: numToBaseK(n//k, k) + str(n%k) if n >= k else str(n)

BaseKtoN = lambda s, k: k*BaseKtoN(s[:-1], k) + int(s[-1]) if len(s) > 1 else int(s) 


