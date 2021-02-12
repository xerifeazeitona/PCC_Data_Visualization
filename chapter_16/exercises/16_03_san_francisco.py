"""
16-3. San Francisco
Are temperatures in San Francisco more like temperatures in Sitka or
temperatures in Death Valley? Download some data for San Francisco,
and generate a high-low temperature plot for San Francisco to make a
comparison.
"""
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '../data/san_fancisco_rain_2018.csv'

with open(filename) as file_obj:
    reader = csv.reader(file_obj)
    header_row = next(reader)

    # Get daily rainfall amounts from this file.
    dates, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        try:
            prcp = float(row[10])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            prcps.append(prcp)


# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='blue')

# Format plot.
plt.title("Daily rainfall amounts - 2018\n San Francisco", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Precipitation', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
