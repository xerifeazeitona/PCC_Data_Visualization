"""
The current map shows the location of each earthquake, but it doesn’t
communicate the severity of any earthquake. We want viewers to
immediately see where the most significant earthquakes occur in the
world.
To do this, we’ll change the size of markers depending on the magnitude
of each earthquake.
"""
import json

from plotly.graph_objs import Layout
from plotly import offline

# Explore the structure of the data.
filename = '../data/eq_data_1_day_m1.json'
with open(filename) as file_obj:
    all_eq_data = json.load(file_obj)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat' :lats,
    'marker': {
        'size': [5*mag for mag in mags],
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
