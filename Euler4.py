__author__ = 'adam'


def isPali(n):
    nstring = str(n)
    length=len(nstring)
    for i in xrange(0,length):
        if nstring[i]!=nstring[length-1-i]:
            return False
    return True

isPali(101)
largestprod = 0

for i in xrange(100,1000):
    for j in xrange(100,1000):
        prod = i*j
        if prod > largestprod and isPali(prod):
            largestprod=prod
            print prod

