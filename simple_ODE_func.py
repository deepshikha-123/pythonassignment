#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:27:02 2020

@author: deepsikha
"""


'''Exercise 1: Solve a simple ODE with function-based code.

This exercise aims to solve the ODE problem u−10u′=0, u(0)=0.2, for t∈[0,20]. '''

''' a) Identify the mathematical function f(u,t) in the generic ODE form u′=f(u,t).
    b) Implement the f(u,t) function in a Python function. 
    c) Use the ForwardEuler function from the section Function implementation to compute a numerical solution of the ODE problem. Use a time step Δt=5.
    d) Plot the numerical solution and the exact solution u(t)=0.2exp(0.1)t.
    e) Save the numerical solution to file. Decide upon a suitable file format. 
    f) Perform simulations for smaller Δt  values and demonstrate visually that the numerical solution approaches the exact solution. 
 Filename: simple_ODE_func. '''
import numpy as np 

import ForwardEuler as FP
from matplotlib.pyplot import plot
def f(u,t):
    return u/10

u,t=FP.ForwardEuler(f, U0=0.2, T=20, n=100)


plot(t,u)
'''plot the exact solution.'''


# setting the x - coordinates 
t = np.arange(0, 20, 0.2) 
# setting the corresponding y - coordinates y

u = np.exp(0.1*t) 

# potting the points 
plot(t, u) 

# function to show the plot 

