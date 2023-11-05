# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 16:34:04 2023

@author: 17740
"""

def gcd(a, b):  
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def reduce(n, d): 
    if n<0 :
        if d<0:
            return [n/gcd(-n,-d), d/gcd(-n,-d)]
        else:
            return [n/gcd(-n,d), d/gcd(-n,d)]
    else:
        if d<0:
            return [n/gcd(n,-d), d/gcd(n,-d)]
        else:
            return [n/gcd(n,d), d/gcd(n,d)]

class Rational:
    def __init__(self, n=0, d=1):  
        _nu = n; _de = d
        self.__dict__['nu'] = _nu; self.__dict__['de'] = _de

    def __setattr__(self, name, value):
        raise TypeError('Error: Rational objects are immutable')

    def __str__(self): return '%d/%d' % (self.nu, self.de)

    def __add__(self, other): 
        n = self.nu * other.de + self.de * other.nu
        d = self.de * other.de
        c = reduce(n, d)
        return Rational(c[0],c[1])

    def __sub__(self, other):  
        n = self.nu * other.de - self.de * other.nu
        d = self.de * other.de
        c = reduce(n, d)
        return Rational(c[0],c[1])
    
    def __mul__(self, other): 
        n = self.nu * other.nu
        d = self.de * other.de
        c = reduce(n, d)
        return Rational(c[0],c[1])

    def __truediv__(self, other):  
        n = self.nu * other.de
        d = self.de * other.nu
        c = reduce(n, d)
        return Rational(c[0],c[1])

    def __eq__(self, other):  #==
        if self.nu * other.de - self.de * other.nu == 0:
            return True
        else:
            return False

    def __ne__(self, other):  #!=
        if self.nu * other.de - self.de * other.nu == 0:
            return False
        else:
            return True

    def __gt__(self, other):   #>
        a = self.nu * other.de - self.de * other.nu 
        b = self.de * other.de
        if a * b > 0:
            return True
        else:
            return False
            

    def __lt__(self, other):   #<
        a = self.nu * other.de - self.de * other.nu 
        b = self.de * other.de
        if a * b < 0:
            return True
        else:
            return False

    def __ge__(self, other):    #>=
        a = self.nu * other.de - self.de * other.nu 
        b = self.de * other.de
        if a * b >= 0:
            return True
        else:
            return False

    def __le__(self, other):    #<=
        a = self.nu * other.de - self.de * other.nu 
        b = self.de * other.de
        if a * b <= 0:
            return True
        else:
            return False


def test():
    testsuite = [
        ('Rational(2, 3) + Rational(-70, 40)',
          Rational(-13, 12)),
        ('Rational(-20, 3) - Rational(120, 470)',
          Rational(-976,141)),
        ('Rational(-6, 19) * Rational(-114, 18)',
          Rational(2, 1)),
        ('Rational(-6, 19) / Rational(-114, -28)',
          Rational(-28,361)),

        ('Rational(-6, 19) == Rational(-14, 41)', False),
        ('Rational(-6, 19) != Rational(-14, 41)', True),
        ('Rational(6, -19) > Rational(14, -41)', True),
        ('Rational(-6, 19) < Rational(-14, 41)', False),
        ('Rational(-6, 19) >= Rational(-14, 41)', True),
        ('Rational(6, -19) <= Rational(14, -41)', False),
        ('Rational(-15, 8) == Rational(120, -64)', True),
    ]
    for t in testsuite:
        try:
            result = eval(t[0])
        except:
            print('Error in evaluating ' + t[0]); continue

        if result != t[1]:
            print('Error:  %s != %s' % (t[0], t[1]))

if __name__ == '__main__':
    test()
