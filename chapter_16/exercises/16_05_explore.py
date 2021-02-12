"""
16-5. Explore
Generate a few more visualizations that examine any other weather aspect
you’re interested in for any locations you’re curious about.
"""
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '../data/sitka_weather_2018_full.csv'

with open(filename) as file_obj:
    reader = csv.reader(file_obj)
    header_row = next(reader)
    wind_index = header_row.index('AWND')
    date_index = header_row.index('DATE')
    location_index = header_row.index('NAME')

    # Get average winds (AWND) from this file.
    dates, winds = [], []
    location_name = ''
    for row in reader:
        if not location_name:
            location_name = row[location_index]
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            wind = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            winds.append(wind)

# Plot the wind averages.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, winds, c='green')

# Format plot.
title = "Daily wind averages\n"
title += location_name
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
