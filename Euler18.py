__author__ = 'adam'

matrix=[]
with  open("Data/Euler18data.txt") as f:
    for line in f:
        row=[]
        for i in str(line).split(' '):
            row.append(int(i.translate(None,'\n')))
        matrix.append(row)

print matrix

for i in reversed(xrange(len(matrix)-1)):
    for j in xrange(len(matrix[i])):
        matrix[i][j] += max(matrix[i+1][j], matrix[i+1][j+1])

print matrix