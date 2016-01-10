__author__ = 'adam'

def fiboGen():
    a=1
    b=1
    yield a
    yield b

    while True:
        c=a+b
        a=b
        b=c
        yield c

counter = 0
for fibo in fiboGen():
    print fibo
    counter+=1
    if len(str(fibo)) == 1000:
        break

print counter


