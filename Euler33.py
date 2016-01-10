__author__ = 'adam'
import fractions as f

def reduce (numerator, denominator):
    num= str(numerator)
    den = str(denominator)
    for char in num:
        if char in den:
            num=num.replace(char,'',1)
            den = den.replace(char,'',1)
  #  print num, numerator, den, denominator
    return num, den
prodnum=1
prodden=1
for i in xrange(10,100):
    for j in xrange(i,100):
        if (not i == j) and not (i%10 ==0 and j%10==0):
            num,den = reduce(i,j)
            if (len(num)>0 and len(den)>0) and (not int(num) == i) and (not int(den)==0):
                if f.Fraction(i,j) == f.Fraction(int(num),int(den)):
                    print num , den , i , j
                    prodnum *= int(num)
                    prodden *= int(den)

print f.Fraction(prodnum,prodden)