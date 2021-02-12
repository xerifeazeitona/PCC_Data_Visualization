"""
We can make our informative graph even more useful by including the low
temperatures. We need to extract the low temperatures from the data file
and then add them to our graph.
"""
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '../data/sitka_weather_2018_simple.csv'

with open(filename) as file_obj:
    reader = csv.reader(file_obj)
    header_row = next(reader)

    # Get high temperatures (TMAX) from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

# Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
