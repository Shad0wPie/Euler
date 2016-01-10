__author__ = 'adam'

import primes
from math import sqrt


def isGoldbach(x):
    for i in primes.numpyPrimes(x):
        rest  = sqrt((x-i)/2)
        if int(rest) - rest == 0:
            return True
    return False

n=33
while True:
    n=n+2
    while (primes.isPrime(n)):
        n=n+2
    if not isGoldbach(n):
        print n
        break
