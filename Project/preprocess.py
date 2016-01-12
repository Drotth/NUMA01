# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 22:11:37 2016
@author: Andreas Drotth
"""
from scipy import *
from pylab import *
from datetime import datetime
import re

def preprocessing():
    file = open("birds.txt", "r")  # Öppnar filen birds och läser den.
    listG = []  # Skapar en tom lista
    for line in file:
        listG.append(re.findall(r"[\w']+", line))

    listindex = []
    for a in range(len(listG)):
        listG[a-1] = [int(i) for i in listG[a-1]]  # makes them into integers
        listG[a] = [int(i) for i in listG[a]]
        diff = listG[a][7] - listG[a-1][7]

        if a > 0:
            if diff < 0:
                listindex.append(a)
    for i in range(len(listindex)):
        del listG[listindex[i]]  # we do this to delete the unwanted lines

    difflist = []
    dateslist = []

    for a in range(len(listG)):
        listG[a-1] = [int(i) for i in listG[a-1]]  # makes them into integers
        listG[a] = [int(i) for i in listG[a]]
        # datelist is a list of the dates as integers
        dateslist.append(listG[a][0:6])
        diff = listG[a][7]-listG[a-1][7]
        difflist.append(diff)

    for t in range(len(difflist)):
        if difflist[t] < 0:
            difflist[t] = 0  # changes difference to be 0 when there is a reset
        if difflist[t] > 8:
            difflist[t] = 8

    A = 0
    datalist = []

    for a in range(len(difflist)):
        A = difflist[a] + A
        datalist.append(A)

    finaldatalist = [k+70 for k in datalist]  # list comprehention

    finaldateslist = []
    for object in listG:
        frmt = '%Y-%m-%d %H:%M:%S.%f'
        a, b, c = line.split()
        finaldateslist.append(datetime.strptime(a + " " + b, frmt))
    
    return finaldateslist, finaldatalist
