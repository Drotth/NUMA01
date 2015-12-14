# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:26:14 2015
@author: Sebastian Olsson & Andreas Drotth
"""
from  scipy import *
from  pylab import *
import matplotlib.pyplot as plt
import scipy.integrate as spi


#klar
print("--------------------------------Task1----------------------")

hh=[]
def ctrapezoidal(f,a,b,n):
    """
    This function implements composite trapezoidal rule
    This rule is used to approximate an integral for a given function
    Parameters are the function, and the interval a and b ([a,b]])
    the last parameter is n which is the discretization points.
    """
    
    x = linspace(a,b, n+1)
    h = x[1] - x[0]
    hh.append(h)
    s = sum(f(x[1:-1])) + 0.5*(f(x[0])+f(x[-1]))
    s = s * h
    return s

#klar
print("--------------------------------Task2----------------------")
ctrapval=[] #contains integral values with different n

def start_ctrapezoidal(npoints,tol,f,a,b):
    """
    For an increasing number of discretization points n in a loop. 
    Stop the loop when the difference of two successive results is less than 
    a given tolerance and return the final approximation.
    """
    for n in range(npoints):
        ctrapval.append(ctrapezoidal(f, a, b, n+1))

    
    for n in range(npoints):
        if abs(ctrapval[n]-ctrapval[n+1])<tol:   
            break
        return ctrapval[-1]


npoints=10000
tol=30
f=lambda x:exp(x)
a=0.0
b=5.0

Ih=start_ctrapezoidal(npoints,tol,f, a, b)
print("Approximated integral value ",Ih)


I=spi.quad(f, a, b)
print("Real integral value ",I[0])

error=abs(I[0]-Ih)
print("Error difference ",error)




print("--------------------------------Task3----------------------")
error=[]
def loglog_plot():
    """
    This function plots the error from abs(Real integral value -Approximated value)
    against the step size h.
    """
    for value in ctrapval:
        error.append((abs(I[0]-value)))
    
    #print(ctrapval)
    #print(hh)
    plt.loglog(hh,error)
    plt.title('loglog diagram')
    plt.xlabel('log10(h)')
    plt.ylabel('log10(error)')
    plt.grid(True, which="both")
    plt.show()

loglog_plot()

print("--------------------------------Task4----------------------")

def sparbanken(K_0,r,n,R):
    """
    Computes the remaining loan after n years assuming that the initial loan was K0 
    and the interest r%.  
    Parameters to the function is initial loan, interest, years and ammortization
    """
    loan_value = []
    if(K_0>=0 and r>=0 and n>=0 and R>=0):
        loan_value.append(K_0)
        for year in range(n):                      
            K_0=(K_0*(r+1))-R*(r+1)
            loan_value.append(round(K_0))
            #print(loan_value)          
        return loan_value   #loan_value[-1]
    
    else:
        print("You most have positiv values")

R = 100
print(sparbanken(1000, 0.03, 12, R))


print("--------------------------------Task5----------------------")
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



print("--------------------------------Task6----------------------")

def ammortization_rate(K_0,r,n):
    """
    This functions determines an ammortization rate such that the
    loan is payed back after exactly n years.
    print("test")
    """

    if r ==0.0:
        R=K_0/n
        return R
        
    else:    
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

years = 2
res = ammortization_rate(1000, 0.01, years)
print("Pay", res, "a year to be debt-free in", years, "years.")



print("--------------------------------Task7----------------------")
def plot_loan(K,n,R_list,r_list):
    """
    This function plots how the loan develops over the year.
    The user can send in different interest (r) and/or ammortizations (R)
    """
    
    x_list=list(range(n+1)) 

    y_list1=sparbanken(K,r_list[0],n,R_list[0])
    plt.plot(x_list,y_list1,label='r={r1} R={R1}'.format(r1=r_list[0],R1=R_list[0])) 

    y_list2=sparbanken(K,r_list[1],n,R_list[1])
    plt.plot(x_list,y_list2,label='r={r2} R={R2}'.format(r2=r_list[1],R2=R_list[1])) 

    y_list3=sparbanken(K,r_list[2],n,R_list[2])
    plt.plot(x_list,y_list3,label='r={r3} R={R3}'.format(r3=r_list[2],R3=R_list[2])) 

    plt.title('How loan develops over the years')
    plt.xlabel('year')
    plt.ylabel('loan')
    plt.grid(True, which="both")
    plt.legend(loc="lower left")
    plt.show()

r_list=[0.03,0.07,0.01]
R_list=[100,200,100]
years=6
K=1000
plot_loan(K,years,R_list,r_list)





print("--------------------------------The end----------------------")