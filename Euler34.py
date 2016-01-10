__author__ = 'adam'
import math

n=0
ninefac=math.factorial(9)
while (n+1)*ninefac>10**n:
    n+=1
print(n)

factorials=[]
for i in range(10):
    factorials.append(math.factorial(i))


def isFactorial(n):
    num=str(n)
    sum=0
    for i in num:
        sum+=factorials[int(i)]
    return n==sum

list=[]
for i in range(10**n):
    if isFactorial(i):
        list.append(i)
        print(i)
print(sum(list))