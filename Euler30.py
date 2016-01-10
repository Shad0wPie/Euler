__author__ = 'adam'

list=[]
n=1
while n*(9**5) > 10**n:
    n+=1
print n

print 9**5
for i in xrange(2,1000000):
    powersum=0
    for char in str(i):
        powersum+=int(char)**5
    if powersum==i:
       list.append(i)

print list
print sum(list)