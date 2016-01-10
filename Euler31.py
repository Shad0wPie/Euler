__author__ = 'adam'


coins=[1,2,5,10,20,50,100,200]

value = 200

def numWays(value,coins):
    coins.sort()
    if len(coins) == 1:
        return 1
    highestcoin = coins[-1]
    ways=0
    for i in xrange(int(value/highestcoin)+1):
        ways+=numWays(value- i*highestcoin,coins[:-1])
    return ways

print numWays(200,coins)