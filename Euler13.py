__author__ = 'adam'
numbers=[]
with  open("Data/Euler13data.txt") as f:
    for line in f:
        numbers.append(int(line.translate(None,'\n')))

sum=0
for number in numbers:
    sum+=number

print (str(sum)[0:10])