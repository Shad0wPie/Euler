__author__ = 'adam'


def isPandigital(n):
    n=str(n)
    if len(n)!=9:
        return False
    for i in '123456789':
        if not i in n:
            return False
    return True


list=[]
for i in xrange(1,10000):
    conc=''
    n=1
    while len(conc)<9:
        conc+=str(i*n)
        n+=1
    if isPandigital(conc):
        list.append(conc)
print(list)
print max(list)