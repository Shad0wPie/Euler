__author__ = 'adam'

bignum=''
for i in xrange(1000):
    bignum+=str(i)
print bignum[0]+'.'+bignum[1:]

print bignum[11]
print bignum[12]

i=1000

while len(bignum)<10**6+1:
    bignum+=str(i)
    i+=1
prod=1
for i in xrange(7):
    print i
    prod *= int(bignum[10**i])
print prod