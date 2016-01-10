__author__ = 'adam'


#generate triangle numbers
trianums = set([0])
for i in xrange(1000):
    trianums.add(int(0.5*i*(i+1)))

def calcWordVal(word):
    value = 0
    word = str(word)
    for char in word:
        if char.isalpha():
            value+=ord(char)-64
    return value

print calcWordVal('SKY') in trianums

num=0
with open('Data/Euler42data.txt') as f:
    for line in f:
        for word in line.split(','):
            if calcWordVal(word) in trianums:
                num+=1
print num