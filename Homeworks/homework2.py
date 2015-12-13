# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 22:37:48 2015
@author: Sebastian Olsson and Andreas Drotth
"""
from  scipy import *
from  pylab import *
import operator

class Interval(object):  
    def __init__(self,leftendpoint, rightendpoint):
        """
        Init (initialize) function is the first function called when an object creates
        Self represent the instance of the object itself
        """
        self.leftendpoint=leftendpoint
        self.rightendpoint=rightendpoint
        start=[self.leftendpoint,self.rightendpoint]
        print(start)
  

    def __add__(self,other):
        """
        This function is used fot addition on two intervals
        """
        add=[]
        p1, q1 = self.leftendpoint,self.rightendpoint
        p2, q2 = other.leftendpoint,other.rightendpoint
        add.append(p1+p2)
        add.append(q1+q2)
        return add      
    
    def __sub__(self,other):
        """
        This function is used for subtraction on two intervals
        """
        sub=[]
        p1, q1 = self.leftendpoint,self.rightendpoint
        p2, q2 = other.leftendpoint,other.rightendpoint
        sub.append(p1-q2)
        sub.append(q1-p2)
        return sub

    def __mul__(self,other):
        """
        This function is used for multiplication on two intervals
        """        
        mult=[]
        p1, q1 = self.leftendpoint,self.rightendpoint
        p2, q2 = other.leftendpoint,other.rightendpoint
        ac=p1*p2
        ad=p1*q2
        bc=p2*q1
        bd=q1*q2
        mult.append(min(ac,ad,bc,bd))
        mult.append(max(ac,ad,bc,bd))
        return mult
        
    def __truediv__(self,other):
        """
        This function is used for division on two intervals
        """        
        div=[]
        p1, q1 = self.leftendpoint,self.rightendpoint
        p2, q2 = other.leftendpoint,other.rightendpoint
        ac=operator.__truediv__(p1,p2)
        ad=operator.__truediv__(p1,q2)
        bc=operator.__truediv__(q1,p2)
        bd=operator.__truediv__(q1,q2)
        div.append(min(ac,ad,bc,bd))
        div.append(max(ac,ad,bc,bd))
        return div
        
       
    def __iadd__(self, other):
        iadd=[]
        self.leftendpoint += other.e
        print(self.leftendpoint)
        self.rightendpoint += other.e
        iadd.append(self.rightendpoint)
        iadd.append(self.leftendpoint)
        return iadd    

        
    
I1 = Interval(1,2) # [1, 2]
I2 = Interval(3, 4) # [3, 4]
print("Reslults:")
I3=I1 + I2 # [4, 6]
print(I3)
I4=I1 - I2 # [-3, -1]
print(I4)
I5=I1 * I2 # [3, 8]
print(I5)
I6=I1 / I2 # [0.25,0.6666666666666666]
print(I6)


#I7=Interval(2,3) + 1 # [3, 4]
#print(I7)
"""
1 + Interval(2,3) # [3, 4]
1.0 + Interval(2,3) # [3.0, 4.0]
"""  