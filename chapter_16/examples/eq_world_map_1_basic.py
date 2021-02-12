"""
With the info we’ve pulled so far, we can build a simple world map.
Although it won’t look presentable yet, we want to make sure the
information is displayed correctly before focusing on style and
presentation issues.
"""
import json

from plotly.graph_objs import Scattergeo, Layout
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
# A Scattergeo chart type allows you to overlay a scatter plot of
# geographic data on a map
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
