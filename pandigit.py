__author__ = 'adam'
import itertools

def isNinePandigital(n):
    n=str(n)
    if len(n)!=9:
        return False
    for i in '123456789':
        if not i in n:
            return False
    return True

def isNpandigital(n,N):
    n=str(n)
    if len(n)!=N:
        return False
    ref=''
    for i in xrange(1,N+1):
        ref+=str(i)
    for i in ref:
        if not i in n:
            return False
    return True

def isPandigital(n):
    n=str(n)
    N=len(n)
    if N>9:
        return False
    ref=''
    for i in xrange(1,N+1):
        ref+=str(i)
    for i in ref:
        if not i in n:
            return False
    return True

def isXtoYPandigital(n,x,y):
    """returns true if the given number is x to y pandigital (eg. 0 to 9 pandigital)
    """
    n=str(n)
    if len(n)!=y-x+1:
        return False
    ref=''
    for i in xrange(x,y+1):
        ref+=str(i)
    for i in ref:
        if not i in n:
            return False
    return True

def isPatternPandigital(n,pattern):
    n=str(n)
    if len(n) != len(pattern):
        return False
    for char in pattern:
        if not char in n:
            return False
    return True

def findXtoYPandigital(x,y):
    digits = y-x +1
    list = []
    ref=''
    for i in xrange(x,y+1):
        ref+=str(i)
    for i in xrange(10**(digits-1),10**digits):
        if isPatternPandigital(i,ref):
            list.append(i)
    return list