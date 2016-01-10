__author__ = 'adam'

def numDivisors(n):
    num=1 #divisible by one
    root=n**0.5
    for i in xrange(2,int(root)):
        if n%i==0:
            num+=2
    if n%int(root)==0:
        num+=1
    return num+1 #divisible by self

numDivisors(36)

number = 1
i=1
while numDivisors(number)<500:
    i+=1
    number+=i

print number