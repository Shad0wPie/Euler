__author__ = 'adam'
import collections
from decimal import *

getcontext().prec=10000

repdec = collections.namedtuple('RepDec', ['dec','num'])

def CalcDec(n):
    num = str(Decimal(1)/Decimal(n))
    num=num[2:]
    for i in xrange(len(num)):
        for j in xrange(i+1):
            if num[j:i+1]*4 in num[i+1:5*i+2-j]:
                #print '0.' + num[0:j] + '(' + num[j:i+1] + ')'
                return repdec('0.' + num[0:j] + '(' + num[j:i+1] + ')', len(num[j:i+1]))

    return repdec('0.'+num, 0)

list= [0,]

for i in xrange(577,1000):
    list.append(CalcDec(i).num)

print 'done!: '
print max(list)
print list.index(max(list))
print list[7]
print list[47]