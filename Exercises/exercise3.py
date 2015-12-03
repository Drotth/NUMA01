# -*- coding: utf-8 -*-
"""
NUMA01 - Exercise 3
Created on Wed Nov 18 09:41:20 2015
@author: Andreas Drotth
"""
from scipy import *
from pylab import *

# TASK 1
print("\nTASK 1 -------------------------------------------------------------")
L = [0, 1, 2, 1, 0, -1, -2, -1, 0]

print(L[0])
print(L[-1])
print(L[:-1])
print(L + L[1:-1] + L)
L[2:2] = [-3]
print(L[2:2])
L[3:4] = []
print(L[3:4])
L[2:5] = [-5]
print(L[2:5])

# TASK 2
print("\nTASK 2 -------------------------------------------------------------")


def f(x):
    return sin(x)

# does this work?
x = 3.
print(f(x))

# and this?
print(f(x))

# what about:
y = 2*pi
print(f(y))

# TASK 3
print("\nTASK 3 -------------------------------------------------------------")


def f(m):
    L = [n-m/2 for n in range(m)]
    return 1 + L[0] + L[-1]


def int_f(m):
    L = [n-m//2 for n in range(m)]
    return 1 + L[0] + L[-1]

print(f(10))
print(int_f(10))

# TASK 4
print("\nTASK 4 -------------------------------------------------------------")
distance = [[0, 20, 30, 40],
            [20, 0, 50, 60],
            [30, 50, 0, 70],
            [40, 60, 70, 0]]
reddistance = []

for row_index, row_elem in enumerate(distance):
    for col_index, col_elem in enumerate(row_elem):
        if (col_elem == 0 and col_index != 0):
            new_list = []
            i = col_index
            while i > 0:
                new_list.append(row_elem[col_index-i])
                i = i - 1
            reddistance.append(new_list)

for n in reddistance:
    print(n)

# TASK 5
print("\nTASK 5 -------------------------------------------------------------")
a = set(['apple', 'pear', 'banana', 'strawberry'])
b = set(['pear', 'banana', 'pineapple'])

# Method that finds the differences between two sets
print(a.symmetric_difference(b))


def symdiff(a, b):
    # Relative complement
    c = a - b
    d = b-a
    print(c, d)

    # Union
    f = c.union(d)
    print("This is the union of the two relative complements:\n", f)

symdiff(a, b)

# TASK 6
print("\nTASK 6 -------------------------------------------------------------")
print(a.intersection(b))
print(a.update(b))
print(a.intersection_update(b))
print(b.intersection(a))
print(b.intersection_update(a))

# TASK 7
print("\nTASK 7 -------------------------------------------------------------")
emptyset = set([])  # The empty set
print(emptyset == emptyset.intersection(emptyset))

# TASK 8
print("\nTASK 8 -------------------------------------------------------------")

# TASK 9
print("\nTASK 9 -------------------------------------------------------------")


"""
# TASK 8 & 9 ------------------------------------------------------------------
def bisec(f, interval, tol):
    midpoint=0
    fininterval=[]
    
       
    midpoint= (interval[0]+interval[1])/2
    
    return midpoint, fininterval    
   
#print(a,b)
    
startinterval =[-0.5, 0.6]
print(bisec(0,startinterval,1e-3))
"""