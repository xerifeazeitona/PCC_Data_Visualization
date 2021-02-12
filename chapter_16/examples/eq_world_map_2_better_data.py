"""
In the current chart, the data list is defined in one line. This is one
of the simplest ways to define the data for a chart in Plotly. But it’s
not the best way when you want to customize the presentation.
Changing the format allows us to specify customizations more easily than
the previous format.
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
    'lat' :lats
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
