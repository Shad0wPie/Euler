__author__ = 'adam'

import pandigit
import primes
import itertools

primelist = primes.numpyPrimes(20)

def isPrimeDivisible(n):
    for i in xrange(7):
        if int(n[1+i:4+i]) % primelist[i]!=0:
            return False
    return True


count=0
list=[]

for i in itertools.permutations('0123456789'):
    i=''.join(i)
    if i[0]=='0':
        continue
    if isPrimeDivisible(i):
        list.append(int(i))

print list
print sum(list)