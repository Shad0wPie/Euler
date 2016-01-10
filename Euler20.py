__author__ = 'adam'

def fack(nr):
    if nr==1:
        return 1
    return nr*fack(nr-1)

product=fack(100)

string=str(product)
sum=0
for i in string:
    sum = sum+int(i)

print(sum)