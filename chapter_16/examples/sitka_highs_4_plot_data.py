"""
To visualize the temperature data we have, we’ll first create a simple
plot of the daily highs using Matplotlib
"""
import csv

import matplotlib.pyplot as plt

filename = '../data/sitka_weather_07-2018_simple.csv'

with open(filename) as file_obj:
    reader = csv.reader(file_obj)
    header_row = next(reader)

    # Get high temperatures (TMAX) from this file.
    highs = [int(row[5]) for row in reader]

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Format plot.
plt.title("Daily high temperatures, July 2018", fontsize=24)
# Because we have yet to add the dates, we won’t label the x-axis, but 
# plt.xlabel() does modify the font size to make the default labels more
# readable.
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
