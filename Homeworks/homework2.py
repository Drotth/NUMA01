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
        is created. This is also called constructor.
        Self represent the instance of the object itself
        """

        if rightendpoint is None:
            self.rightendpoint = leftendpoint
            self.leftendpoint = leftendpoint

        elif (rightendpoint > leftendpoint):
            self.leftendpoint = leftendpoint
            self.rightendpoint = rightendpoint
        else:
            self.leftendpoint = rightendpoint
            self.rightendpoint = leftendpoint


    def __repr__(self):
        """
        This function is used for print out an interval project
        """
        return "[%s,%s]" % (self.leftendpoint, self.rightendpoint)

    def __add__(self, other):
        """
        This function is used for addition of two intervals
        """
        add = []
        if not isinstance(other, Interval):
            p1, q1 = self.leftendpoint, self.rightendpoint
            add.append(p1+other)
            add.append(q1+other)
        else:
            p1, q1 = self.leftendpoint, self.rightendpoint
            p2, q2 = other.leftendpoint, other.rightendpoint
            add.append(p1+p2)
            add.append(q1+q2)
        return Interval(add[0], add[1])



    def __sub__(self, other):
        """
        This function is used for subtraction of two intervals
        """

        sub = []
        p1, q1 = self.leftendpoint, self.rightendpoint
        p2, q2 = other.leftendpoint, other.rightendpoint
        sub.append(p1-q2)
        sub.append(q1-p2)
        return Interval(sub[0], sub[1])

    def __mul__(self, other):
        """
        This function is used for multiplication of two intervals
        """
        mult = []
        if not isinstance(other, Interval):
            return Interval(self.leftendpoint*other,self.rightendpoint*other)            
        else:    
            p1, q1 = self.leftendpoint, self.rightendpoint
            p2, q2 = other.leftendpoint, other.rightendpoint
            ac = p1*p2
            ad = p1*q2
            bc = p2*q1
            bd = q1*q2
            mult.append(min(ac, ad, bc, bd))
            mult.append(max(ac, ad, bc, bd))
            return Interval(mult[0], mult[1])

    def __truediv__(self, other):
        """
        This function is used for division of two intervals
        """

        div = []
        p1, q1 = self.leftendpoint, self.rightendpoint
        p2, q2 = other.leftendpoint, other.rightendpoint
        if (0 >= p2 and 0 <= q2):
            raise ZeroDivisionError("You tried to divide by zero!")
        ac = operator.__truediv__(p1, p2)
        ad = operator.__truediv__(p1, q2)
        bc = operator.__truediv__(q1, p2)
        bd = operator.__truediv__(q1, q2)
        div.append(min(ac, ad, bc, bd))
        div.append(max(ac, ad, bc, bd))
        for i in np.isfinite(div):
            if i != True:
                raise Exception('Is infinity')
        return Interval(div[0], div[1])

    def __pow__(self, other):
        """
        This function is used for power of on a interval
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

        return Interval(powe[0], powe[1])

    def __radd__(self, other):
        """
        Reverses the role of self and other
        """
        return self + other
        
        
    def __rmul__(self, other):
        """
        Reverses the role of self and other when multiplication is used
        """
        return self * other    
        
        
    def __contains__(self, value):
        """
        This function is used to check whether a specified value is within
        the interval
        """

        if not isinstance(
             self.leftendpoint, int) or isinstance(self.leftendpoint, float):
            raise TypeError('Left endpoint is not real value')
        if not isinstance(
             self.rightendpoint, int) or isinstance(self.rightendpoint, float):
            raise TypeError('Right endppoint is not real value')

        if (value <= self.rightendpoint and value >= self.leftendpoint):
            return True
        else:
            return False

    def plot_values():
        """
        Evaluates the polynomial p(x)=3x^3−2x^2+5x−1
        Plots lower boundaries and upper boundaries for y with respect to
        lower boundaries of x
        """
        
        """
        Implementation 1
        """
        yl = []
        yu = []
        xl = linspace(0., 1, 1000)
        xu = linspace(0., 1, 1000)+0.5
   
        list_of_interval=[]
        for l, u in list(zip(xl, xu)):
            list_of_interval.append(Interval(l,u))
            
        #print(len(list_of_interval))  
            
        total=[] 
        for f in list_of_interval:
            x=f
            p1=3*(x**3)
            p2=-2*(x**2)
            p3=5*x
            p4=-1
            #p=3*x**3-2*x**2+5*x-1
            total.append(p1+p2+p3+p4)
        
        
        for k in total:
            yl.append(k.leftendpoint)
            yu.append(k.rightendpoint)
        
 
        plot(xl, yl, label='yl')
        plot(xl, yu, label='yu') 
        
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
    print(Interval(2, 3) + 1)  # [3, 4]
    print(1 + Interval(2, 3))  # [3, 4]
    print(1.0 + Interval(2, 3))  # [3.0, 4.0]

    print("-----------------------------TASK 8-------------------------------")
    x = Interval(1, 5)
    print(x.__contains__(6))
    if 2 in x:
        print(True)
    else:
        print(False)

    print("-----------------------------TASK 9-------------------------------")
    x = Interval(-2, 2)  # [-2, 2]
    print(x**2)  # [0, 4]
    print(x**3)  # [-8, 8]

    print("-----------------------------TASK 10------------------------------")
    Interval.plot_values()
