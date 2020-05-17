#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:14:45 2020

@author: deepsikha
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.'''
def multiple(n,m):
    if m==0:
        return(False)
    if n%m==0:
        return True
    
    






'''Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.'''
import math
def even(k:int):
    assert type(k)==int
    
    if math.gcd(k,2)==1:
        return False
    return True






"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n."""
def sumfun(n):
    if n==1:
        return 1
    return n**2+sumfun(n-1)
print(sumfun(4))

'''Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.'''
def sumoddfun(k):
    
    return sum(x*x for x in range (1,k) if x%2==1)
print(sumoddfun(4))