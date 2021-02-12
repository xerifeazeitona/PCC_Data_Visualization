"""
16-2. Sitka–Death Valley Comparison
The temperature scales on the Sitka and Death Valley graphs reflect the
different data ranges. To accurately compare the temperature range in 
Sitka to that of Death Valley, you need identical scales on the y-axis.
Change the settings for the y-axis on one or both of the charts.
Then make a direct comparison between temperature ranges in Sitka and
Death Valley (or any two places you want to compare).
"""
import csv
from datetime import datetime

import matplotlib.pyplot as plt

def get_temps(filename, dates, highs, lows, date_index, tmax_index, tmin_index):
    """fill dates, highs and lows from a csv file."""
    with open(filename) as file_obj:
        reader = csv.reader(file_obj)
        # Skip header row
        next(reader)

        # Get temperatures from the file.
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[tmax_index])
                low = int(row[tmin_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# Plot the temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Death Valley
dates, highs, lows = [], [], []
filename = '../data/death_valley_2018_simple.csv'
get_temps(filename, dates, highs, lows, 2, 4, 5)
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)

# Sitka
dates, highs, lows = [], [], []
filename = '../data/sitka_weather_2018_simple.csv'
get_temps(filename, dates, highs, lows, 2, 5, 6)
ax.plot(dates, highs, c='yellow')
ax.plot(dates, lows, c='green')
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.3)

# Format plot.
title = "Daily high and low temperatures - 2018"
title += "\nSitka vs Death Valley comparison"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.yticks([value for value in range(20, 131, 10)])

plt.show()
