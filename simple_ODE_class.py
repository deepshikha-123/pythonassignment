#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 00:13:57 2020

@author: deepsikha
"""

'''Exercise 1: Solve a simple ODE with class-based code.

This exercise aims to solve the ODE problem u−10u′=0, u(0)=0.2, for t∈[0,20]. '''

''' a) Identify the mathematical function f(u,t) in the generic ODE form u′=f(u,t).
    b) Implement the f(u,t) function in a Python function. 
    c) Use the ForwardEuler_v1 class from the section class implementation to compute a numerical solution of the ODE problem. Use a time step Δt=5.
    d) Plot the numerical solution and the exact solution u(t)=0.2exp(0.1)t.
    e) Save the numerical solution to file. Decide upon a suitable file format. 
    f) Perform simulations for smaller Δt  values and demonstrate visually that the numerical solution approaches the exact solution. 
 Filename: simple_ODE_class. '''
from matplotlib.pyplot import plot

from ForwardEulerclass import ForwardEuler_v1 as Fp

import numpy as np
def f(u,t):
    return u/10
a =Fp(f, U0=0.2, T=20, n=4)
u,t=a.solve()
b=a.advance()
print(u)
plot(t,u)
#plot the exact vsolution.
u =0.2*np.exp(0.1*t)
plot(t,u)
#perform simulation for smaller value of dt i.e. greater value of n
a =Fp(f, U0=0.2, T=20, n=20)
u,t=a.solve()
b=a.advance()
print(u)
plot(t,u)
