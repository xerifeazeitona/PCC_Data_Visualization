"""
Using the list containing data about each earthquake, we can loop
through that list and extract any information we want. Now we’ll pull
the magnitude and location data of each earthquake.
"""
import json

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

print(mags[:10])
print(lons[:10])
print(lats[:10])
