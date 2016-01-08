# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 17:04:28 2016
@author: Andreas Drotth, Sebastian Olsson, TODO: FILL IN REST
"""
from scipy import *
from pylab import *
from datetime import datetime  
import pytz

# --------------------- TASK 1 ------------------------------------------------


def read_file():
    file = open("birds.txt", "r")  # Öppnar filen birds
    listG = []

    for line in file: 
        # Detta är en formatet för tiden och datumet
        frmt = '%Y-%m-%d %H:%M:%S.%f'
        a, b, c = line.split()  # Delar upp datum, tid och data till a, b och c
        # Lägger till a och b som datetimeobjects i listG
        listG.append(datetime.strptime(a + " " + b, frmt))

    return listG

# --------------------- TASK 2 ------------------------------------------------


def convert_local_timezone(listG):
    newList = []

    for date in listG:  # Variabeln date går igenom förra listan (listG)
        local_tz = pytz.timezone('Europe/Stockholm')  # Lokal tidszon
        # Variabeln date överförs till den lokala tidszonen
        local_time = date.replace(tzinfo=pytz.utc).astimezone(local_tz)
        newList.append(local_time)  # Lägger till nya tider i den nya listan

    return newList

# --------------------- TASK 3 ------------------------------------------------


def preprocessing():
    print("preproc")

# --------------------- TASK 4 ------------------------------------------------


def compute_data():
    print("compute data")    
    input_example = input('Enter your name: ')
    print('Hello', input_example)

# --------------------- TASK 5 ------------------------------------------------


def plot_value():
    print("plot")
    
    
# --------------------- TASK 6 ------------------------------------------------
def visualize():
    print("Visualize")

    
if __name__ == '__main__':
    listG = read_file()
    newList = convert_local_timezone(listG)
    preprocessing()
    for obj in newList:
        print(obj)
        
    compute_data()   
    plot_value()
    visualize()
    