__author__ = 'adam'


pentagonals = set([])
n = 1
diff=9999999999
bestPair=[0,0]
oldPenta=0
newPenta=0
for i in xrange(1,100000000):
    pentagonals.add(int(i * (3 * i - 1) * 0.5))

print 'done'


countingPenta = []

while True:
    oldPenta=newPenta
    newPenta = int(n * (3 * n - 1) * 0.5)
#    print 'newPenta: ' + str(newPenta)
    if newPenta-oldPenta > diff:
        break
    for penta in countingPenta:
#        print penta
        a = newPenta + penta
        b = newPenta - penta
        if a in pentagonals and b in pentagonals and b<diff:
            diff=b
            bestPair=a,b
            print bestPair
            print diff
    n+=1
    countingPenta.append(newPenta)

print bestPair
print diff