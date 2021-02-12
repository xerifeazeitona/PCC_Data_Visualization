"""
16-9. World Fires
In the data folder, you’ll find a file called world_fires_1_day.csv.
This file contains information about fires burning in different
locations around the globe, including the latitude and longitude, and
the brightness of each fire.
Using the data processing work from the first part of this chapter and
the mapping work from this section, make a map that shows which parts of
the world are affected by fires.

You can download more recent versions of this data at
https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data/.
You can find links to the data in CSV format in the TXT section.
"""
import csv

from plotly.graph_objs import Layout
from plotly import offline

filename = '../data/world_fires_1_day.csv'

# Extract fire data from csv file.
with open(filename) as file_obj:
    reader = csv.reader(file_obj)
    header_row = next(reader)

    brights, lons, lats = [], [], []
    for row in reader:
        brights.append(float(row[2]))
        lons.append(row[1])
        lats.append(row[0])


# Map the fires.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat' :lats,
    'text': brights,
    'marker': {
        'size': [bright/20 for bright in brights],
        'color': brights,
        'colorscale': 'reds',
        'colorbar': {'title': 'Brightness'},
        'line': {'color': 'Gray'},
    },
}]
my_layout = Layout(title='World Fires', title_font_size=24)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')
