__author__ = 'adam'

import primes

primelist = set(primes.primes(1000000))
smallprimes =primes.primes(1000)

def primecount(a,b):
    number = b
    n=0
    while number in primelist:
        n+=1
        number = n**2 + a*n + b
    return n

largestCount = 0
produkt = 0
for a in xrange(-1000,1000):
    for b in smallprimes:
        count = primecount(a,b)
        if count>largestCount:
            produkt=a*b
            largestCount=count
print largestCount
print produkt