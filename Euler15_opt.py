__author__ = 'adam'

size=20
table=[]
for i in xrange(0,22):
    table.append([0]*22)
def numWays(x,y):
    if(x>size or y>size):
        return 1
    tabvalue = table[x][y]
    if tabvalue != 0:
        return tabvalue

    return numWays(x,y+1) + numWays(x+1,y)

def buildTable():
    for i in xrange(1,size+2):
        i=size+2-i
        for j in xrange(1,size+2):
            j=size+2-j
            table[i][j]=numWays(i,j)

buildTable()
for row in table:
    print row