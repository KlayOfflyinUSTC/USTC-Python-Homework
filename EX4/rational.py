# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:34:53 2023

@author: 17740
"""

##EX4_3
"""

Module for performing arithmetic operations for rational numbers. 
To run the module, user needs to supply three named parameters:

1. op stands for the operation:

    add for addition

    sub for subtraction

    mul for multiplication

    div for division

2. x stands for the first operand

3. y stands for the second operand 

x and y must be enclosed in paired parentheses. 

For example: 

>>> run rational.py --op add --x (2/3) --y (-70/40)

-13/12

>>> run rational.py --op sub --x (-20/3) --y (120/470)

-976/141

>>> run rational.py --op mul --x (-6/19) --y (-114/18)

2/1

>>> run rational.py --op div --x (-6/19) --y (-114/-28)

-28/361

""" 

import sys, math 

def test_all_functions(): 
    test_reduce()
    test_add()
    test_mul()
    test_output()
    test_get_rational()

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
        

def test_reduce():
    n=-10
    d=5
    print(reduce(n, d))

def add(x, y): 
    n = x[0] * y[1] + x[1] * y[0]
    d = x[1] * y[1]
    return reduce(n,d)


def test_add():
    x = [1,2]
    y = [1,3]
    print(add(x,y))
    

def sub(x, y): 
    n = x[0] * y[1] - x[1] * y[0]
    d = x[1] * y[1]
    return reduce(n,d)

def mul(x, y):   
    n = x[0] * y[0]
    d = x[1] * y[1]
    return reduce(n,d)

def test_mul():
    x=[4,55]
    y=[11,7]
    print(mul(x,y))

def div(x, y):   
    n = x[0] * y[1]
    d = x[1] * y[0]
    return reduce(n,d)

def output(y): 
    x = []
    for i in y:
        number = int(i)
        x.append(number)
    s = f"{x[0]}/{x[1]}"
    print(s)
    
def test_output():
    x = [-7,11]
    output(x)

def get_rational(s):  
    import re
    x = re.findall('-?\d+', s)
    number_list = []
    for string in x:
        number = float(string)
        number_list.append(number)
    return  number_list 
    
def test_get_rational():
    s = '(-13/5)'
    print(get_rational(s))
    


if __name__ == '__main__':

    if len(sys.argv) == 1:

        print(__doc__)

    elif len(sys.argv) == 2 and sys.argv[1] == '-h':

        print(__doc__)

    elif len(sys.argv) == 2 and sys.argv[1] == 'test':

        test_all_functions()

    else:

        import argparse

        parser = argparse.ArgumentParser()

        parser.add_argument('--op', type=str)

        parser.add_argument('--x', type=str)

        parser.add_argument('--y', type=str)

        args = parser.parse_args()

        op = args.op

        x = get_rational(args.x); y = get_rational(args.y)

        f = {'add':add, 'sub':sub, 'mul':mul, 'div':div}

        output(f[op](x, y))