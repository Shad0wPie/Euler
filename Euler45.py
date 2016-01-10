__author__ = 'adam'

from math import sqrt


def is_pent(x):
    f = (.5 + sqrt(.25 + 6 * x)) / 3
    if f - int(f) == 0:
        return True
    else:
        return False

def is_tria(x):
    f = (-.5 + sqrt(.25 + 2 * x))
    if f - int(f) == 0:
        return True
    else:
        return False


def gen_hexa(n=1):
    if n < 1:
        print "Input must be at least 1!"
        return
    while True:
        yield n * (2 * n - 1)
        n += 1


for i in gen_hexa(144):
    if is_pent(i):
        if is_tria(i):
            print i
            break