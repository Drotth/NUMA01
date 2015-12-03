# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:26:14 2015
@author: Sebastian Olsson & Andreas Drotth
"""

from scipy import *
from pylab import *
import matplotlib.pyplot as plt
import scipy.integrate as spi


print("--------------------------------Task1---------------------------------")

hh = []
ee = []
ff = []  # Contains integral values with different n


def ctrapezoidal(f, a, b, n):
    """
    This function implements composite trapezoidal rule
    This rule is used to approximate an integral for a given function
    Parameters are the function, and the interval a and b ([a,b]])
    the last parameter is n which is the discretization points.
    """

    h = (b - a) / n
    hh.append(10*h**2)
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2 * f(a + i * h)
    return s * h / 2

print("--------------------------------Task2---------------------------------")


def start_ctrapezoidal(N_points, TOL):
    """
    For an increasing number of discretization points n in a loop.
    Stop the loop when the difference of two successive results is less than
    a given tolerance and return the final approximation.
    """

    for n in range(1, N_points):
        ff.append(ctrapezoidal(lambda x: exp(x), 0.0, 5.0, n))

    for n in range(N_points):
        if abs(ff[n] - ff[n+1]) < TOL:
            break
        return ff[-1]

print("Approximated integral value", start_ctrapezoidal(1000, 30))
Ih = start_ctrapezoidal(1000, 30)

I = spi.quad(lambda x: exp(x), 0.0, 5.0)
print("Real integral value", I[0])

error = abs(I[0]-Ih)
print("Error difference", error)

print("--------------------------------Task3---------------------------------")


def loglog_plot():
    """
    This function plots the error from abs(Real integral value
    - Approximated value) against the step size h.
    """

    for eVal in ff:
        ee.append(abs(I[0]-eVal))

    plt.loglog(hh, ee)

    plt.title('loglog diagram')
    plt.xlabel('log10(h)')
    plt.ylabel('log10(error)')
    plt.grid(True, which="both")
    plt.show()

loglog_plot()

print("--------------------------------Task4---------------------------------")


def sparbanken(K_0, r, n, R):
    """
    Computes the remaining loan after n years assuming that the initial loan
    was K0 and the interest r%. Parameters to the function is initial loan,
    interest, years and ammortization.
    """

    loan_value = []
    if(K_0 >= 0 and r >= 0 and n >= 0 and R > 0):
        loan_value.append(K_0)
        for year in range(n):
            K_0 = (K_0 * (r+1)) - R * (r+1)
            loan_value.append(round(K_0))
        return loan_value

    else:
        print("You most have positiv values")

R = 100
print(sparbanken(1000, 0.03, 12, R))

print("--------------------------------Task5---------------------------------")


def check_year_fully_paid(K_0, r, R):
    """
    This function determines which the first year when the loan is
    fully payed back.
    """

    years = 0
    paid = -1
    while (paid < 0):
        years = years + 1
        k = sparbanken(K_0, r, years, R)
        if(k[years] <= 0):
            paid = 1
            return years

print("Loan fully paid after:", check_year_fully_paid(1000, .03, R), "years.")

print("--------------------------------Task6---------------------------------")


def ammortization_rate(K_0, r, n):
    """
    This functions determines an ammortization rate such that the
    loan is payed back after exactly n years.
    print("test")
    """

    R_values = 0
    R = K_0 * (r/(1-(1+r) ** -n))
    i = 0

    while (K_0 > 0):
        i = i + 1    # current number of years passed
        H = K_0 * r  # yearly interest
        C = R - H    # yearly payment minus yearly interest
        K_0 = K_0 - C  # new balance
        R_values += C
    return (R_values/i)

years = 12
res = ammortization_rate(1000, .03, years)
print("Pay", res, "a year to be debt-free in", years, "years.")

print("--------------------------------Task7---------------------------------")


def plot_loan(K, n, R_list, r_list):
    """
    This function plots how the loan develops over the year.
    The user can send in different interest (r) and/or ammortizations (R)
    """

    x_list = list(range(n+1))

    y_list1 = sparbanken(K, r_list[0], n, R)
    plt.plot(x_list, y_list1, label='r={r1} R={R1}'
             .format(r1=r_list[0], R1=R_list[0]))

    y_list2 = sparbanken(K, r_list[1], n, R)
    plt.plot(x_list, y_list2, label='r={r2} R={R2}'
             .format(r2=r_list[1], R2=R_list[1]))

    y_list3 = sparbanken(K, r_list[2], n, R)
    plt.plot(x_list, y_list3, label='r={r3} R={R3}'
             .format(r3=r_list[2], R3=R_list[2]))

    plt.title('loan develops over the years')
    plt.xlabel('year')
    plt.ylabel('loan')
    plt.grid(True, which="both")
    plt.legend()
    plt.show()

r_list = [0.03, 0.07, 0.11]
R_list = [200, 200, 200]
years = 6
K = 1200
plot_loan(K, years, R_list, r_list)
