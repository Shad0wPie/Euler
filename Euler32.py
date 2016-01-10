__author__ = 'adam'

def isPandigital(n):
    n=str(n)
    if len(n)!=9:
        return False
    for i in '123456789':
        if not i in n:
            return False
    return True

prods= set([])
for a in xrange(1,10000):
    numdigitsa=len(str(a))
    typb=10**((9-2*numdigitsa)/2)
    #print a, typb
    for b in xrange(typb/10,typb*10):
        prod = a*b
        if isPandigital(str(a)+str(b)+str(prod)):
            print a, b, prod
            prods.add(prod)
print sum(prods)

