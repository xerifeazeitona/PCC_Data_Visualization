"""
Now we can improve our temperature data plot by extracting dates for the
daily highs and passing those highs and dates to plot()
"""
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '../data/sitka_weather_07-2018_simple.csv'

with open(filename) as file_obj:
    reader = csv.reader(file_obj)
    header_row = next(reader)

    # Get high temperatures (TMAX) from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
# The call to fig.autofmt_xdate() draws the date labels diagonally to
# prevent them from overlapping.
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
