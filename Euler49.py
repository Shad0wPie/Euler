__author__ = 'adam'

import primes

primelist = primes.numpyPrimes(10000)
for i in xrange(len(primelist)):
    if primelist[i] > 1000:
        primelist = primelist[i:]
        break
print primelist
primeset = set(primelist)

def isPermutation(a,b):
    a=str(a)
    b=str(b)
    while len(a)>0:
        if not a[0] in  b:
            return False
        b=b.replace(a[0],'',1)
        a=a[1:]
    return True

for index,i in enumerate(primelist):
    for j in primelist[index+1:]:
        if not isPermutation(i,j):
            continue
        k=j + j-i
        if k in primeset and isPermutation(j,k):
            print str(i) + str(j) + str(k)
