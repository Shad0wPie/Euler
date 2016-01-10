__author__ = 'adam'

words=[]
with  open("Data/Euler22data.txt") as f:
    for line in f:
        for i in str(line).split(','):
            words.append(i.translate(None,'"'))

print words

words.sort()
print words

sum=0
for i,word in enumerate(words):
    score=0
    for letter in word:
        score+=ord(letter)-64
    score *= i+1
    sum+=score
print sum