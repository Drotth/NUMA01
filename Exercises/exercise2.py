# -*- coding: utf-8 -*-
"""
NUMA01 - Exercise 2
Created on Wed Nov 18 08:57:19 2015
@author: Andreas Drotth
"""
from scipy import *
from pylab import *

# TASK 1
print("\nTASK 1 -------------------------------------------------------------")
x = 0.5
a = 0.5
# a=8
ss = []
for i in range(200):
    x = sin(x)-a*x+30
    ss.append(x)
    if abs(ss[i] - ss[i - 1]) < 1.e-8 and abs(ss[i] - ss[i-1]) != 0.0:
        print("Iteration was terminated!")
        break
else:
    print("Iteration was not terminated!")

print("The result after {num} iterations is {res}".format(num=i, res=x))

# TASK 2
print("\nTASK 2 -------------------------------------------------------------")
x_vals = [n for n in range(5, 30)]
y1 = [sin(x)-a*x+30 for x in x_vals]
y2 = [x for x in x_vals]
plot(x_vals, y1, label="sin(x)-a*x+30")
plot(x_vals, y2, label="y=x")
title("Graph")
legend()
show()

# TASK 3
print("\nTASK 3 -------------------------------------------------------------")
nn = []
for n in range(500):
    x = pow(sin(n), 2)/n
    nn.append(x)
    if x < 1.e-9:
        print("Found threshold!")
        print(len(nn))
        break
else:
    print("Did not find threshold!")

# TASK 4
print("\nTASK 4 -------------------------------------------------------------")
xx = []
a = [-0.5, 0.5, -0.25, 0.25]
x = 1
xx.append(x)
neg_flag = 0

for n in a:
    print("\nALPHA VARIABLE IS: {res}".format(res=n))
    for m in range(10):
        x = (0.2*x) - (n*(pow(x, 2)-5))
        xx.append(x)
        if x < 0 and neg_flag != 1:
            neg_flag = 1

    if abs(xx[-1] - xx[-2]) < 1.e-9:
        print("Sequence converged to x = {res}".format(res=x))
    else:
        print("No convergence detected.")
    if(neg_flag):
        print("Negative elements found!")

    xx = []
    neg_flag = 0

# TASK 5
print("\nTASK 5 -------------------------------------------------------------")
xx_neg = []
xx_pos = []
a = 0.5
x = 1
xx_pos.append(x)

for m in range(9):
    x = (0.2*x) - (0.5*(pow(x, 2)-5))
    if (x > 0):
        xx_pos.append(x)
    else:
        xx_neg.append(x)

print(xx_pos)
print("\n {vals}".format(vals=xx_neg))

# TASK 6
print("\nTASK 6 -------------------------------------------------------------")


def convergence_t6(a):
    xx = []
    x = 1
    xx.append(x)

    print("\nAlpha variable is: {res}".format(res=a))
    for m in range(29):
        x = (0.2*x)-(a*(pow(x, 2)-5))
        xx.append(x)
        if abs(xx[-1] - xx[-2]) < 1.e-9:
            return True
    return False

a = [-0.5, 0.5, -0.25, 0.25]
print("Converged within 30 iterations: {res}"
      .format(res=convergence_t6(-0.5)))
print("Converged within 30 iterations: {res}"
      .format(res=convergence_t6(0.5)))
print("Converged within 30 iterations: {res}"
      .format(res=convergence_t6(-0.25)))
print("Converged within 30 iterations: {res}"
      .format(res=convergence_t6(0.25)))

# TOO LARGE VARIABLE
# print("Converged within 30 iterations: {res}".format(res=convergence1(1)))

# TASK 7
print("\nTASK 7 -------------------------------------------------------------")


def convergence_t7(a, x0):
    xx = []
    x = x0
    xx.append(x)
    print("\n(Alpha / x0): {alpha} / {x0}".format(alpha=a, x0=x0))
    for m in range(29):
        x = (0.2*x) - (a*(pow(x, 2)-5))
        xx.append(x)
        if abs(xx[-1] - xx[-2]) < 1.e-9:
            return True
    return False

print("Converged within 30 iterations: {res}"
      .format(res=convergence_t7(0.5, 1)))
print("Converged within 30 iterations: {res}"
      .format(res=convergence_t7(0.5, 2)))
print("Converged within 30 iterations: {res}"
      .format(res=convergence_t7(0.5, 3)))
print("Converged within 30 iterations: {res}"
      .format(res=convergence_t7(0.5, 0)))

# TASK 8
print("\nTASK 8 -------------------------------------------------------------")


def convergence_t8(a, x0):
    xx = []
    xx_neg = []
    xx_pos = []
    x = x0
    xx.append(x)

    if (x < 0):
        xx_neg.append(x)
    else:
        xx_pos.append(x)

    print("\n(Alpha / x0): {alpha} / {x0}".format(alpha=a, x0=x0))
    for m in range(29):
        x = (0.2*x) - (a*(pow(x, 2) - 5))
        xx.append(x)
        if (x < 0):
            xx_neg.append(x)
        else:
            xx_pos.append(x)
        if abs(xx[-1] - xx[-2]) < 1.e-9:
            dict = {'pos': xx_pos, 'neg': xx_neg, 'convergent': True}
            return dict

    dict = {'pos': xx_pos, 'neg': xx_neg, 'convergent': False}
    return dict


def print_dict(a):
    print("\nConverged within 30 iterations: {res}"
          .format(res=a['convergent']))
    print("\nPositive values: {res}".format(res=a['pos']))
    print("\nNegative values: {res}".format(res=a['neg']))

print_dict(convergence_t8(-0.5, 1))
print_dict(convergence_t8(0.5, 1))
print_dict(convergence_t8(-0.25, 1))
print_dict(convergence_t8(0.25, 1))
