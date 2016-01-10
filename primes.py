__author__ = 'adam'
import numpy as np
import math

def primes (n):
    primelist=[]
    for i in xrange(2,n):
        isprime=True;
        for j in primelist:
            if j>i**0.5:
                break
            if i%j==0:
                isprime=False
                break
        if(isprime):
            primelist.append(i)
    return primelist

def calculatePrimes(n):
    list = set(range(1,n))
    for i in list:
        newlist = set( )

def numpyPrimes(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]


def isPrime(n):
    if n==1 or n==2:
        return True
    for i in xrange(2,int(n**0.5)):
        if n%i==0:
            return False
    return True


def writePrimesToFile(n,path):
    with  open(path,'w') as f:
        max=10
        for prime in numpyPrimes(n):
            if prime > max:
                f.write(str(prime)+'\n')
                max*=10
            else:
                f.write(str(prime)+' ')

def readPrimes(n):
    with  open('Data/Primes.txt','r') as f:
        max=math.log10(n)-1
        count =0
        list=[]
        for line in f:
            list+=([int(i) for i in line.strip().split(' ')])
            count+=1
            if(count>max):
                break
    return list
