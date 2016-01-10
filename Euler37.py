__author__ = 'adam'

import primes

max=10**6
primelist = set(primes.primes(max))

def isTruncable(n):
    if not n in primelist:
        return False
    num1=str(n)
    num2=str(n)
    for i in xrange(1,len(num1)):
        num1=num1[1:]
        #print num1
        if not int(num1) in primelist:
            return False
        num2 = num2[:-1]
        #print num2
        if not int(num2) in primelist:
            return False
    return True

print isTruncable(3797)

count = 0
list=[]
for i in primelist:
    if isTruncable(i):
        print i
        count+=1
        list.append(i)

print list
print sum(list)-17