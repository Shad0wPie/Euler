__author__ = 'adam'

#sum of all primes below 2000000

def primes (n):
    primelist=[]
    for i in xrange(2,n):
        isprime=True;
        for j in primelist:
            if j>i**0.5:
                break
            if i%j==0:
                isprime=False
                break
        if(isprime):
            primelist.append(i)
    return primelist

primelist = primes(2000000)
sum=0
for i in primelist:
    sum+=i
print len(primelist)
print sum

# 142913828922