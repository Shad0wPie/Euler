__author__ = 'adam'


def d(n):
    sum = 1
    for i in xrange(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if (int(n / i) == i):
                sum += i
            else:
                sum += i + n / i
    return sum


list = [0, 0]
sum = 0
for x in xrange(2, 10000):
    db = d(x)
    if (x != db and db <= len(list)) and x == list[db]:
        print db, list[db]
        sum += db + list[db]
    list.append(db)

print sum
