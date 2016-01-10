__author__ = 'adam'

import primes


class PrimeHolder:
    primelist = primes.numpyPrimes(10 ** 6)
    primeset = set(primelist)


def newNumDistFactors(x):
    if x in PrimeHolder.primeset:
        return 0
    num = 0
    for prime in PrimeHolder.primelist:
        if x % prime == 0:
            num += 1
            while x % prime == 0:
                x = x / prime
        if prime > x:
            return num


print newNumDistFactors(645)
num = 0
x = 10
while num < 4:
    x += 1
    if newNumDistFactors(x) == 4:
        num += 1
    else:
        num = 0
print str(x) + " and" + str(x - 1) + " and" + str(x - 2) + " and" + str(x - 3)
