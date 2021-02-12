"""
To finish this map, we’ll add some informative text that appears when
you hover over the marker representing an earthquake.
In addition to showing the longitude and latitude, which appear by
default, we’ll show the magnitude and provide a description of the
approximate location as well.
"""
import json

from plotly.graph_objs import Layout
from plotly import offline

# Explore the structure of the data.
filename = '../data/eq_data_30_day_m1.json'
filename = '/home/korporal/labs/PCC_Data_Visualization/chapter_16/data/eq_data_30_day_m1.json'
with open(filename) as file_obj:
    all_eq_data = json.load(file_obj)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat' :lats,
    'text': hover_texts,
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
