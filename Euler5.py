__author__ = 'adam'
import primes

def numDivisibleBy(number,divider,counter=0):
    if number%divider==0:
        return numDivisibleBy(number/divider,divider,counter+1)
    else:
        return counter

max = 20

primelist = primes.primes(max)
primecount= []
for i in xrange(0,len(primelist)):
    primecount.append(0)

for i in xrange(2,max+1):
    for j in xrange(0, len(primelist)):
        k=numDivisibleBy(i,primelist[j])
        if k > primecount[j]:
            primecount[j]=k

result=1
for i in xrange(0,len(primecount)):
    if primecount[i]>0:
        print result
        result= result*(primelist[i]**primecount[i])
print primecount
print result

#77597520