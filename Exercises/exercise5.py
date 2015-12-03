# -*- coding: utf-8 -*-
"""
NUMA01 - Exercise 5
Created on Wed Nov 18 16:17:59 2015
@author: Andreas Drotth
"""
from scipy import *
from scipy.integrate import quad
from pylab import *

# TASK 1
print("\nTASK 1 -------------------------------------------------------------")


def f(x): return sin(2*pi*x)
a = 0
b = pi/2

print(quad(f, a, b))

# TASK 2
print("\nTASK 2 -------------------------------------------------------------")


def f(x):
    # w = 2*pi
    w = range(0, 2*pi, 1000)
    return sin(w*x)

a = 0
b = pi/2

plot(quad(f, a, b))
show()

# TASK 3
print("\nTASK 3 -------------------------------------------------------------")

# TASK 4
print("\nTASK 4 -------------------------------------------------------------")
