__author__ = 'adam'


def step(n):
    if(n==1):
        return 1
    if n%2 == 0:
        return step(int(n*0.5))+1
    else:
        return step(3*n+1)+1

mostSteps=0
startingnumber=0
for i in xrange(1,1000000):
    steps = step(i)
    if steps>mostSteps:
        mostSteps=steps
        startingnumber=i

print startingnumber
print mostSteps
