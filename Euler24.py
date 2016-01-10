__author__ = 'adam'
import copy

origNums = list(xrange(3))
availableNums = origNums[:]


def permutationGenerator(s):
    s=str(s)
    if len(s)==1:
        yield s
    else:
        for i in xrange(len(s)):
            newstring = s[0:i] + s[i+1:len(s)]
#            print str(i) + " and  " + newstring
            for permutation in permutationGenerator(newstring):
                yield s[i] + permutation

count = 0
for permutation in permutationGenerator("0123456789"):
    count+=1
    if count == 1000000:
        print "This was the shit! permutation is: " + permutation
        break