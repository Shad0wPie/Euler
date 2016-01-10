__author__ = 'adam'

import primes
import pandigit
import numpy as np


primelist = primes.numpyPrimes(1000000000)
print len(primelist)
print 'done with primes'
for i in np.nditer(primelist):
    if pandigit.isPandigital(i):
        print i
print 'done'