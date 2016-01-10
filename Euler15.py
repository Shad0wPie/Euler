__author__ = 'adam'

size=20

def numWays(x,y):
    if(x==size+1 and y==size+1):
        return 1
    if(x>size):
        return numWays(x,y+1)
    if(y>size):
        return numWays(x+1,y)
    else:
        return numWays(x,y+1) + numWays(x+1,y)

print numWays(1,1)