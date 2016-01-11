# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 17:04:28 2016
@author: Andreas Drotth, Sebastian Olsson, TODO: FILL IN OTHERS
"""
from scipy import *
from pylab import *
from datetime import datetime
from datetime import timedelta
import pytz

list_dates = []
list_data = []
converted_dates = []
plot_dates = []
plot_data = []

# --------------------- TASK 1 ------------------------------------------------


def read_file():
    file = open("birds_26.txt", "r")

    for line in file:
        frmt = '%Y-%m-%d %H:%M:%S.%f'
        a, b, c = line.split()
        list_dates.append(datetime.strptime(a + " " + b, frmt))
        list_data.append(c)

# --------------------- TASK 2 ------------------------------------------------


def convert_local_timezone():

    for date in list_dates:
        local_tz = pytz.timezone('Europe/Stockholm')
        local_time = date.replace(tzinfo=pytz.utc).astimezone(local_tz)
        converted_dates.append(local_time)

# --------------------- TASK 3 ------------------------------------------------


def preprocessing():
    print("Preprocessing data")

# --------------------- TASK 4 ------------------------------------------------


def compute_data():
    start_date = input('Start date [YYYY-MM-DD]: ')
    days = input('Number of days: ')
    interval = input('Interval [0=2 mins, 1=hours, 2=days, 3=weeks]: ')
    date_1 = datetime.strptime(start_date, "%Y-%m-%d")

    collect_plot_dates(start_date)  # collect dates/data for start date

    if int(days) > 1:  # Repeat collection for each plus day separatly
        for t in range(1, int(days)):
            end_date = date_1 + timedelta(int(t))
            a, b = str(end_date).split()
            collect_plot_dates(a)

    # print(plot_data)
    # print(plot_dates)

    print(len(list_data))  # 2015-01-26 has 720 rows of data (this is verified)
    print(len(plot_data))  # 2015-01-26 has 720 rows of data (this is verified)
    print(len(modify_interval(interval)))  # Results in 24 hours
    print(modify_interval(interval))  # Gives the data in hours


def collect_plot_dates(start_date):
    first = 0
    last = 0
    temp_list = []

    for i in list_dates:
        if (start_date in str(i)):
            temp_list.append(list_dates.index(i))

    for i in converted_dates:
        a, b = str(i).split()
        if (start_date in a):
            plot_dates.append(i)

    first = temp_list[0]
    last = temp_list[-1]
    collect_plot_data(first, last)


def collect_plot_data(first, last):
    for k in range(first, last+1):
        plot_data.append(list_data[k])

    # list_for_interval = []
    # list_for_interval = list(zip(plot_dates, plot_data))


def modify_interval(interval):
    interval_list = []
    sum_value = 0
    index = 0

    if (interval == '0'):
        print("Interval is se to every 2 minute")  # use data as it is
    elif (interval == '1'):
        for data in plot_data:
            sum_value = sum_value + int(data)
            index = index + 1
            if (index is 30):  # Number of values in an hour
                interval_list.append(sum_value)
                index = 0
    elif (interval == '2'):
            for data in plot_data:
            sum_value = sum_value + int(data)
            index = index + 1
            if (index is 720):  # Number of values in a day
                interval_list.append(sum_value)
                index = 0
    elif (interval == '3'):
            for data in plot_data:
            sum_value = sum_value + int(data)
            index = index + 1
            if (index is 5040):  # Number of values in a week
                interval_list.append(sum_value)
                index = 0
    else:
        print("Not a valid interval")
  
    return interval_list

# --------------------- TASK 5 ------------------------------------------------


def plot_graph():
    print("Plot data")

# --------------------- TASK 6 ------------------------------------------------


def day_night_cycle():
    print("Visualize day and night cycle")


if __name__ == '__main__':
    read_file()
    convert_local_timezone()
    # preprocessing()
    compute_data()
    # plot_graph()
    # day_night_cycle()
