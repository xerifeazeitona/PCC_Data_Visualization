"""
We can also customize each marker’s color to provide some classification
to the severity of each earthquake.
"""
import json

from plotly.graph_objs import Layout
from plotly import offline

# Explore the structure of the data.
filename = '../data/eq_data_30_day_m1.json'
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
        # The 'color' setting tells Plotly what values it should use to
        # determine where each marker falls on the colorscale.
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
