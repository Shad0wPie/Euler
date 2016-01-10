__author__ = 'adam'

low = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8] #0:1:19

tens = [0,0,6,6,5,5,5,7,6,6] # 0:10:90

def numLetters(n):
    number =  str(n)
    l=0
    if len(number) == 3:
       l += low[int(number[0])] + 7
       if(number[1:3]!='00'):
           l+=3
       number = number[1:]
    if int(number) < 20:
        l+= low[int(number)]
    else:
        l+= tens[int(number[0])] + low[int(number[1])]
    return l

sum=0
for i in xrange(1,1000):
    sum+=numLetters(i)
sum+=11
print sum
print numLetters(100)