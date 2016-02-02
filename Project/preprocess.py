"""
Created on Wed Jan 13 10:25:08 2016
@author: henrikoldehed
"""
from scipy import *
from pylab import *
from datetime import datetime
import re

# --------------------- TASK 1 & 3---------------------------------------------


def preprocessing(file_url):
    file = open(file_url, "r")  # Öppnar filen birds och läser den.
    listG = []  # Skapar en tom lista
    for line in file:
        listG.append(re.findall(r"[\w']+", line))

    listF = []
    for a in range(len(listG)):
        listG[a-1] = [int(i) for i in listG[a-1]]  # makes them into integers
        listG[a] = [int(i) for i in listG[a]]
        diff = listG[a][7] - listG[a-1][7]

        if a > 0:
            if  diff>=0 or listG[a][7] is 0:
                listF.append(listG[a])


    difflist = []
    dateslist = []

    for a in range(len(listF)):
        listF[a-1] = [int(i) for i in listF[a-1]] 
        listF[a] = [int(i) for i in listF[a]]
  
        dateslist.append(listF[a][0:6])
        diff = listF[a][7]-listF[a-1][7]
        difflist.append(diff)

    for t in range(len(difflist)):
        if difflist[t] < 0:
            difflist[t] = 0 
        if difflist[t] > 8:
            difflist[t] = 8

    A = 0
    datalist = []

    for a in range(len(difflist)):
        A = difflist[a] + A
        datalist.append(A)

    finaldatalist = [k+70 for k in datalist]  # list comprehention

    finaldateslist = []
    for obj in listF:
        del obj[7]
        new_date = datetime(*map(int, obj))
        finaldateslist.append(new_date)
    return finaldateslist, finaldatalist
#==============================================================================
#==============================================================================
# #     return finaldateslist, finaldatalist
#==============================================================================
#==============================================================================
