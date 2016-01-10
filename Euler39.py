__author__ = 'adam'

import collections
import math

triangle = collections.namedtuple('Triangle',['a', 'b', 'c'])

list = []
for a in xrange(200,500):
    for b in xrange(1,a):
        c=math.sqrt(a**2 + b**2)
        if c.is_integer():
            list.append(triangle(a,b,int(c)))
print list
dict = {}
for tri in list:
    perim = tri.a + tri.b + tri.c
    if perim>1000:
        continue
    if dict.has_key(perim):
        dict[perim] += 1
    else:
        dict[perim]=1
print dict
print max(dict.iterkeys(), key=(lambda key: dict[key]))