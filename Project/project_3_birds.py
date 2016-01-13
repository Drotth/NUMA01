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
from astral import Astral
from preprocess import preprocessing
import numpy as np
import matplotlib.pyplot as plt

list_dates = []
list_data = []
converted_dates = []
plot_dates = []
plot_data = []

# --------------------- TASK 2 ------------------------------------------------


def convert_local_timezone():

    for date in list_dates:
        local_tz = pytz.timezone('Europe/Stockholm')
        local_time = date.replace(tzinfo=pytz.utc).astimezone(local_tz)
        converted_dates.append(local_time)


# --------------------- TASK 4 ------------------------------------------------


def compute_data():
    start_date = '2015-01-26' #input('Start date [YYYY-MM-DD]: ')
    days = '1' #input('Number of days: ')
    date_1 = datetime.strptime(start_date, "%Y-%m-%d")

    collect_plot_dates(start_date)  # collect dates/data for start date

    if int(days) > 1:  # Repeat collection for each plus day separatly
        for t in range(1, int(days)):
            end_date = date_1 + timedelta(int(t))
            a, b = str(end_date).split()
            collect_plot_dates(a)

    array1 = np.array(plot_data)
    diff_array = np.diff(array1)
    graph_dates, graph_data, sun_indexes = graph_values(diff_array)

    return graph_dates, graph_data, sun_indexes


def collect_plot_dates(start_date):
    first = 0
    last = 0
    index_list = []

    for i in list_dates:
        if (start_date in str(i)):
            index_list.append(list_dates.index(i))

    for i in list_dates:
        a, b = str(i).split()
        if (start_date in a):
            plot_dates.append(i)

    first = index_list[0]
    last = index_list[-1]
    collect_plot_data(first, last)


def collect_plot_data(first, last):
    for k in range(first, last+1):
        plot_data.append(int(list_data[k]))


def graph_values(diff_array):
    graph_data = []
    graph_dates = []
    sum_value = 0
    index = 0
    current_hour = plot_dates[0].hour
    sun_indexes = []

    graph_dates.append(plot_dates[0].strftime('%Y-%m-%d'))

    city_name = 'Stockholm'
    a = Astral()
    a.solar_depression = 'civil'
    city = a[city_name]

    sunrise_found = False
    sunset_found = False
    sun = city.sun(plot_dates[0], local=True)

    for data in diff_array:
        if (plot_dates[index].hour > current_hour):
            graph_data.append(sum_value)
            sum_value = 0
            sum_value = sum_value + int(data)
            current_hour = current_hour + 1
            graph_dates.append(str(current_hour))
        elif (plot_dates[index].hour < current_hour):
            graph_data.append(sum_value)
            sum_value = 0
            sum_value = sum_value + int(data)
            current_hour = 0
            graph_dates.append(plot_dates[index].strftime('%Y-%m-%d'))
            sunrise_found = False
            sunset_found = False
            sun = city.sun(plot_dates[index], local=True)
        else:
            sum_value = sum_value + int(data)

        if (plot_dates[index].hour == sun['sunrise'].hour and sunrise_found == False):
            sun_indexes.append(current_hour)
            sunrise_found = True
        if (plot_dates[index].hour == sun['sunset'].hour and sunset_found == False):
            sun_indexes.append(current_hour)
            sunset_found = True

        index = index + 1

    graph_data.append(sum_value)

    print(sun_indexes)

    return graph_dates, graph_data, sun_indexes

# --------------------- TASK 5 ------------------------------------------------


def plot_graph(graph_dates, graph_data, sun_indexes):
    x_values = np.array(range(0, len(graph_dates)))
    y_values = np.array(graph_data)
    x_names = graph_dates
    
    
    x2_values = np.array(range(0, len(graph_dates)))
    y2_raw = [0,0,0,0,0,0,0,0,12,12,12,12,12,12,12,12,0,0,0,0,0,0,0,0]
    y2_values = np.array(y2_raw)
    
    plt.xticks(rotation=90)  # Roterar det som står på x-axeln
    plt.xticks(x_values, x_names)
    barWidth = 1  # Bredd på staplarna
    plt.bar(x2_values, y2_values, width=barWidth, align='center', color='y')
    plt.bar(x_values, y_values, width=barWidth, align='center')
    plt.show()

# --------------------- TASK 6 ------------------------------------------------


def day_night_cycle():
    city_name = 'Stockholm'
    a = Astral()
    a.solar_depression = 'civil'
    city = a[city_name]
    
    sun = city.sun(plot_dates[0], local=True)

if __name__ == '__main__':
    list_dates, list_data = preprocessing("birds.txt")
    convert_local_timezone()
    graph_dates, graph_data, sun_indexes = compute_data()
    plot_graph(graph_dates, graph_data, sun_indexes)
    day_night_cycle()
