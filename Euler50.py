__author__ = 'adam'

from primes import numpyPrimes
import copy

primelist = numpyPrimes(10 ** 6)
primeset = set(primelist)
primeSumNum = {}


target = 10**6
components = []
bestComponents=[]
for i, prime in enumerate(primelist):
    if sum(components) in primeset:
        if len(components) > len(bestComponents):
            bestComponents=copy.copy(components)
    if sum(components) < target:
        components.append(prime)
        testcomponents=copy.copy(components)
        while len(testcomponents)>len(bestComponents):
            if sum(testcomponents) in primeset:
                bestComponents=copy.copy(testcomponents)
                break
            else:
                testcomponents=testcomponents[1:]
        #check decreasing shit until length of bestcomponents
    else:
        if len(components) < len(bestComponents):
            break
        while sum(components) > target:
            components=components[1:]

print sum(bestComponents)
print components



'''
num = 0
for i, prime in enumerate(primelist):
    components = []
    for smallprime in primelist[:i]:
        if sum(components) == prime:
            primeSumNum[prime]=len(components)
            break
        components.append(smallprime)
        while sum(components) > prime:
            components=components[1:]
    if sum(components) == prime:
        primeSumNum[prime]=len(components)

bestPrime = max(primeSumNum.iterkeys(), key = lambda k: primeSumNum[k])
print str(bestPrime) + ". Number of consecutives: " + str(primeSumNum[bestPrime])
'''
