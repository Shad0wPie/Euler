__author__ = 'adam'

class DIR:
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

def spiral(dim):
    mat = [[0]*dim for row in xrange(dim)]
    center = int(dim/2)
    mat[center][center]=1
    num=2
    for i in xrange(1, center+1):
        #go down
        for j in xrange(-i+1,i+1):
            mat[center+j][center+i]=num
            num+=1
        num-=1
        #go left
        for j in xrange(-i,i+1):
            mat[center+i][center-j]=num
            num+=1
        num-=1
        #go up
        for j in xrange(-i,i+1):
            mat[center-j][center-i]=num
            num+=1
        num-=1
        #go right
        if center + i + 1 >= dim:
            for j in xrange(-i,i+1):
                mat[center-i][center+j]=num
                num+=1
        else:
            for j in xrange(-i,i+2):
                mat[center-i][center+j]=num
                num+=1
        num-=1
    return mat

dim=1001
spir=spiral(dim)
sum=-1 #one will be counted twice
for i in xrange(dim):
    #print spir[i]
    sum+= spir[i][i]+ spir[i][dim-1-i]
print sum