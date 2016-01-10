__author__ = 'adam'

import primes as p

primelist = set(p.primes(10**6))

def rotate(n):
    return n[1:] + n[0]

def isCircularPrime(n):
    n=str(n)
    for i in xrange(len(n)):
        if int(n) in primelist:
            n=rotate(n)
        else:
            return False
    return True

list=[]
for i in xrange(10**6):
    if isCircularPrime(i):
        print i
        list.append(i)

print list
print len(list)