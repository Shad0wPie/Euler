__author__ = 'adam'

abundants = set([])

def sumDivisors(n):
    sum = 1
    for i in xrange(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if (int(n / i) == i):
                sum += i
            else:
                sum += i + n / i
    return sum

for i in xrange(1,28123):
    if sumDivisors(i) > i:
        abundants.add(i)

numbers=[]
for i in xrange(1,28123):
    possible = False
    for x in abundants:
        if x>i:
            break
        if abundants.issuperset(set([i-x])):
            possible=True
            break
    if not possible:
        numbers.append(i)

#print abundants

print sum(numbers)

# 4179871



