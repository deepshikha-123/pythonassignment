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
    """
    This function will discribe whether two numbers are multiple of each other or not.

    Parameters
    ----------
    n : any real number entered by you.
    m : any real number entered by you.

    Returns
    either True, False or undefined

    
    TYPE
        This is a user defined function named multiple(n,m).

    """

    if m==0:
        return 'undefined'
    if n%m==0:
        return True
    else: return False
    
    





'''Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.'''
import math
def even(k:int):
    """
    This function will report the information that the number you input is even or not.

    Parameters
    ----------
    k : int
        Number should be integer.

    Returns
    -------
    bool
        Function name is even(k).

    """
    assert type(k)==int
    
    if math.gcd(k,2)==1:
        return False
    return True






"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n."""
def sumfun(n):
    """
    This function will return the sum of the squres of all positive integers smaller than that number you entered.

    Parameters
    ----------
    n : any positive integer.
        

    Returns
    A positive integer
    TYPE
    function name: sumfun(n)
        .

    """
    if n==1:
        return 1
    return n**2+sumfun(n-1)

'''Give a single command that computes the sum from above question, rely-
ing on Python’s comprehension syntax and the built-in sum function.''' 



def sumfun1(k):
    """
    This will give the sum of square of all positive integer less than the number you entered.
    

    Parameters
    ----------
    k : A positive integer.
        

    Returns
    A positive number.
    TYPE
    Function defined in single line with the help of built-in sum function.

    """
    return sum(n*n for n in range (1,k))




'''Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.'''
def sumoddfun(k):
    """
    This function will return the sum of the squares of all the odd positive integers
    smaller than the number you entered.

    Parameters
    ----------
    k : any positive integer.
        

    Returns
    A positive integer
    TYPE
        single input user defined function named sumoddfun(k).

    """
    
    
    if k==1:
        return 1
    if k%2==1:
        
        return k**2+sumfun((k-2)**2)
    else: return (k-1)**2+sumfun((k-3)**2)
'''Give a single command that computes the sum from above question, rely-
ing on Python’s comprehension syntax and the built-in sum function.'''    


def sumoddfun1(k):
    """
    This will return the sum of squares of all positive odd numbers less than that number you entered.
    

    Parameters
    ----------
    k : any positive integer.

    Returns
    positive integer value
    TYPE
        function defined in a single line with the help of built-in sum function.

    """
    return sum(n*n for n in range (1,k) if k%2==1)



'''What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?'''
a=list(range(50,90,10))

'''What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?'''

b=list(range(-8,10,2))

'''Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].'''


print([2**n for n in range(0,9)])


            







