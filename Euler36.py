__author__ = 'adam'

from numpy import binary_repr

def isPali(n):
    nstring = str(n)
    length=len(nstring)
    if nstring[0] == '0':
        return False
    for i in xrange(0,length):
        if nstring[i]!=nstring[length-1-i]:
            return False
    return True

list=[]
for i in xrange(1,10**6):
    if isPali(str(i)) and isPali(binary_repr(i)):
        list.append(i)
print list
print sum(list)
