__author__ = 'adam'
import primes
import time

before = time.time()
primelist1=primes.numpyPrimes(10**10)
after = time.time()
print 'time to calculate : ' + str(after-before)
print len (primelist1)
print primelist1[-1]

before = time.time()
primelist = primes.readPrimes(10**8)
after = time.time()
print 'time to read : ' + str(after-before)
