__author__ = 'adam'

#10 001st prime

def primes (n):
    primelist=[]
    count = 0
    i=2
    while count < n:
        isprime=True;
        for j in primelist:
            if i%j==0:
                isprime=False
                break
        if(isprime):
            primelist.append(i)
            count += 1
        i += 1
    return primelist


print primes(10001)[10000]

#104743