# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 20:48:22 2023

@author: jjh
"""
##EX4.1
def is_sorted(s):##判断列表s是否已经排好序
    for i in range(0,len(s)-1):
        if s[i] > s[i+1]:
            return False; break
    return True

def qsort(s):
    if len(s) <= 1: return s
    s_less = [] ; s_greater = [] ; s_equal = []
    for k in s:
        if k < s[0]:
            s_less.append(k)
        elif k > s[0]:
            s_greater.append(k)
        else:
            s_equal.append(k)
    return qsort(s_less) + s_equal + qsort(s_greater)

def binary_search(s, low, high, k):
    if high < low:
        return -1
    else: 
        mid = (high + low)//2
        if s[mid] > k:
            return binary_search(s, low, mid-1, k)
        elif s[mid] < k:
            return binary_search(s, mid+1, high, k)
        else :
            return mid

        
s = [5, 6, 21, 32, 51, 60, 67, 73, 77, 99]
if not is_sorted(s):

    s = qsort(s)

    print(s) 

print(binary_search(s, 0, len(s) - 1, 5)) 

print(binary_search(s, 0, len(s) - 1, 31))

print(binary_search(s, 0, len(s) - 1, 99))

print(binary_search(s, 0, len(s) - 1, 64))

print(binary_search(s, 0, len(s) - 1, 51))