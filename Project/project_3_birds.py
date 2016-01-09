# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 17:04:28 2016
@author: Andreas Drotth, Sebastian Olsson, TODO: FILL IN REST
"""
from scipy import *
from pylab import *
from datetime import datetime 
from datetime import timedelta 
import pytz

list_date = []
newList = []
list_data = []
list_all = []
new_list_data=[]
# --------------------- TASK 1 ------------------------------------------------


def read_file():
    file = open("test.txt", "r")  
    

    for line in file:       
        frmt = '%Y-%m-%d %H:%M:%S.%f'
        a, b, c = line.split()  
        list_date.append(datetime.strptime(a + " " + b, frmt))
        list_data.append(c)

    return list_date

# --------------------- TASK 2 ------------------------------------------------


def convert_local_timezone(list_date):
   

    for date in list_date:  
        local_tz = pytz.timezone('Europe/Stockholm')  
        local_time = date.replace(tzinfo=pytz.utc).astimezone(local_tz)
        newList.append(local_time)  

    return newList

# --------------------- TASK 3 ------------------------------------------------


def preprocessing():
    print("preproc")

# --------------------- TASK 4 ------------------------------------------------


def compute_data():  
    start_date = input('Start date [YYYY-MM-DD]: ')
    days = input('Number of days: ')
    interval = input('Interval [0=mins, 1=hours, 2=days, 3=weeks]: ')
    date_1 = datetime.strptime(start_date, "%Y-%m-%d")

    set_date(start_date)
    for t in range(int(days)):
       end_date = date_1 + timedelta(int(t)+1) 
       print("End",str(end_date))
       a,b = str(end_date).split()
       #start_date=str(datetime.strptime(str(end_date), "%Y-%m-%d"))
       set_date(a)
         
            

def set_date(start_date):    
    first=0
    last=0
    index =[]
    for i in list_date:
        if (start_date in str(i)):
            index.append(list_date.index(i))
            #print("Index",list_date.index(i))
    
    first=index[0]
    last=index[-1]
    set_data(first,last)       
    del index[:]
    
def set_data(first,last):       
    for k in range(first,last+1):
        #print("Data",list_data[k])         
        new_list_data.append(list_data[k])

    print(new_list_data)

   
        
# --------------------- TASK 5 ------------------------------------------------


def plot_data():
    print("plot")
    
    
# --------------------- TASK 6 ------------------------------------------------
def visualize():
    print("Visualize")

    
if __name__ == '__main__':
    listG = read_file()
    newList = convert_local_timezone(listG)
    preprocessing()
    #for obj in newList:
    #    print(obj)
        
    compute_data()   
    plot_data()
    visualize()