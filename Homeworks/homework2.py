# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 22:37:48 2015
@author: Sebastian Olsson and Andreas Drotth
"""

from scipy import *
from pylab import *
import operator


class Interval(object):
    def __init__(self, leftendpoint, rightendpoint=None):
        """
        Init (initialize) function is the first function called when an object
        is created.
        Self represent the instance of the object itself
        """

        self.leftendpoint = leftendpoint
        if rightendpoint is not None:
            self.rightendpoint = rightendpoint
        else:
            self.rightendpoint = leftendpoint
        start = [self.leftendpoint, self.rightendpoint]
        print(start)

    def __add__(self,other):
        """
        This function is used fot addition on two intervals
        """
        add=[] 
        if not isinstance(other, Interval):
            p1, q1 = self.leftendpoint,self.rightendpoint
            add.append(p1+other)
            add.append(q1+other)                 
        else:
            p1, q1 = self.leftendpoint,self.rightendpoint
            p2, q2 = other.leftendpoint,other.rightendpoint
            add.append(p1+p2)
            add.append(q1+q2)
        return add      
                
    def __radd__(self, other):
        """
        Reverses the role of self and other
        """
        return self + other
         
    def __sub__(self, other):
        """
        This function is used for subtraction on two intervals
        """

        sub = []
        p1, q1 = self.leftendpoint, self.rightendpoint
        p2, q2 = other.leftendpoint, other.rightendpoint
        sub.append(p1-q2)
        sub.append(q1-p2)
        return sub

    def __mul__(self, other):
        """
        This function is used for multiplication on two intervals
        """

        mult = []
        p1, q1 = self.leftendpoint, self.rightendpoint
        p2, q2 = other.leftendpoint, other.rightendpoint
        ac = p1*p2
        ad = p1*q2
        bc = p2*q1
        bd = q1*q2
        mult.append(min(ac, ad, bc, bd))
        mult.append(max(ac, ad, bc, bd))
        return mult

    def __truediv__(self, other):
        """
        This function is used for division on two intervals
        """

        div = []
        p1, q1 = self.leftendpoint, self.rightendpoint
        p2, q2 = other.leftendpoint, other.rightendpoint
        if (p2 == 0 or q2 == 0):
            raise ZeroDivisionError("You tried to divide by zero!")
        ac = operator.__truediv__(p1, p2)
        ad = operator.__truediv__(p1, q2)
        bc = operator.__truediv__(q1, p2)
        bd = operator.__truediv__(q1, q2)
        div.append(min(ac, ad, bc, bd))
        div.append(max(ac, ad, bc, bd))
        return div

    def __pow__(self, other):
        """
        This function is used for the power of
        """

        powe = []
        if other % 2 == 0 and other > 0:  # even
            if self.leftendpoint >= 0:
                powe.append(self.rightendpoint**other)
                powe.append(self.leftendpoint**other)
            elif self.rightendpoint < 0:
                powe.append(self.rightendpoint**other)
                powe.append(self.leftendpoint**other)
            else:
                powe.append(0)
                powe.append(max(self.leftendpoint**other,
                                self.rightendpoint**other))
        else:
            powe.append(self.leftendpoint**other)
            powe.append(self.rightendpoint**other)

        return powe

    def __contains__(self):
        if not isinstance(
             self.leftendpoint, int) or isinstance(self.leftendpoint, float):
            raise TypeError('Left endpoint is not real value')
        if not isinstance(
             self.rightendpoint, int) or isinstance(self.rightendpoint, float):
            raise TypeError('Right endppoint is not real balue')

    def plot_values():
        """
        Evaluate the polynomial p(x)=3x^3−2x^2+5x−1
        Plots lower boundaries and upper boundaries for y with respect to
        lower boundaries of x
        """

        yl = []
        yu = []
        xl = linspace(0., 1, 1000)
        xu = linspace(0., 1, 1000) + 0.5
        p = [3, -2, 5, -1]
        yl = np.polyval(p, xl)
        yu = np.polyval(p, xu)
        plot(xl, yl, label='yl')
        plot(xl, yu, label='yu')
        xlabel('xl')
        ylabel('y')
        title("Graph")
        legend()
        show()

if __name__ == '__main__':
    print("-----------------------------TASK 3-------------------------------")
    I1 = Interval(1, 2)  # [1, 2]
    I2 = Interval(3, 4)  # [3, 4]

    print("-----------------------------TASK 4-------------------------------")
    I3 = I1 + I2  # [4, 6]
    print("I1 + I2 =", I3)
    I4 = I1 - I2  # [-3, -1]
    print("I1 - I2 =", I4)
    I5 = I1 * I2  # [3, 8]
    print("I1 * I2 =", I5)
    I6 = I1 / I2  # [0.25,0.6666666666666666]
    print("I1 / I2 =", I6)

    print("-----------------------------TASK 5-------------------------------")
    Ivalid = Interval(4, 1)
    Izero = Interval(3, 2)  # Change anyone to 0 for test!
    Iresult = Ivalid / Izero
    print("Iresult =", Iresult)

    print("-----------------------------TASK 6-------------------------------")
    Isingle1 = Interval(1)
    Isingle2 = Interval(2)

    print("-----------------------------TASK 7-------------------------------")
    
    print(Interval(2,3) + 1) # [3, 4]
    
    print(1 + Interval(2,3)) # [3, 4]
    print(1.0 + Interval(2,3)) # [3.0, 4.0]
    

    print("-----------------------------TASK 9-------------------------------")
    x = Interval(-2, 2)  # [-2, 2]
    print(x**2)  # [0, 4]
    print(x**3)  # [-8, 8]

    """
    I9 = Interval(1j,3)
    I9.__contains__()
    """

    Interval.plot_values()
