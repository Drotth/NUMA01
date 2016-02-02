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
import matplotlib.dates as dates

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
    first_date = list_dates[0].date()
    last_date = list_dates[-1].date()

    checkstartdate = True
    while(checkstartdate):
        try:
            start_date = datetime.strptime(
                            input('Start date [YYYY-MM-DD]: '), "%Y-%m-%d")
            date_0 = start_date.date()
            checkstartdate = False

            if (date_0 > last_date or date_0 < first_date):
                print("The entered date is outside of the data range!")
                checkstartdate = True

        except:
            print("You have to write input on the form YYYY-MM-DD")

    checkinterval = True
    while(checkinterval):
        try:
            interval = int(input(
                         'Enter 1 for day interval and 2 for week interval: '))
            if(interval == 1):
                days = int(input('Number of days: '))
                checkinterval = False
            elif(interval == 2):
                nbrofweeks = int(input('Number of weeks: '))
                w = [start_date + timedelta(weeks=i) for i in range(
                        nbrofweeks+1)]
                delta = w[-1]-w[0]
                days = delta.days
                checkinterval = False
            else:
                print("You have to choose interval")
        except ValueError:
            print("You have to write an integer for the interval")

    plot_dates.clear()
    plot_data.clear()

    start_time = datetime.now()

    # One-loop version
    end_date = start_date + timedelta(days)
    collect_all(start_date, end_date)

    """
    # Several-loops version
    start_date2 = str(start_date.date())
    collect_plot_dates(start_date2)  # collect dates/data for start date
    if int(days) > 1:  # Repeat collection for each plus day separatly
        for t in range(1, int(days)):
            end_date = start_date + timedelta(int(t))
            a, b = str(end_date).split()
            collect_plot_dates(a)
    """

    stop_time = datetime.now()
    diff_time = stop_time - start_time
    print(diff_time.microseconds)

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
            plot_dates.append(i)

    first = index_list[0]
    last = index_list[-1]
    collect_plot_data(first, last)


def collect_plot_data(first, last):
    for k in range(first, last+1):
        plot_data.append(int(list_data[k]))


def collect_all(start_date, end_date):
    start_found = False
    collect_index = 0

    for datum in list_dates:
        if (start_found is False and start_date.date() == datum.date()):
            start_found = True
            plot_dates.append(datum)
            plot_data.append(int(list_data[collect_index]))
        elif (start_found is True):
            if (end_date.date() == datum.date()):
                break
            else:
                plot_dates.append(datum)
                plot_data.append(int(list_data[collect_index]))
        collect_index = collect_index + 1


def graph_values(diff_array):
    graph_data = []
    graph_dates = []
    sum_value = 0
    index = 0
    current_hour = plot_dates[0].hour
    sun_indexes = []

    city_name = 'Stockholm'
    a = Astral()
    a.solar_depression = 'civil'
    city = a[city_name]

    sunrise_found = False
    sunset_found = False
    sun = city.sun(plot_dates[0], local=True)

    graph_dates.append(plot_dates[0].strftime('%Y-%m-%d %H:%M:%S'))

    for data in diff_array:
        if (plot_dates[index].hour > current_hour):
            graph_data.append(sum_value)
            sum_value = 0
            sum_value = sum_value + int(data)
            current_hour = current_hour + 1
            graph_dates.append(plot_dates[index].strftime('%Y-%m-%d %H:%M:%S'))
        elif (plot_dates[index].hour < current_hour):
            graph_data.append(sum_value)
            sum_value = 0
            sum_value = sum_value + int(data)
            current_hour = 0
            graph_dates.append(plot_dates[index].strftime('%Y-%m-%d %H:%M:%S'))
            sunrise_found = False
            sunset_found = False
            sun = city.sun(plot_dates[index], local=True)
        else:
            sum_value = sum_value + int(data)

        if (plot_dates[index].hour is sun['sunrise'].hour and
                sunrise_found is False):
            sun_indexes.append(current_hour)
            sunrise_found = True
        if (plot_dates[index].hour is sun['sunset'].hour and
                sunset_found is False):
            sun_indexes.append(current_hour)
            sunset_found = True

        index = index + 1

    graph_data.append(sum_value)

    return graph_dates, graph_data, sun_indexes

# --------------------- TASK 5 ------------------------------------------------


def plot_graph(graph_dates, graph_data):
    x_values = []
    for i in graph_dates:
        x_values.append(datetime.strptime(i, '%Y-%m-%d %H:%M:%S'))

    y_values = np.array(graph_data)

    fig = plt.figure()

    ax = fig.add_subplot(111)
    barWidth = 1.0/(len(x_values) + 2)
    ax.bar(x_values, y_values, width=barWidth, color='green', align='center')

    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=45)
    plt.tight_layout()

    ax = plt.gca()

    xaxis = ax.get_xaxis()
    xaxis.set_major_locator(dates.DayLocator())
    xaxis.set_major_formatter(dates.DateFormatter('%Y-%m-%d'))

    space = 3
    start = 2
    end = 24

    hours = int((x_values[-1]-x_values[0]).total_seconds()/3600)+1
    if(hours > 96 and hours < 120):
        space = 5
    elif(hours > 120):
        space = 10

    xaxis.set_minor_locator(dates.HourLocator(byhour=range(start, end, space)))
    xaxis.set_minor_formatter(dates.DateFormatter('%H'))  # minor locator timme
    xaxis.set_tick_params(which='major', pad=18)  # sätter ner datumen 18 steg

    plt.title("Nesting box activities")
    plt.ylabel("In/out movements per hour")
    save_plot()
    plt.show()

# --------------------- TASK 6 ------------------------------------------------


def day_night_cycle():
    print("Visualize day and night cycle")

# --------------------- TASK 7 (EXTRA) ----------------------------------------


def save_plot():
    save = input('Press s to save graph as png file or enter to skip: ')
    if(save == 's'):
        plt.savefig('bird_movements.png', bbox_inches='tight')
        print("File saved as bird_movements.png in your working directory")

if __name__ == '__main__':
    list_dates, list_data = preprocessing("birds.txt")
    convert_local_timezone()
    continue_loop = 'y'
    while (continue_loop is 'y'):
        graph_dates, graph_data, sun_indexes = compute_data()
        plot_graph(graph_dates, graph_data)
        # day_night_cycle()
        continue_loop = input('Do you want to plot something more? [y/n]')
        if (continue_loop is not 'y' and continue_loop is not 'n'):
            print(
                "Since you apparently can't read, I'll shut it down for you.")
            continue_loop = 'n'
