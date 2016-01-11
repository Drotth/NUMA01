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
    file = open("birds.txt", "r")

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
    interval = input('Interval [0=mins, 1=hours, 2=days, 3=weeks]: ')
    date_1 = datetime.strptime(start_date, "%Y-%m-%d")

    collect_plot_dates(start_date)  # collect dates/data for start date

    if int(days) > 1:  # Repeat collection for each plus day separatly
        for t in range(1, int(days)):
            end_date = date_1 + timedelta(int(t))
            a, b = str(end_date).split()
            collect_plot_dates(a)

    print(plot_data)
    print(plot_dates)


def collect_plot_dates(start_date):
    first = 0
    last = 0
    index = []

    for i in list_dates:
        if (start_date in str(i)):
            index.append(list_dates.index(i))

    for i in converted_dates:
        a, b = str(i).split()
        if (start_date in a):
            plot_dates.append(i)

    first = index[0]
    last = index[-1]
    collect_plot_data(first, last)


def collect_plot_data(first, last):
    for k in range(first, last+1):
        plot_data.append(list_data[k])

    list_for_interval = []
    list_for_interval = list(zip(plot_dates, plot_data))

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
