__author__ = 'adam'


distincts=set([])

for a in xrange(2,101):
    for b in xrange(2,101):
        distincts.add(a**b)

print len(distincts)