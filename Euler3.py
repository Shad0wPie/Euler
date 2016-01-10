__author__ = 'adam'

import primes

num=600851475143
sqrtnum = int(num**0.5)

primelist = primes.primes(sqrtnum)

biggestprime=0
for i in primelist:
    if num%i==0:
        biggestprime=i


print biggestprime


