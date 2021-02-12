"""
16-1. Sitka Rainfall
Sitka is in a temperate rainforest, so it gets a fair amount of
rainfall. In the data file sitka_weather_2018_simple.csv is a header
called PRCP, which represents daily rainfall amounts.
Make a visualization focusing on the data in this column.
You can repeat the exercise for Death Valley if you’re curious how
little rainfall occurs in a desert.
"""
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '../data/sitka_weather_2018_simple.csv'

with open(filename) as file_obj:
    reader = csv.reader(file_obj)
    header_row = next(reader)

    # Get daily rainfall amounts from this file.
    dates, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        prcp = float(row[3])
        dates.append(current_date)
        prcps.append(prcp)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='blue')

# Format plot.
plt.title("Daily rainfall amounts - 2018\n Sitka", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Precipitation', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
