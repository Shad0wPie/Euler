__author__ = 'adam'

i=1
j=2
k=i+j
sum=j

while k <= 4000000:
    print k
    if(k%2==0):
        sum+=k
    i=j
    j=k
    k=i+j
print sum