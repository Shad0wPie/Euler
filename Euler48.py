__author__ = 'adam'

for i in xrange(1,1000+1):
    sum=0
    for j in xrange(1,i+1):
        sum+=j**j
    print "Self power of: " + str(i) + "is: " + str(sum)