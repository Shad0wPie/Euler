__author__ = 'adam'

#bruteforce

n=100

sumsq=0
sqsum=0
for i in xrange(1,n+1):
    sumsq+=i**2
    sqsum+=i

sqsum=sqsum**2
print sqsum
print sumsq
print sqsum-sumsq

#25164150