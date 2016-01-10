__author__ = 'adam'

#a2+b2=c2

#a+b+c=1000

#a+b >c
#a+b>500

for i in xrange(1,501):
    for j in xrange(501-i,1001-i):
        k=1000-i-j
        if i**2+j**2==k**2:
            print i
            print j
            print k
            print i*j*k

# 200,375,425
# 31875000

