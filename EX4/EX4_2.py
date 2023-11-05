# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:03:58 2023

@author: jjh
"""

##EX4_2
d = {}
def F(n):
    global d
    d[n] = d.pop(n,0) + 1
    if n <= 1:
        return 1
    return F(n-1) + F(n-2) 

F(10)
print(d)