"""
16-4. Automatic Indexes
In this section, we hardcoded the indexes corresponding to the TMIN and
TMAX columns. Use the header row to determine the indexes for these
values, so your program can work for Sitka or Death Valley.
Use the station name to automatically generate an appropriate title for
your graph as well.
"""
import csv
from datetime import datetime

import matplotlib.pyplot as plt

#filename = '../data/sitka_weather_2018_simple.csv'
filename = '../data/death_valley_2018_simple.csv'

with open(filename) as file_obj:
    reader = csv.reader(file_obj)
    header_row = next(reader)
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    date_index = header_row.index('DATE')
    location_index = header_row.index('NAME')

    # Get high temperatures (TMAX) from this file.
    dates, highs, lows = [], [], []
    location_name = ''
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        if not location_name:
            location_name = row[location_index]
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)

# Format plot.
title = "Daily high and low temperatures - 2018\n"
title += location_name
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
#plt.yticks([value for value in range(20, 131, 10)])


plt.show()
