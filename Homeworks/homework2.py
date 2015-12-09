# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 22:37:48 2015
@author: Sebastian Olsson and Andreas Drotth
"""
from  scipy import *
from  pylab import *

class Interval(object):
    def __init__(self,leftendpoint, rightendpoint):
        self.leftendpoint=leftendpoint
        self.rightendpoint=rightendpoint
        
        
    def addition(self,other):
        add=[]
        p1, q1 = self.leftendpoint,self.rightendpoint
        p2, q2 = other.leftendpoint,other.rightendpoint
        add.append(p1+p2)
        add.append(q1+q2)
        return add
    
    
        
    def subtraction(self,other):
        sub=[]
        p1, q1 = self.leftendpoint,self.rightendpoint
        p2, q2 = other.leftendpoint,other.rightendpoint
        sub.append(p1-q2)
        sub.append(q1-p2)
        return sub
        
   
    def multiplication(self,other):
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

    
    def division(self,other):        
        div=[]
        p1, q1 = self.leftendpoint,self.rightendpoint
        p2, q2 = other.leftendpoint,other.rightendpoint
        ac=p1/p2
        ad=p1/q2
        bc=p2/q1
        bd=q1/q2
        div.append(min(ac,ad,bc,bd))
        div.append(max(ac,ad,bc,bd))
        return div
        
        
    

    
I1 = Interval(1, 2) # [1, 2]
I2 = Interval(3, 4) # [3, 4]

print(I1.addition(I2))
print(I1.subtraction(I2))
print(I1.multiplication(I2))
print(I1.division(I2))
#I1 + I2 # [4, 6]
#I1 - I2 # [-3, -1]
#I1 * I2 # [3, 8]
#I1 / I2 # [0.25,0.6666666666666666]


  