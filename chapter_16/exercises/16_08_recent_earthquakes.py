"""
16-8. Recent Earthquakes
You can find data files containing information about the most recent
earthquakes over 1-hour, 1-day, 7-day, and 30-day periods online.
Go to https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php and
you’ll see a list of links to data sets for various time periods,
focusing on earthquakes of different magnitudes.
Download one of these data sets, and create a visualization of the most
recent earthquake activity.
"""
import json

from plotly.graph_objs import Layout
from plotly import offline

filename = '../data/recent_earthquakes.json'
with open(filename) as file_obj:
    all_eq_data = json.load(file_obj)

layout_title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat' :lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title=layout_title, title_font_size=24)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
