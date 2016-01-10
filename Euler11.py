__author__ = 'adam'

matrix=[]
with  open("Data/Euler11data.txt") as f:
    for line in f:
        row=[]
        for i in str(line).split(' '):
            row.append(int(i.translate(None,'\n')))
        matrix.append(row)

#print matrix
assert(len(matrix[0])==20)
maxprod=0
for i in xrange(0,20):
    for j in xrange(0,20):
        diadown=matrix[i][j]
        diaup=matrix[i][j]
        hor=matrix[i][j]
        ver=matrix[i][j]
        if(i+3>19):
            diadown=0
            ver=0
        if(j+3>19):
            diaup=0
            diadown=0
            hor=0
        if(i-3<0):
            diaup=0
        for k in xrange(1,4):
            if(diadown!=0):
                diadown= diadown * matrix[i+k][j+k]
            if(diaup!=0):
                diaup=diaup*matrix[i-k][j+k]
            if(hor!=0):
                hor=matrix[i][j+k]
            if ver != 0:
                ver=matrix[i+k][j]
        biggest = max(diaup,diadown,hor,ver)
        if(biggest > maxprod):
            maxprod = biggest

print maxprod
