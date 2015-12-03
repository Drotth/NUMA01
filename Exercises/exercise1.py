# -*- coding: utf-8 -*-
"""
NUMA01 - Exercise 1
Created on Mon Nov  2 10:20:25 2015
@author: Andreas Drotth
"""
from scipy import *
from pylab import *

# TASK 1
print("\nTASK 1 -------------------------------------------------------------")
print(sys.version)

# TASK 2
print("\nTASK 2 -------------------------------------------------------------")
x = 2.3
print(x**2+0.25-5)

# TASK 3
print("\nTASK 3 -------------------------------------------------------------")
L = [1, 2]
L3 = 3*L
print("L3[0]: ", L3[0], "\nL3[-1]: ", L3[-1], "\nL3[10]: error if uncommented")

# TASK 4
print("\nTASK 4 -------------------------------------------------------------")
L4 = [k**2 for k in L3]
print("L4: ", L4)

# TASK 5
print("\nTASK 5 -------------------------------------------------------------")
L5 = L3 + L4
print("L5: ", L5)

# TASK 6
print("\nTASK 6 -------------------------------------------------------------")
S = [x/100 for x in range(100)]
print(S)

# TASK 7
print("\nTASK 7 -------------------------------------------------------------")
s = 0
for i in range(0, 500):
    s = s + i
print(s)

ss = [0]
for i in range(1, 500):
    ss.append(ss[i-1] + i)
print("i: ", i)

# TASK 8
print("\nTASK 8 -------------------------------------------------------------")
x_plot = [0]
for i in range(1, 100):
    x_plot.append(i/100)
print(x_plot)

# TASK 9
print("\nTASK 9 -------------------------------------------------------------")
y_plot = [0]
for i in range(1, 100):
    y_plot.append(arctan(x_plot[i]))
print(y_plot)

# TASK 10
print("\nTASK 10 ------------------------------------------------------------")
plot(x_plot, y_plot, "+")
title("x vs arctan(x)")
xlabel("x")
ylabel("arctan(x)")
show()

# TASK 11
print("\nTASK 11 ------------------------------------------------------------")
L11 = [0]
for i in range(1, 200):
    L11.append(1/sqrt(i))
print(L11)

# TASK 12
print("\nTASK 12 ------------------------------------------------------------")
h = 1/1000
a = -0.5
e0 = exp(0)
eha = exp(h*a)
e2ha = exp(2*h*a)
U = [e0, eha, e2ha]

for i in range(3, 1000):
    U.append(U[i-1]+h*a*(((23/12)*U[i-1])-((4/3)*U[i-2])+((5/12)*U[i-3])))
print(U)
